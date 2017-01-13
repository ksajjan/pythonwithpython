title: Feature Scaling with Python and Sklearn  
date: 2016-12-22
Tag: ['SkLearn','SKLearn']
description : Sometime we have to pre-process our data before applying a machine learning algorithm. Below Methods can be used..
keywords : scale(), MinMaxScale(), MaxAbsScaler(), custom data transformation with python, pre-processing of data python, sklearn data preprocessing, python normalization, Binarization using python.  
author : Sajjan Kumar


Sometime before applying a machine learning algorithm on your dataset, first you have to do some pre-processing for your data. For this purpose Sklearn provide a package to deal with such scenario. Here We will use that to make our work easy.
Pre-processing may include Standardization, normalization, Binarization, imputation of missing value etc. Now get ready and start importing !


importing pandas, and numpy
 
	import pandas as pd 
	import numpy as np


Nothing special, Just loading our data

	data=pd.read_csv(r'E:\python\from hp\train.csv')
	Fare= data['Fare'].values[:40]

Check our input
 
	print Fare

Output:

    [   7.25     71.2833    7.925    53.1       8.05      8.4583   51.8625
       21.075    11.1333   30.0708   16.7      26.55      8.05     31.275
        7.8542   16.       29.125    13.       18.        7.225    26.       13.
        8.0292   35.5      21.075    31.3875    7.225   263.        7.8792
        7.8958   27.7208  146.5208    7.75     10.5      82.1708   52.
        7.2292    8.05     18.       11.2417]
    

This would be our input data which is going to be scaled.

Now starting our, first import pre-processing from sklearn. All the other magic tools are under the pre-processing.


	from sklearn import preprocessing


### scale() Function:
The function **scale** provide a basic overview of pre-processing. The scale function will transform your data between -1 to 1.



Apply the function to our input data(Fare) and store the output into other variable called fare_scaled.

	fare_scaled= preprocessing.scale(Fare)

Check the scaled input :
 
	print fare_scaled

Output:

    [-0.51857041  0.88523827 -0.50377232  0.4866039  -0.50103193 -0.49208073
      0.45947406 -0.2154835  -0.43343642 -0.01826765 -0.31139708 -0.09545451
     -0.50103193  0.00813216 -0.50532447 -0.32674325 -0.03900252 -0.39251257
     -0.28289705 -0.51911849 -0.10751222 -0.39251257 -0.50148793  0.10075727
     -0.2154835   0.01059851 -0.51911849  5.08826339 -0.5047764  -0.50441247
     -0.06978694  2.5346778  -0.50760886 -0.44732033  1.12392606  0.46248848
     -0.51902641 -0.50103193 -0.28289705 -0.43105996]
    

The data has been scaled and now its lie between -1,1.

### Scaling features to a range

Sometime data should be scaled between some minimum and maximum value, often between zero and one. This can be achieved using **MinMaxScaler** or **MaxAbsScaler**. Let's try that.


First define our min_max_scaler and let's say we want to scale our data between a range 0 to 5.
	min_max_scaler= preprocessing.MinMaxScaler(feature_range=(0,5))
	print min_max_scaler

Output:

    MinMaxScaler(copy=True, feature_range=(0, 5))
    

Now transform our data using min_max_scaler

	fare_transformed= min_max_scaler.fit_transform(Fare.reshape(-1,1))
	
	print fare_transformed.reshape(1,-1) #Using reshape(1,-1) just for better view
		
Output:

    [[  4.88710781e-04   1.25223927e+00   1.36839019e-02   8.96784283e-01
        1.61274558e-02   2.41090802e-02   8.72593099e-01   2.70745773e-01
        7.64011338e-02   4.46599550e-01   1.85221386e-01   3.77773434e-01
        1.61274558e-02   4.70139771e-01   1.22998729e-02   1.71537484e-01
        4.28110644e-01   1.12892190e-01   2.10634347e-01   0.00000000e+00
        3.67021797e-01   1.12892190e-01   1.57208484e-02   5.52731893e-01
        2.70745773e-01   4.72338970e-01   0.00000000e+00   5.00000000e+00
        1.27885837e-02   1.31130877e-02   4.00660737e-01   2.72301437e+00
        1.02629264e-02   6.40211123e-02   1.46507282e+00   8.75281009e-01
        8.21034112e-05   1.61274558e-02   2.10634347e-01   7.85201838e-02]]
    

The scaled data is now lie in range between 0 to 5. Here we can provide any range in which we want our data to be scaled.

The transformation for **MinMaxScaler()** is given by:

    X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
    X_scaled = X_std * (max - min) + min
    
where min, max = feature_range.

Now Let's move to our other scaling function **MaxAbsScaler**.It scale each feature by its maximum absolute value.



first define our maxabs scaler

	maxabs_scaler= preprocessing.MaxAbsScaler()
	print maxabs_scaler

Output:

    MaxAbsScaler(copy=True)
    

Now transform the data using maxabs_scaler.fit_transform(). The output is stored into another variable called fare_maxabs_scaled.

	fare_maxabs_scaled= maxabs_scaler.fit_transform(Fare.reshape(-1,1))
	print fare_maxabs_scaled.reshape(1,-1) #reshape is just for preety view

Output:

    [[ 0.02756654  0.27103916  0.03013308  0.20190114  0.03060837  0.03216084
       0.19719582  0.08013308  0.04233194  0.11433764  0.0634981   0.10095057
       0.03060837  0.11891635  0.02986388  0.0608365   0.11074144  0.04942966
       0.06844106  0.02747148  0.09885932  0.04942966  0.03052928  0.13498099
       0.08013308  0.11934411  0.02747148  1.          0.02995894  0.03002205
       0.10540228  0.55711331  0.02946768  0.03992395  0.3124365   0.19771863
       0.02748745  0.03060837  0.06844106  0.04274411]]
    

### Normalization 

Normalization is the process of scaling individual samples to have unit norm.
The function normalize() provides a quick and easy way to perform normalization on a array-like dataset, either using the l1 or l2 norms:

Check Example :


Normalization using normalize(x)

	fare_normalized = preprocessing.normalize(Fare.reshape(1,-1), norm="l1")


Check the output

	print fare_normalized

Output:

    [[ 0.00586493  0.057665    0.00641097  0.04295552  0.00651209  0.00684239
       0.04195444  0.01704873  0.00900634  0.02432593  0.01350955  0.02147776
       0.00651209  0.02530007  0.0063537   0.01294328  0.02356082  0.01051642
       0.01456119  0.0058447   0.02103284  0.01051642  0.00649526  0.02871791
       0.01704873  0.02539108  0.0058447   0.21275522  0.00637392  0.00638735
       0.02242489  0.11852876  0.0062694   0.00849403  0.0664725   0.04206567
       0.0058481   0.00651209  0.01456119  0.00909403]]
    

### Binarization

Binarization is the process of thresholding numerical features to get boolean values.it binarize data (set feature values to 0 or 1) according to a threshold.Values greater than the threshold map to 1, while values less than or equal to the threshold map to 0.

Check the example Below.
First check what our Fare data looks alike .


	print Fare

Output:

    [   7.25     71.2833    7.925    53.1       8.05      8.4583   51.8625
       21.075    11.1333   30.0708   16.7      26.55      8.05     31.275
        7.8542   16.       29.125    13.       18.        7.225    26.       13.
        8.0292   35.5      21.075    31.3875    7.225   263.        7.8792
        7.8958]
    

Now Let's Binarize it. Divide it into two groups fare less than 15.0 and fare more than 15.0 . <br>

Put a threshold value equal to 15.0 so that binarizer convert fare less than 15.0 as 0 and fare more than 15.0 as 1. 

Let's do this.


First define our binarizer:
 
	binarizer = preprocessing.Binarizer(threshold=15.0)
	print binarizer

Output:

    Binarizer(copy=True, threshold=15.0)
    



Now transform our data and store it in variable called fare_binarized.

	fare_binarized=binarizer.transform(Fare.reshape(-1,1))
	print fare_binarized.reshape(1,-1)

Output:

    [[ 0.  1.  0.  1.  0.  0.  1.  1.  0.  1.  1.  1.  0.  1.  0.  1.  1.  0.
       1.  0.  1.  0.  0.  1.  1.  1.  0.  1.  0.  0.  1.  1.  0.  0.  1.  1.
       0.  0.  1.  0.]]
    

Here Values above 15.0 are converted into 1 and value less than or equal to are converted to 0. 

### Custom transformers

Sklearn provides some method for custom transformation of data. If a function of your choice isn't listed then you can create your own function for transformation using FunctionTransformer() function.

Check example below

First define our input let's it is

	x=np.array([[121,424],[986,361]])
	print x

Output:


    [[121 424]
     [986 361]]
    
*Let's say we want to take square root of our input.* We will do this with the help of sklearn.

Call the function FunctionTransformer() with appropriate function(here will take square root of the given input, so will use np.sqrt )

	custom_transformer = preprocessing.FunctionTransformer(np.sqrt)

Now Transform our input using custom_transformer function
 
	x_transformed= custom_transformer.transform(x)

Let's Check what we have transformed.
 
	print x_transformed

Output:

    [[ 11.          20.59126028]
     [ 31.40063694  19.        ]]
    

As we can see the output is perfect square root of input x. More about custom transformation can be learn from <a href="http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer">docs </a>

In feature scaling, Imputation of missing value and Encoding Categorical feature is also important. I have separately written on these two topics. You should read these to complete **feature scaling**.

1. <a href="http://sajjan.xyz/posts/+Imputation+of+missing+values+using+sklearn/index.html" >Imputation of Missing values using Sklearn </a>

2. <a href="http://sajjan.xyz/posts/Predicative+Modeling+with+Categorical+Variables+In+Python/index.html" > Predictive Modeling with Categorical Variable  </a>


Thanks for reading. Got anything in  mind, Hit **"Email me"**.