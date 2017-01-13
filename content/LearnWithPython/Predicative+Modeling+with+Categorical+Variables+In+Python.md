title: Predicative Modeling with Categorical Variables in Python   
date: 2016-12-01
Tag: ['Machine Learning','SkLearn']
description : I am going to deal with Categorical data which can't be fitted into ML algorithm in their raw. These are some methods by which you can convert categorical data into numeric data.
keywords : Dealing with Categorical Variable, Categorical Variable in Python, covert categorical variable into continuous,categorical value into numeric, sklearn LabelEncoder, Pandas get_dummies
author : Sajjan Kumar

Sometime data-set contains both continuous and categorical variables. Usually we skip the categorical variables but in some cases categorical variable contains information that we don't want to skip. In that cases we have to prepare our model for categorical data as we can't fit categorical variable into regression/classification equation in there row form. They must be treated. Also Most ML algorithm gives best result with numeric data. 

Recently I was making a predictive model. That's works fine on continuous data but that can't be used for categorical data. To deal with categorical data either you have to change the data into numeric or switch to another model. Now I have a situation that how can I change my categorical data into numeric values using Python, To solve this let's get started.

#### What is categorical variable/data?

In a data-set the value for particular column/variable is not represented by some numeric value. Instead it is represented by some string value. These string value create different levels for that variable.
    
Ex.

1.  In a dataset variable 'sex' have two levels which is represented by string 'male' and 'female'.
2. In a data-set, variable country is a categorical variable and it can have different number of value so the Level formed by this variable depends on the different value country. 
 


Now moving to our programming part!
The data-set is Titanic data-set.

Lets First import our modules


	import pandas as pd
	import numpy as np

load our data

	data= pd.read_csv(r'E:\python\data\titanic.csv')


Let's take a look on our data


	data.head()


Output:



<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>



## Method First - By Inspection:

Sometime by using a small python script, we can convert our categorical or non-leveled data into a more sophisticated data so that our classification model can give best result. Let's Check...


This data range from age 0.8 to age 80. So what we can do we can divide this in 5 Levels where each level represents 
an age group ranging from 0 to 15.
if there is an 'NaN' value,  I am going to replace by putting that into a level between range age 30 to age 45.



	age= data['Age']
	age_processed=[]


	for i in age:
    	if i < 15.0:
    	    age_processed.append(int(1))
    	elif i >= 15.0 or i < 30.0:
    	    age_processed.append(int(2))
    	elif i >= 30.0 or i < 45.0:
    	    age_processed.append(int(3))
    	elif i >= 45.0 or i< 60.0:
    	    age_processed.append(int(4))
    	elif i >= 60.0:
    	    age_processed.append(int(5))
    	else:
    	    age_processed.append(int(2))




Now by using a simple python script, our data has been transformed into a 5-leveled value.



## Method Second : Using Python's Sklearn LabelEncoder

Python's sklearn provide a method to deal with categorical data using label encoding. This method is used to per-process data before applying to any model.



	new_data= pd.DataFrame()

first import our library

	from sklearn import preprocessing

Now define our label encoder
 
	le= preprocessing.LabelEncoder()

Now tell our encoder that how much types of label we have.
let's our categorical variable(Country) have below values
 
	le.fit(['India','China','USA','UK','Bangladesh','Japan', 'Spain'])

The data has been fitted to model. So Check how many classes are defined.

	le.classes_

Output:

    array(['Bangladesh', 'China', 'India', 'Japan', 'Spain', 'UK', 'USA'], 
          dtype='|S10')


Now let's transform some data from categorical to numeric values.


	Country=['India','China','USA','India','China','USA','UK','Bangladesh','Japan', 'Spain','UK','Bangladesh',
         'India','China','India','China','USA','UK','Bangladesh','Japan', 'Spain','USA',
         'UK','Bangladesh','Japan', 'Spain','Japan', 'Spain',]

	country_nuemeric= le.transform(Country)

Transformation has been done. Now check how the array country_numeric look a like.

	country_nuemeric

Output :

    array([2, 1, 6, 2, 1, 6, 5, 0, 3, 4, 5, 0, 2, 1, 2, 1, 6, 5, 0, 3, 4, 6, 5,
           0, 3, 4, 3, 4])



Our data has been transformed and each integer value represent corresponding to le.classes_ output.  

## Method Third : Using dummy coding 

Python's data manipulation library Pandas also provides a method to deal with categorical data. 


	new_df= pd.get_dummies(data['Embarked'])

Data has been transformed into new variables.  

	new_df.head()





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>Q</th>
      <th>S</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



Here Embarked variable has three values (Level) 'C', 'Q', and 'S'. Pandas's get_dummies create three new variable in the data-frame and assign the value accordingly. for a single row only one column will have active value(1).

So if the value for categorical variable have limited variation then it can be helpful.Now the new data can be joined with existing data or treated separately.

## Final Thought:-

It would be difficult to tell you about the best method fit for you. you have to check that for yourself.
Got anything about this post, Hit email me!


