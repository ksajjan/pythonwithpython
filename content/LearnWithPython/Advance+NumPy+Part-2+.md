title: Advance NumPy Part-II  
date: 2016-12-17
Tag: ['Numpy','Numpy']
description : NumPy stands for Numerical Python which provides a vast type of methods to deal with data. Some advance method used in Numpy are..
keywords : Advance NumPy, NumPy universal funcation, ufunc, custom ufunc in python, Sorting, advance sorting python, argsort(),reduceat(),outer(),accumulate(),reduce(), Broadcasting Rule 
author : Sajjan Kumar



This is the second post on Advance Numerical Python (NumPy). To read first part visit - <a href="http://sajjan.xyz/posts/Advance+Numpy+Part-+I+/index.html"> Advance Numpy Part-I </a> .<br>
In this post we will talk about ufunc methods, sorting and structured array.let's start by importing numpy.



	import numpy as np
	from numpy.random import randn


### Universal functions (ufunc):

From docs "A universal function (or ufunc for short) is a function that operates on ndarrays in an element-by-element fashion, supporting array broadcasting, type casting, and several other standard features. That is, a ufunc is a “vectorized” wrapper for a function that takes a fixed number of scalar inputs and produces a fixed number of scalar outputs.

In Numpy, universal functions are instances of the numpy.ufunc class"

### ufunc Instance Methods 

Their are few NumPy's binary ufuncs special methods for performing certain kinds of special vectorized operations. Some of them are: 

1. <i> **reduce()** </i><br>
 reduce takes a single array and aggregates its values, optionally along an axis, by performing a sequence of binary operation.<br>
 For example, an alternate way to sum elements in an array is to use <b> <i> np.add.reduce() </i> </b>



	arr= np.arange(20)
	arr

Output:

    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19])


Let's perform an addition:

	arr.sum()

Output:


    190

Check:


	np.add.reduce(arr)

Output:

    190



2.<b><i> accumulate() </i> </b> <br>
it produces an array of the same size with the intermediate accumulated values.


	np.add.accumulate(arr)

Output:

    array([  0,   1,   3,   6,  10,  15,  21,  28,  36,  45,  55,  66,  78,
            91, 105, 120, 136, 153, 171, 190])


another example:

	np.add.accumulate(arr1)

Output:

    array([0, 1, 3, 6])



3.<b><i> outer() </i> </b> <br>
it performs a pairwise cross-product between two arrays.



	arr1= np.arange(4)
	arr1

Output:

    array([0, 1, 2, 3])

So

	np.multiply.outer(arr,arr1) # you can try different value
	of second argument and see the difference in result.

Output:

    array([[ 0,  0,  0,  0],
           [ 0,  1,  2,  3],
           [ 0,  2,  4,  6],
           [ 0,  3,  6,  9],
           [ 0,  4,  8, 12],
           [ 0,  5, 10, 15],
           [ 0,  6, 12, 18],
           [ 0,  7, 14, 21],
           [ 0,  8, 16, 24],
           [ 0,  9, 18, 27],
           [ 0, 10, 20, 30],
           [ 0, 11, 22, 33],
           [ 0, 12, 24, 36],
           [ 0, 13, 26, 39],
           [ 0, 14, 28, 42],
           [ 0, 15, 30, 45],
           [ 0, 16, 32, 48],
           [ 0, 17, 34, 51],
           [ 0, 18, 36, 54],
           [ 0, 19, 38, 57]])



The output of <i> **outer** </i> will have a **dimension that is the sum of the dimensions of the input.**


	result= np.subtract.outer(randn(3,4), randn(4))
	print result.shape
	print result

Output:


    (3, 4, 4)
    [[[ -4.13051051e-01   1.04092440e+00   2.98847493e+00   3.27364074e-01]
      [ -1.17842508e-01   1.33613294e+00   3.28368348e+00   6.22572617e-01]
      [  6.09592054e-01   2.06356750e+00   4.01111804e+00   1.35000718e+00]
      [ -1.21598150e+00   2.37993946e-01   2.18554448e+00  -4.75566377e-01]]
    
     [[  4.15421397e-01   1.86939684e+00   3.81694738e+00   1.15583652e+00]
      [ -2.65594289e+00  -1.20196744e+00   7.45583097e-01  -1.91552776e+00]
      [ -2.91411002e+00  -1.46013457e+00   4.87415964e-01  -2.17369490e+00]
      [ -1.02671631e+00   4.27259137e-01   2.37480968e+00  -2.86301185e-01]]
    
     [[ -9.78589483e-01   4.75385964e-01   2.42293650e+00  -2.38174358e-01]
      [ -7.41275465e-01   7.12699982e-01   2.66025052e+00  -8.60340601e-04]
      [ -2.63662351e+00  -1.18264807e+00   7.64902472e-01  -1.89620839e+00]
      [ -1.75669451e+00  -3.02719064e-01   1.64483147e+00  -1.01627939e+00]]]
    

4.<b><i> reduceat() </i> </b> <br>
it performs a local reduce, in essence an array  groupby operation in which slices of the array are aggregated together.It accepts a sequence of “bin edges” which indicate how to split and aggregate the values:


	arr2= np.arange(12)
	arr2

Output:


    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

Now

	np.add.reduceat(arr2,[0,5,8])

Output:

    array([10, 18, 38])



The results are the reductions (here sums) performed over arr2[0:5], arr2[5:8] and arr2[8:].



	np.add.reduceat(arr2,[0,4,8,11])

Output:

    array([ 6, 22, 27, 11])



In this case, sums are performed over arr2[0:4], arr2[4:8], arr2[8:11] and arr2[11:].

### Custom ufuncs:
There are a couple of facilities for creating your own function. 
<b> <i> np.frompyfunc </i> </b> accepts a Python function along with a specification for the number of inputs and outputs. Let's see an example for this 


First define a function let's call it add_elem.

	def add_elem(x,y):
	    return x+y

let's feed our newly created function to np.frompyfunc

	add_arr= np.frompyfunc(add_elem,2,1)

Output:

    <ufunc 'add_elem (vectorized)'>

From docs (about numpy.frompyfunc ):

	numpy.frompyfunc(func, nin, nout) <br>
		Takes an arbitrary Python function and returns a Numpy ufunc.

	Parameters:	
    	func : Python function object

    	        An arbitrary Python function.

    	nin : int
	
    	        The number of input arguments.

    	nout : int

    	        The number of objects returned by func.



Now call our custom ufunc 

	add_arr(np.arange(8), randn(8))

Output:

    array([-0.6014613786566805, 1.894454043067947, 0.873415829705414,
           5.287178163549635, 4.665605872908261, 5.890771105067648,
           6.063906527348435, 4.756267572064051], dtype=object)

**(here notice dtype=object in the output)**

Functions created using Frompyfinc always return <b> arrays of Python objects</b> which isn't very convenient. So there is an alternate for this which is <b> <i> numpy.vectorize()</i> </b>, which is a bit more sophisticated about type inference. 

Define our function using np.vectorize :

	add_arr1= np.vectorize(add_elem, otypes=[np.float64])

Check our function:

	add_arr1(np.arange(8), randn(8)) #check the dtype in both output

Output:

    array([ 2.00642338,  0.96311945,  1.5726915 ,  3.95436983,  2.69372674,
            4.48954831,  7.71851384,  6.68381484])



<b> DrawBack of custom ufuncs </b> <br>
these are very slow because they require a Python Function call to compute each elements.

### Structured and Record Arrays

Until now the numpy array is a <i>homogeneous</i> data container. On the surface, this would appear to not allow you to represent heterogeneous or tabular-like data. <br>
A <i> structured <i> array is an ndarry in which each element can be thought of as representing a struct in C or row in a SQL table with multiple named fields.




	dtype= [('x', np.float64), ('y',np.int32)]

	arr3= np.array([(2.3,6),(3,-2)], dtype=dtype)
	print arr3

Output:

    array([(2.3, 6), (3.0, -2)], 
          dtype=[('x', '<f8'), ('y', '<i4')])



There are several ways to specify a structured dtype. One typical way is as a list of tuples with<i>(field_name, field_data_type)<i>. Now, the elements of the array are tuple-like objects whose elements can be accessed like a dictionary:



	print arr3[0]

Output:

    (2.3, 6)
    
Check:
	
	print arr3[0]['y']

Output:

    6
    
and,


	arr3[0]['x']

Output:


    2.2999999999999998



The field names are stored in the <i> dtype.names </i> attribute. On accessing a field on the structured array, a strided view on the data is returned.


For x:

	arr3['x']

Output:

    array([ 2.3,  3. ])


For y:

	arr3['y']

Output:

    array([ 6, -2])


<b> Nested dtypes and Multidimensional Fields </b>
When specifying a structured dtype, you can additionally pass a shape(as an int or tuple).


	dtype1= [('x', np.int32, 3), ('y', np.int32)]

	arr4= np.ones(4,dtype=dtype1)
	print arr4

Output:


    array([([1, 1, 1], 1), ([1, 1, 1], 1), ([1, 1, 1], 1), ([1, 1, 1], 1)], 
          dtype=[('x', '<i4', (3,)), ('y', '<i4')])



**<i> In this case, the x field now refers to an array of length three for each record. and field y refers to an array of length 1 or a single integer</i>**


	arr4[0]

Output:

    ([1, 1, 1], 1)


Check:


	arr4[0]['x']

Output:

    array([1, 1, 1])

Check:

	arr4[0]['y']

Output:


    1


	arr4['x']

Output:

    array([[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]])



Check:

	arr4['y']

Output:

    array([1, 1, 1, 1])



### Sorting
Basically sorting can be done with two types:
1. Python's built-in sort() method- it is an <i>in-plcae</i> sort, means that the array contents are rearranged without producing a new array
2. numpy.sort() method- it create a new, sorted copy of an array. <br>
Lets see example of both


	arr5= randn(5)
	arr5

Output:


    array([ 1.56312324, -1.2984947 ,  2.15808092,  0.09181684,  0.44818238])


Buit-in Sort()


	print arr5.sort() # we have to call the array to print the sorted values
	print arr5	

Output:

    None
    [-1.2984947   0.09181684  0.44818238  1.56312324  2.15808092]
    


**Sorting in multidimensional array**

	arr6= randn(3,4)
	arr6

Output:

    array([[ 0.35860128, -0.8384423 , -1.6795786 ,  0.31239183],
           [ 0.41454569,  0.03815681, -0.57127612, -0.28904015],
           [-0.48835359,  0.58665824, -0.61388025, -0.84957973]])


Sorting only columns:

	arr6[:,0].sort() # sort first column values in-place 
	arr6

Output:

    array([[-0.48835359, -0.8384423 , -1.6795786 ,  0.31239183],
           [ 0.35860128,  0.03815681, -0.57127612, -0.28904015],
           [ 0.41454569,  0.58665824, -0.61388025, -0.84957973]])

Raw-sorting:

	arr6[0,:].sort() # sort first row values in-place
	arr6

Output:

    array([[-1.6795786 , -0.8384423 , -0.48835359,  0.31239183],
           [ 0.35860128,  0.03815681, -0.57127612, -0.28904015],
           [ 0.41454569,  0.58665824, -0.61388025, -0.84957973]])



Check:

	arr7= randn(5)
	arr7

Output:

    array([ 2.14457701,  0.63477678,  0.59464752,  2.42914111, -0.46264067])

Numpy Sorting

	np.sort(arr7)
	
Output:

    array([-0.46264067,  0.59464752,  0.63477678,  2.14457701,  2.42914111])

Here we don't have to call the array specifically np.sort() created a new array with sorted value and that is returned.



Multidimensional array Sorting with numpy.sort

	arr8= randn(2,4)
	arr8

Output:

    array([[ 0.12966096,  0.10096747,  0.53117391, -0.92888992],
           [-0.00552033,  0.85259994,  0.40965244, -0.35089807]])

Now:


	np.sort(arr8,axis=0) # sorting is done along the axis=0 (column wise)

Output:

    array([[-0.00552033,  0.10096747,  0.40965244, -0.92888992],
           [ 0.12966096,  0.85259994,  0.53117391, -0.35089807]])


Sorting along axis=1


	np.sort(arr8, axis=1) #sorting is done along axis 1 (row wise)

Output:

    array([[-0.92888992,  0.10096747,  0.12966096,  0.53117391],
           [-0.35089807, -0.00552033,  0.40965244,  0.85259994]])


To sorting in <b> Descending order </b> the trick for a list values , values[::-1] return a list in reverse order. The same is true for ndarrays.



	arr8.sort(axis=1) # first sorting a list
	arr8

Output:


    array([[-0.92888992,  0.10096747,  0.12966096,  0.53117391],
           [-0.35089807, -0.00552033,  0.40965244,  0.85259994]])


Now Sorting in **descending order**

	arr8[:, ::-1] 

Output:



    array([[ 0.53117391,  0.12966096,  0.10096747, -0.92888992],
           [ 0.85259994,  0.40965244, -0.00552033, -0.35089807]])



### Sorting with argsort() and lexsort()

argsort() :
it return an array of index (let's called indexer) in which order the original array can be sorted.


	arr9= randn(5)
	arr9

Output:

    array([ 1.45852206,  1.89598304,  0.28001503, -1.01477851,  1.32962551])



argsort() sorting:

	indexer= arr9.argsort()
	indexer

Output:

    array([3, 2, 4, 0, 1])


Here it tells the index of data which will be placed in sorted array. <br>
let's say 

arr10= np.sort(arr9)


	arr10= np.sort(arr9)
	arr10

Output:


    array([-1.01477851,  0.28001503,  1.32962551,  1.45852206,  1.89598304])


so first value in arr10 (sorted arr9) is -1.4577 which is on 0th index, second value is -1.0486 which is on 4th index in arr9 and so on.<br>
so that indexer tells us about the sorting order in which the data will sorted.

<b> <i>lexsort() </i> </b> is similar to argsort, but it performs an indirect <i>lexicographical </i> sort on multiple key arrays.

<b> Alternate Sort Algorithms </b> :
various stable sorting alogrithm can be used with a 
<i> (kind= " mergesort ") argument </i>

### Finding elements in a Sorted Array:-
<b> <i>numpy.searchsorted() </i> </b> is used to performs a binary search, returning the location in the array where the value would need to be inserted to maintain sorting.



	arr11= np.array([0,1,22,4,42,33,64])
	arr11

Output:

    array([ 0,  1, 22,  4, 42, 33, 64])


Check:

	arr11.searchsorted(33)

Output:

    4

So 33 will be on 4th place in sorted array. let's check where 41 would fit.


	arr11.searchsorted(41)

Output:

    6

so in sorted array 41 would be 6th place.

### Performance Tips
Getting good performance out of code utilizing NumPy is often straightforward, as
array operations typically replace otherwise comparatively extremely slow pure Python
loops. Here is a brief list of some of the things to keep in mind: <br>
• Convert Python loops and conditional logic to array operations and boolean array
operations <br>
• Use broadcasting whenever possible <br>
• Avoid copying data using array views (slicing) <br>
• Utilize ufuncs and ufunc methods<br>


More ufunc function can be checked here:
[https://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs](https://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs)


Time to time as I learn more about Numpy I will update this post. Got anything in mind about this post Hit "Email me".
Thanks for Reading.
