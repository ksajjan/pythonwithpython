title: Machine Learning with Naive Bayes Classification
date: 2016-11-26
Tag: ['Machine Learning','SkLearn']
description : Changing the different Parameters of Naive Bayes Algorithm to Find the best pair of parameter.
keywords : Naive Bayes Examples, Supervised learning example, machine learning, Naive Bayes classification
author : Sajjan Kumar

**Machine Learning : Intro**

In general, a Learning problem considers a set of n samples of data and then tries to predict properties of unknown data. we can separate learning problems in a few categories:<br>

**1. Supervised Learning :**
In this type of learning the data comes with additional attributes(features) that we want to predict. This problem can be either: <br>

**a. classification :**
 
Samples belong to two or more classes and we want to learn from already labeled data and then predict the class of unlabeled data.
 
**b. Regression:**
 
if the desired output consists of one or more continuous variable, then the task is call <b> Regression.</b> 
            
**2. Unsupervised Learning:** 

In this learning the training data consists of a set of input vectors x without any corresponding target values. The goal in such problem may be to discover groups of similar examples within the data, where it is called **clustering**, or to determine the distribution of data within the input space, known as **density estimation**.


## About this post:
This post is the first one of this series. In this series I will explain some of Machine learning algorithms and play with their different parameter. There is different accuracy for different values of different parameters. <br>
The Data-set I am going to use Titanic data set. More about data-set  [https://www.kaggle.com/c/titanic](https://www.kaggle.com/c/titanic "here") 

## Naive Bayes Algorithm :
In this particular post I am going use Naive Bayes algorithm.Naive Bayes methods are a set of supervised learning algorithms based on applying Bayes theorem with the “naive” assumption of independence between every pair of features.<br>

Naive Bayes algorithm provide three *methods for classification*.<br>
1. Gaussian Naive Bayes (GaussianNB) <br>
2. Bernoulli Naive Bayes (BernoulliNB) <br>
3. Multinomial Naive Bayes (MultinomialNB)

Here I am not going into details about Bayes'theorm or any mathematical formulation, let's do some programming.

*first import our modules. I use pandas and Numpy for most of my work.* 




	import pandas as pd
	import numpy as np

	from sklearn.naive_bayes import GaussianNB
	from sklearn.metrics import accuracy_score




*import our data which is train.csv*

	data=pd.read_csv(r'train.csv')

Let's take a look on our data 
 
	data.head()




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





Let's scrape some handful data from it.
we will use naive bayes classifier to predict the Survival factor based on different parameter
(features).
Here our features will be Class of passanger(Pclass), Sibling-spouse-aboard(SibSp) and Parent-children-aboard(Parch) and labels
will be Survival(Survived).
 
	target= data['Survived'].values 
	pclass= data['Pclass'].values
	age= data['Age'].values
	sibsp= data['SibSp'].values
	parch= data['Parch'].values

Check the shape of our data
	print target.shape
	print pclass.shape

Output :

	(891,)
	(891,)
    

Now Let's dig in and  write some code for our classifier. I am going to write a function which return accuracy for given feature data and classifier.



	def classifier_accuracy(clf,features, labels):

    	# divde our features into test and train data 
    	#here we know the size of data and we can divide the data as we want. 

    	features_train= features[:700]
    	features_test= features[700:]
    
    	#Dividing labels into train and test

    	labels_train = labels[0:700]
    	labels_test= labels[700:]
    
    	#here clf is our classifier which is defined with naive bayes methods.
    	#Let's train our data
 
    	clf.fit(features_train.reshape(len(features_train),1),labels_train)
    
    	# the below line of code will predict the outcome with input test features.This outcome will be based on how we
    	#train our model. predic varaible is used to hold the outcome.
 
    	predic= clf.predict(features_test.reshape(len(features_test),1))
    
    	# Now let's check the accuracy using sklearn's accuracy_score here the input for this will be the the predication made
    	#by our model and the actual values which is test label.
 
    	return accuracy_score(predic,labels_test)






# Gaussian Naive Bayes classifier.
Let's start with our first classifier which would be Gaussian Naive Bayes Classifier. GaussianNB implements the Gaussian Naive Bayes algorithm for classification. The likelihood of the features is assumed to be Gaussian.



	clf=GaussianNB()


Additionally Gaussian Naive Bayes take a <b> priors </b> parameter. Which is "Prior probabilities of the classes. If specified the priors are not adjusted according to the data". More can be learn from documentation.[http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB)


#####It's time to call our function classifier_accuracy with appropriate inputs.



	# let's check accuracy for passanger class and 
	#other features set one by one. Here classifer would be GaussianNB.

	accuracy_1=classifier_accuracy(clf,pclass,target)
	print accuracy_1

	accuracy_2=classifier_accuracy(clf,sibsp,target)
	print accuracy_2
	
	accuracy_3=classifier_accuracy(clf,parch,target)
	print accuracy_3


Output for above code would be :

	0.738219895288
	0.628272251309
	0.628272251309
    



we have 73% accuracy while predicating survival factor based on passenger class.

    

# Bernoulli Naive Bayes Classifier

***BernoulliNB implements*** the naive Bayes training and classification algorithms for data that is distributed according to multivariate Bernoulli distributions; i.e., there may be multiple features but each one is assumed to be a binary-valued (Bernoulli, Boolean) variable. Therefore, this class requires samples to be represented as binary-valued feature vectors; if handed any other kind of data, a BernoulliNB instance may binarize its input (depending on the binarize parameter).
More - [http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB)


	from sklearn.naive_bayes import BernoulliNB




Let's define our second classifier and also notice the different default parameters in the output. 

	clf2= BernoulliNB()
	print clf2

Output

	BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True)
    

Now Check for accuracy. Here the classifier would be BernoulliNB classifier. 

	accuracy_4=classifier_accuracy(clf2,pclass,target)
	print accuracy_4


	accuracy_5=classifier_accuracy(clf2,sibsp,target)
	print accuracy_5

	accuracy_6=classifier_accuracy(clf2,parch,target)
	print accuracy_6


Output:
 
	0.628272251309 
	0.628272251309
	0.628272251309
    
    

####Here accuracy is same for all features.

Additional classifier parameter like <b> alpha, binarize </b> are set to defaults. *Let adjust them one by one and try to increase the accuracy.*

<b> alpha </b> by default it is 1.0 and  it represents "*Additive (Laplace/Lidstone) smoothing parameter (0 for no smoothing)*." 
The smoothing priors <b> alpha</b> accounts for features not present in the learning samples and prevents zero probabilities in further computations. Setting alpha = 1 is called Laplace smoothing, while alpha < 1 is called Lidstone smoothing.
I will use different value of alpha and check for corresponding accuracy. 



	clf3= BernoulliNB(alpha=10.0)
	print clf3

	accuracy_7=classifier_accuracy(clf3,pclass,target)
	print accuracy_7
Output:

    BernoulliNB(alpha=10.0, binarize=0.0, class_prior=None, fit_prior=True)
    0.628272251309
    
Let's change the alpha to 100.0

	clf3= BernoulliNB(alpha=100.0)
	print clf3

	accuracy_7=classifier_accuracy(clf3,pclass,target)
	print accuracy_7

Output:

    BernoulliNB(alpha=100.0, binarize=0.0, class_prior=None, fit_prior=True)
    0.628272251309
    
Again change alpha to  0.0003

	clf3= BernoulliNB(alpha=0.0003)
	print clf3

	accuracy_7=classifier_accuracy(clf3,pclass,target)
	print accuracy_7

Output

    BernoulliNB(alpha=0.0003, binarize=0.0, class_prior=None, fit_prior=True)
    0.628272251309
    

so after trying different value of alpha, one thing is clear <b> <i> it has no effect on accuracy on  this data-set</i> </b> even for negative value of alpha.Accuracy from different values is same as with default values. <br>

Now let's take a look with our second parameter <b> binarize </b> by default it is 0.0 and it represents "Threshold for binarizing (mapping to booleans) of sample features. If None, input is presumed to already consist of binary vectors."<br>
Let's Begin



	clf4= BernoulliNB(binarize=1.0)
	print clf4

	accuracy_8=classifier_accuracy(clf4,pclass,target)
	print accuracy_8
Output:

    BernoulliNB(alpha=1.0, binarize=1.0, class_prior=None, fit_prior=True)
    0.738219895288
    

***Accuracy increased!(cool)*** So with increasing <b> binarize </b>accuracy is increasing. Right? Let's check



	clf4= BernoulliNB(binarize=10.0)
	print clf4

	accuracy_8=classifier_accuracy(clf4,pclass,target)
	print accuracy_8

Output:

    BernoulliNB(alpha=1.0, binarize=10.0, class_prior=None, fit_prior=True)
    0.628272251309
    

What did just happen ? I used <b> binarize=10.0 </b> and thought accuracy would be higher than previous <b> binarize=1.0 </b> but just opposite happen. I don't know what is going on. <br>
Let's try another value and then generalize it.



	clf4= BernoulliNB(binarize=2.0)
	print clf4

	accuracy_8=classifier_accuracy(clf4,pclass,target)
	print accuracy_8

Output

    BernoulliNB(alpha=1.0, binarize=2.0, class_prior=None, fit_prior=True)
    0.701570680628
    

**Decreased!** OK Let's Combine all of these, with binarize=1.0 our accuracy is maximum and then it is decreasing with increasing value of binarize. Also certain maximum and minimum level is set for accuracy as maximum accuracy would be 0.738219895288 which is equivalent to Gaussian Naive bayes classifier and minimum accuracy is 0.628272251309 which is same accuracy with default parameters. <br>

Let's check our third parameter <b> fit_prior </b> which is by default True and it represents "Whether to learn class prior probabilities or not. If false, a uniform prior will be used". It accepts boolean value. Now check what will happen if we change fit_prior from True to False?



	clf5= BernoulliNB(fit_prior=False)
	print clf5

	accuracy_9=classifier(clf5,pclass,target)
	print accuracy_9

Output:

    BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=False)
    0.628272251309
    

**NOTHING!** YES, No change in accuracy. it is same as with the default value.

**Key Note:** Accuracy can be changed by adjusting the different parameters of the classifier. These parameters can vary from data to data.So you have to find the right set of parameters for your classification.

# MultinomialNB

MultinomialNB implements the naive Bayes algorithm for multinomially distributed data, and is one of the two classic naive Bayes variants used in text classification.



	from sklearn.naive_bayes import MultinomialNB
	clf6= MultinomialNB()
	print clf6

	accuracy_10=classifier(clf6,pclass,target)
	print accuracy_10
Output

    MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
    0.628272251309
    

The accuracy is same as previous one(BernoulliNB) and changing its parameter won't change anything in accuracy( go ahead and try it). 


# Two Words : 

1. Among the three classifier (GaussianNB, BernoulliNB ,MultinomialNB) <b> Gaussian Naive Byes classifier </b> have highest accuracy.
2. Parameters of BernoulliNB classifier can be adjusted to increase the accuracy and it can result in same accuracy as GaussianNB classifier.





