>`Numpy` is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays.

## Arrays

A numpy array is a grid of values. It's all the same type.

It's indexed by a tuple of non-negative integers.

### Create numpy array

#### `np.array()`

```python
import numpy as np

a = np.array([1, 2, 3])

print(a[1])     // output 2
```

#### `np.arrange()`

1 param for end
```python
>>> np.arange(3)
array([0, 1, 2])
```

2 param for range
```python
>>> np.arange(2, 8)
array([2, 3, 4, 5, 6, 7])
```

3 param for range and distance
```python
>>> np.arange(1, 6, 1.5)
array([1. , 2.5, 4. , 5.5])
```
##### `np.arrange()` vs `np.linspace `

```python
# np.arrange allows you to define the stepsize 
>>> np.arange(0, 1, 0.1) #--> 0.1 is the stepsize or interval 
>>> array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
# np.linspace allows you to define how many values you get including the specified min and max value 

>>> np.linspace(0, 1, 11) #--> 11 no of values you need 
>>> array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. ])
```

### Access the array element
2 ways to access the element:
```python
arr = array([[0, 0, 0],
	       [2, 2, 2],
	       [4, 4, 4]])

arr[2][2] # gets 4
arr[2, 2] # gets 4
```

### Array shape

1 rank array
```python
a = np.array([1, 2, 3])

a.shape     // (3,)
```

2 rank array
```python
b = np.array([   [1, 2, 3],
                 [7, 8, 9]   ] )

b.shape    
# (2, 3)
```

### Reshape array  `np.reshape()`

```python
>>> x = np.arange(6)
>>> x = x.reshape((2, 3))
>>> x
array([[0, 1, 2],
       [3, 4, 5]])
```

## Common methods

### `np.ravel()`
>Return a contiguous flattened array 
```python
>>> x = np.array([[1, 2, 3], [4, 5, 6]])
>>> np.ravel(x)
array([1, 2, 3, 4, 5, 6])
```


### `np.meshgrid(x, y)`

![](images/numpy_meshgrid.png)

[stackoverflow ](https://stackoverflow.com/a/36014586)

>The purpose of `meshgrid` is to create a rectangular grid out of an array of x values and an array of y values.

Create a array like:
```python
x =   0 1 2 3 4        y =   0 0 0 0 0
      0 1 2 3 4              1 1 1 1 1
      0 1 2 3 4              2 2 2 2 2
      0 1 2 3 4              3 3 3 3 3
      0 1 2 3 4              4 4 4 4 4

# to code
x[0,0] = 0    y[0,0] = 0
x[0,1] = 1    y[0,1] = 0
x[0,2] = 2    y[0,2] = 0
x[0,3] = 3    y[0,3] = 0
x[0,4] = 4    y[0,4] = 0
x[1,0] = 0    y[1,0] = 1
x[1,1] = 1    y[1,1] = 1
...
x[4,3] = 3    y[4,3] = 4
x[4,4] = 4    y[4,4] = 4
```
But with `meshgrid()` it's easier
```python
xvalues = np.array([0, 1, 2, 3, 4])
yvalues = np.array([0, 1, 2, 3, 4])

>>> xx, yy = np.meshgrid(xvalues, yvalues)
>>> xx
array([[0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4]])
>>> yy
array([[0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1],
       [2, 2, 2, 2, 2],
       [3, 3, 3, 3, 3],
       [4, 4, 4, 4, 4]])
>>> 
```
### `np.linspace()`

>It creates a evenly spaced values within a defined interval.

```python
np.linspace(start = 0, stop = 100, num =5)
```

It will produce 5 intervals of : [0, 25, 50, 75, 100]

### `np.reshape()`
>Return an array of zeros with the same shape and type as a given array.

```python
>>> x = np.arange(6)
>>> x = x.reshape((2, 3))
>>> x
array([[0, 1, 2],
       [3, 4, 5]])
>>> np.zeros_like(x)
array([[0, 0, 0],
       [0, 0, 0]])


>>> y = np.arange(3, dtype=float)
>>> y
array([0., 1., 2.])
>>> np.zeros_like(y)
array([0.,  0.,  0.])
```