title: Dealing With Missing Values Using Sklearn and Pandas 
date: 2016-12-02
Tag: ['SkLearn','Pandas']
description : Real world data sets contain missing values. These values encoded as blanks, NaNs or other placeholders. Below methods can be used to fill out the missing values
keywords : Pandas fillna, filling missing value, deal with missing value python, sklearn Imputer function, handling missing value, imputation of missing values
author : Sajjan Kumar

Real world data sets contain missing values. These values encoded as blanks, NaNs or other placeholders. we are used to skip that entire row/columns containing missing value while describing a machine learning model. However this comes at the price of losing data. 

A good strategy is to fill out the missing values using known part of the data. The Imputer class provides basic strategies for imputing missing values, either using the mean, the median or the most frequent value of the row or column in which the missing values are located. Let's Check


first import our module and grab our data 

	import pandas as pd

	data= pd.read_csv(r'titanic.csv')


Let's Grab some column data which has some missing values. Have a look.

	data['Age'].values[1:30]

Output :

    array([ 38.,  26.,  35.,  35.,  nan,  54.,   2.,  27.,  14.,   4.,  58.,
            20.,  39.,  14.,  55.,   2.,  nan,  31.,  nan,  35.,  34.,  15.,
            28.,   8.,  38.,  nan,  19.,  nan,  nan])



Here one can see missing values are represented as 'nan' (nan in Numpy array and NaN in pandas dataframe).Below are some method by which missing value can be handled.

1. Using sklearn.preprocessing Imputer function

2. Using Pandas fillna() method

## 1. Using Sklearn Imputer Function

import imputer class from sklearn.preprocessing

	from sklearn.preprocessing import Imputer

define our imputer. here we will describe missing_value placeholder, strategy used to fill out the value and axis.

	imp = Imputer(missing_values='NaN', strategy='mean', axis=0)

check out the imputer

	print imp

Output 

    Imputer(axis=0, copy=True, missing_values='NaN', strategy='mean', verbose=0)
    

Here some additional variables axis, verbose are set to default.
Now let's fit our data to our Imputer.

	imp.fit(data['Age'].values.reshape(-1,1)) 

Output
 
	Imputer(axis=0, copy=True, missing_values='NaN', strategy='mean', verbose=0)


Now transform our data replacing Nan with appropriate mean value.

	age_reformed= imp.transform(data['Age'].values.reshape(-1,1))

Now Check the transformed data.

	age_reformed[1:10]

Output

    array([[ 38.        ],
           [ 26.        ],
           [ 35.        ],
           [ 35.        ],
           [ 29.69911765],
           [ 54.        ],
           [  2.        ],
           [ 27.        ],
           [ 14.        ]])



Now these "nan" values has been transformed into mean value(29.69911765). The data after transformation can be used to machine learning model
as it doesn't have missing value.

## 2. Using Pandas fillna() 

Python's pandas library provide a direct way to deal with missing value. 

First create a new data frame with column value as age.

	df= pd.DataFrame(columns=['age'])
	df['age']= data['Age'].values

We have missing values in newly created Dataframe.

	df.head(10)

Output
 

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>22.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>38.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>26.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>35.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>35.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>54.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>27.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>14.0</td>
    </tr>
  </tbody>
</table>
</div>


Pandas fillna method is applied to dataframe as

	DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)

Now apply this to our data and put a value equal to 25 where nan occurs.

	filled_value=df.fillna(25)

Check the filled value
 
	fill_value.head(10)

Output:

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>22.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>38.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>26.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>35.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>35.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>54.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>27.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>14.0</td>
    </tr>
  </tbody>
</table>
</div>


Here value in 6th row(5th indexed) has been changed from 'NaN' to 25.0.
More information about the default variable can be checked from docs.

Pandas's DataFrame fillan:-

[http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.fillna.html](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.fillna.html)

Pandas's Series fillna:-
  
[http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.fillna.html](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.fillna.html)


Got something about this post, Hit Email me.