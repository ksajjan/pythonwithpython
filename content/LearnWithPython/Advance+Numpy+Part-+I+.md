title: Advance NumPy Part-I  
date: 2016-12-15
Tag: ['Numpy','Numpy']
description : NumPy stands for Numerical Python which provides a vast type of methods to deal with data. Some advance method used in Numpy are..
keywords : Advance NumPy, NumPy Broadcasting, array broadcasting, Numpy reshape(), NumPy newaxis(), C Versus Fortan Order Python, Python ravel() or flatten(),Concatenating and Splitting Arrays, array repetition, Broadcasting Rule 
author : Sajjan Kumar


NumPy stands for Numerical Python which is widely used for scientific calculation for its advance interface for array manipulation. From Broadcasting to other tools it became quite handy when one is dealing with large data set.
So let's start exploring Numpy features in this notebook with first importing numpy.

	import numpy as np
	from numpy.random import randn


You may occasionally have some data set(usually array) for which you need to check whether data set contains integers, floating point numbers, strings, or Python objects. For this <i> <b> np.issubdtype(array, datatype) </b> </i> is used. Let's code for this.




Define our test array

	arr1= np.ones(10, dtype= np.uint16)

	arr2= np.ones(10, dtype= np.float32)

	arr3= [1,2,3,4,5]
Now to Checking wheather a data set have a specific datatype using np.issubdtype() fucntion

	print np.issubdtype(arr1.dtype,np.integer)
	print np.issubdtype(arr2.dtype, np.integer)
	print np.issubdtype(arr2.dtype, np.floating)

Output:

    True
    False
    True
    

# Array Manipulation 
Numpy provide ease with Array Manipulation. Here are some handy feature of Numpy Array Manipulation.Let's First talk about Reshaping Array.

### Reshaping Arrays 
while using **.reshape()** function, we should keep in mind that overall shape of array shouldn't be changed. the input of this function is the dimension in which we want to convert the array.

First define sample array 

	arr3= np.arange(18)
	arr3

Output:

    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17])

Now Let's reshape it into [9,2] size.

	arr3.reshape((9,2))

Output:

    array([[ 0,  1],
           [ 2,  3],
           [ 4,  5],
           [ 6,  7],
           [ 8,  9],
           [10, 11],
           [12, 13],
           [14, 15],
           [16, 17]])


Let's change this into [2,9] size.

	arr3.reshape((2,9))

Output:

    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8],
           [ 9, 10, 11, 12, 13, 14, 15, 16, 17]])


Again Change the shape of array to a different size.

	arr3.reshape((3,6))

Output:

    array([[ 0,  1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10, 11],
           [12, 13, 14, 15, 16, 17]])



**One of the passed dimensions in .reshape() can be -1, in that case value used for that dimension will be taken from the data.**
See the example below

	arr4 = np.arange(30)
	arr4

Output:

    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])



Now Let's reshape using -1 as a dimension 

	arr4.reshape((5,-1)) 

here to complete the array size, in-place of -1 it should be 6 so reshape((5,-1)) will interrupt -1 as 6 and then proceed. 

Output: 



    array([[ 0,  1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10, 11],
           [12, 13, 14, 15, 16, 17],
           [18, 19, 20, 21, 22, 23],
           [24, 25, 26, 27, 28, 29]])


Check another example :


	arr4.reshape((3,-1)) 

Here to complete the array size their should be 10 instead of -1.

Output:




    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
           [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])

Next example:

	arr4.reshape((-1,2))

Output: 

    array([[ 0,  1],
           [ 2,  3],
           [ 4,  5],
           [ 6,  7],
           [ 8,  9],
           [10, 11],
           [12, 13],
           [14, 15],
           [16, 17],
           [18, 19],
           [20, 21],
           [22, 23],
           [24, 25],
           [26, 27],
           [28, 29]])



### Reshaping array with numpy.newaxis() method:
**newaxias()** is used to create a new axis(dimension) in the array to fit the broadcast rule.Check example below 


	array= randn(2,3)
	array.shape

Output:

    (2, 3)

Now let's create a new axis.

	array2= array[:,np.newaxis, :]
	array2.shape

Output:

    (2, 1, 3)


<b> Numpy </b> provide the opposite operation of reshape (i.e from higher dimension to one-dimensional). This is also known as flattening or raveling.
Their are two methods.

1. ravel() <br>
2. flatten() <br>
see the example below

	arr5= np.ones((5,3), dtype= np.uint16)
	arr5

Output:

    array([[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]], dtype=uint16)

Now 

	arr5.ravel()

Output:

    array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dtype=uint16)


For flatten()

	arr5.flatten()

Output:

    array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dtype=uint16)



ravel() does not produce a copy of data if it does not have to While, the flatten() method always return a copy of the data.

### C Versus Fortan Order

	arr4

Output:

    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])


With order F:

	arr4.reshape((3,10), order='F')

Output:

    array([[ 0,  3,  6,  9, 12, 15, 18, 21, 24, 27],
           [ 1,  4,  7, 10, 13, 16, 19, 22, 25, 28],
           [ 2,  5,  8, 11, 14, 17, 20, 23, 26, 29]])

when reshaping with order F, data is append column by column.

	arr4.reshape((3,10), order='C') # order 'C' is by default 

Output:

    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
           [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])


When reshaping with order C, data is append raw by raw.

The Key difference between C and Fortran order is the order in which the dimensions are traversed:

<b> C order </b> Traverse Higher dimensions first (i.e axis 1 before advancing on axis 0). [Raw major order]

<b> Fortan Order </b> Traverse Higher dimensions last(i.e axis 0 before advancing on axis 1) [ column major order]


### Concatenating and Splitting Arrays

Numpy provides 2 types of concatenation of arrays.First is along axis=0 and other is along axis=1.<br>
see the example below

	arr6= np.array([[1,2,3,4,5],[6,7,8,9,10]])
	arr6

Output:

    array([[ 1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10]])

Our second array:

	arr7= np.array([[11,12,13,14,15],[16,17,18,19,20]])
	arr7

Output:

    array([[11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20]])


Now Concatenation operation along axis=0 

	np.concatenate((arr6,arr7),axis=0)

Output:

    array([[ 1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20]])


Concatenation operation along axis=1

	np.concatenate((arr6,arr7), axis=1)

Output:

    array([[ 1,  2,  3,  4,  5, 11, 12, 13, 14, 15],
           [ 6,  7,  8,  9, 10, 16, 17, 18, 19, 20]])


Some other function :

	np.vstack((arr6,arr7)) # same as np.concatenate() with axis=0

Output:

    array([[ 1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20]])


Now

	np.hstack((arr6,arr7)) # same as np.cooncatenate() with axis=1

Output:

    array([[ 1,  2,  3,  4,  5, 11, 12, 13, 14, 15],
           [ 6,  7,  8,  9, 10, 16, 17, 18, 19, 20]])


**Now Splitting Operation:**

	arr8= randn(4,4)
	arr8

Output:

    array([[  7.08533211e-01,   4.59659578e-01,  -1.57881323e-01,
              1.07929958e+00],
           [ -3.86824405e-01,  -1.64399896e-01,   1.53551098e+00,
              1.15847583e+00],
           [  1.94122163e-01,  -7.44141600e-01,  -4.42922893e-01,
             -2.25669699e-01],
           [ -1.01093857e+00,  -5.21043404e-01,  -7.55925342e-04,
              1.55661573e-01]])



split() takes array as argument along with size of array to be splited or a array like object of the array size.


	arr_1= np.split(arr8,1)  #size of arr_1 is 1 which mean arr8 will be divided in one part.
	arr_1

Output:


    [array([[ 0.50454954,  0.65916656,  1.69246983,  0.86705127],
            [-0.71989673,  0.37454774, -0.32577363, -0.08872866],
            [ 0.65309926, -0.49518186, -0.73326777,  1.18062482],
            [ 0.9273575 , -1.40040011,  1.65876684, -0.65355634]])]


Split array in 2 parts:

	np.split(arr8,2) # the output array will be half-half of arr8

Output:

    [array([[ 0.50454954,  0.65916656,  1.69246983,  0.86705127],
            [-0.71989673,  0.37454774, -0.32577363, -0.08872866]]),
     array([[ 0.65309926, -0.49518186, -0.73326777,  1.18062482],
            [ 0.9273575 , -1.40040011,  1.65876684, -0.65355634]])]

Split array in 4 parts

	np.split(arr8,4)  #here if you give the input

Output:

    [array([[ 0.50454954,  0.65916656,  1.69246983,  0.86705127]]),
     array([[-0.71989673,  0.37454774, -0.32577363, -0.08872866]]),
     array([[ 0.65309926, -0.49518186, -0.73326777,  1.18062482]]),
     array([[ 0.9273575 , -1.40040011,  1.65876684, -0.65355634]])]


Here if you give the size of splitting array 3 instead of 4 then it would through an error <i> ValueError: array split does not result in an equal division </i>
<br>.

### Repeating Elemetns : Tile and Repeat

To Produce Larger arrays, repeat() and tile() functions are used. <br>
repeat replicates each element in an array some number of times, producing a larger array.


	arr9= np.arange(4)
	arr9

Output:

    array([0, 1, 2, 3])


Repeat every element 2 times

	arr9.repeat(2) 

Output:

    array([0, 0, 1, 1, 2, 2, 3, 3])

Now 

	arr9.repeat([2,3,5,6]) # repeat first element 2 times, second element 3 times , third element 5 times and fourth element 6 time

Output: 

    array([0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3])

For multidimensional Array

	arr10= randn(2,2)
	arr10

Output:

    array([[-0.31851426,  2.01991533],
           [-0.13367267,  1.00630383]])


Repeat element which is on axis=0

	arr10.repeat(2,axis=0) 

Output:

    array([[-0.31851426,  2.01991533],
           [-0.31851426,  2.01991533],
           [-0.13367267,  1.00630383],
           [-0.13367267,  1.00630383]])


Repeat element which is on axis=1

	arr10.repeat(2,axis=1)

Output:

    array([[-0.31851426, -0.31851426,  2.01991533,  2.01991533],
           [-0.13367267, -0.13367267,  1.00630383,  1.00630383]])


Similarly you can pass an array of integers when repeating a multidimensional array to repeat a given slice a different number of times:


	arr10.repeat([2,4],axis=0)  # which row to be repeated(2nd) and
	the no of times(4 time) the row to be repeated

Output:

    array([[ 1.1676876 ,  0.73187928],
           [ 1.1676876 ,  0.73187928],
           [ 1.19650763, -0.85104547],
           [ 1.19650763, -0.85104547],
           [ 1.19650763, -0.85104547],
           [ 1.19650763, -0.85104547]])



For Columns

	arr10.repeat([1,3],axis=1) # same for columns( 1st column repeated 3 times)

Output:

    array([[ 1.1676876 ,  0.73187928,  0.73187928,  0.73187928],
           [ 1.19650763, -0.85104547, -0.85104547, -0.85104547]])


Now 


	arr10.repeat([0,3], axis=1) #here it will repeat column=0
	and discard column 1 in output

Output:

    array([[ 0.73187928,  0.73187928,  0.73187928],
           [-0.85104547, -0.85104547, -0.85104547]])



<b> <i> tile </i> </b> on the other hand, is a shortcut for stacking copies of an array along an axis.


	arr10

Output:

    array([[ 1.1676876 ,  0.73187928],
           [ 1.19650763, -0.85104547]])

Now


	np.tile(arr10,2) # the second argument is the number of
	tiles ( a scalar or a tuple). When the second argument to tile is
	tuple it indicate the layout of the tiling.

Output:

    array([[ 1.1676876 ,  0.73187928,  1.1676876 ,  0.73187928],
           [ 1.19650763, -0.85104547,  1.19650763, -0.85104547]])



<b> The tiling is made row by row, rather than column by column. </b>



	np.tile(arr10,(2,2))  #row repeated 2 times, column repeated 2 times.

Output:

    array([[ 1.1676876 ,  0.73187928,  1.1676876 ,  0.73187928],
           [ 1.19650763, -0.85104547,  1.19650763, -0.85104547],
           [ 1.1676876 ,  0.73187928,  1.1676876 ,  0.73187928],
           [ 1.19650763, -0.85104547,  1.19650763, -0.85104547]])

another example:

	np.tile(arr10,(3,2)) # row repeated 3 times, column repeated 2 times.

Output:

    array([[ 1.1676876 ,  0.73187928,  1.1676876 ,  0.73187928],
           [ 1.19650763, -0.85104547,  1.19650763, -0.85104547],
           [ 1.1676876 ,  0.73187928,  1.1676876 ,  0.73187928],
           [ 1.19650763, -0.85104547,  1.19650763, -0.85104547],
           [ 1.1676876 ,  0.73187928,  1.1676876 ,  0.73187928],
           [ 1.19650763, -0.85104547,  1.19650763, -0.85104547]])



### Broadcasting
 
Broadcasting describes how arithmetic works between arrays of different shapes. It is a very powerful feature.

	arr3

Output:


    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17])



Simple broadcasting:

	arr3*6
 
Output:

    array([  0,   6,  12,  18,  24,  30,  36,  42,  48,  54,  60,  66,  72,
            78,  84,  90,  96, 102])



Here the scalar value 6 has been broadcast to all of other elements in the multiplication operation.

###### The Broadcasting Rule

Two arrays are compatible for broadcasting if for each trailing dimension, (that is, starting from the end ) the axis lengths match or if either of the lengths is 1. Broadcasting is then performed over the missing and / or length 1 dimensions.


	arr11= randn(2,3)
	arr11

Output:


    array([[ 0.15897943,  0.21914698,  1.16865214],
           [-0.1779596 , -1.55740588, -1.40536907]])


another numpy array
	arr12= randn(6,2)
	arr12

Output:

    array([[ 0.61632769,  1.43608023],
           [ 0.12357505, -0.70171185],
           [-0.32430931, -0.15066942],
           [-1.14900472, -0.24824113],
           [-1.25776788, -1.55733187],
           [-0.73411425,  0.76859758]])


Now try this

	arr11 + arr12

this will give ValueError: operands could not be broadcast together with shapes (2,3) (6,2)
so We have to reshape the arr11 before addition.
As according to Broadcasting rule to make addition along axis-1 the smaller array should have a shape of (6,1).

	print arr11.reshape(6,1)+ arr12 

Output:

    [[-0.52834331 -1.57587648]
     [-2.0897029  -1.69842965]
     [-0.56482399 -0.74702429]
     [-1.02085944 -0.45111874]
     [-0.86002779  0.90505302]
     [ 0.29465825  0.86799132]]
   
Check

	arr12 

Output:


    array([[ 0.61632769,  1.43608023],
           [ 0.12357505, -0.70171185],
           [-0.32430931, -0.15066942],
           [-1.14900472, -0.24824113],
           [-1.25776788, -1.55733187],
           [-0.73411425,  0.76859758]])


Check the mean along axis=0

	arr12.mean(0)

Output:

    array([-0.45421557, -0.07554607])

Subtraction in Broadcasting:

	arr12 - arr12.mean(0)

Output:

    array([[ 1.07054326,  1.51162631],
           [ 0.57779062, -0.62616578],
           [ 0.12990626, -0.07512334],
           [-0.69478915, -0.17269506],
           [-0.80355231, -1.48178579],
           [-0.27989868,  0.84414366]])


Boolean operation in Broadcasting:

	arr12[arr12 > 0]

Output:

    array([ 0.61632769,  1.43608023,  0.12357505,  0.76859758])

Check the mean along axis=1

	arr12.mean(1)

Output:

    array([ 1.02620396, -0.2890684 , -0.23748936, -0.69862292, -1.40754987,
            0.01724166])

Now Check this

	arr12 - arr12.mean(1)

By doing this will through a ValueError: operands could not be broadcast together with shapes (6,2) (6,)
because According to the rules, to subtract over axis 1 (that is, subtract the row mean from each row), the smaller array must have shape  (6, 1).

so Let's reshape the mean

	arr12 - arr12.mean(1).reshape(6,1)

Output:


    array([[-0.40987627,  0.40987627],
           [ 0.41264345, -0.41264345],
           [-0.08681994,  0.08681994],
           [-0.45038179,  0.45038179],
           [ 0.14978199, -0.14978199],
           [-0.75135592,  0.75135592]])



Note : for Broadcasting purpose, numpy.newaxis() method can be used.
 
To know more about Broadcasting below post will be helpful to read.
[http://scipy.github.io/old-wiki/pages/EricsBroadcastingDoc](http://scipy.github.io/old-wiki/pages/EricsBroadcastingDoc)

Got any improvement in this post, Hit Email me.