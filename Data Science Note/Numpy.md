# Numpy for Data Science


```python
import numpy as np
```

## Array Attribute

### 1-D Array :


```python
a = np.array([1,2,3,4,5])
a
```




    array([1, 2, 3, 4, 5])




```python
type(a) # numpy.ndarray --> n dimantion array
```




    numpy.ndarray




```python
a.ndim
```




    1




```python
a.shape       # 5 column , no rows
```




    (5,)



### 2-D Array :


```python
b = np.array([[1,2,3],
              [4,5,6]])
b
```




    array([[1, 2, 3],
           [4, 5, 6]])




```python
b.shape           # 2 rows , 3 column
```




    (2, 3)




```python
b.dtype           # dtype --> data type
```




    dtype('int64')




```python
b.size            # Total element
```




    6



### 3-D Array :


```python
c = np.array([[[1,2,3],
              [4,5,6],
              [7,8,9]],
              
            [[11,12,13],    # imagine that 1-9 in up of 10-18
             [14,15,16],
             [17,19,19]]])
c
```




    array([[[ 1,  2,  3],
            [ 4,  5,  6],
            [ 7,  8,  9]],
    
           [[11, 12, 13],
            [14, 15, 16],
            [17, 19, 19]]])



### Memory check :


```python
a.nbytes , b.nbytes , c.nbytes
```




    (40, 48, 144)



### Zeros & Ones :


```python
zeros_arr = np.zeros((3,3) , dtype=int)
zeros_arr
```




    array([[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]])




```python
ones_arr = np.ones((4,4) , dtype=int)
ones_arr
```




    array([[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]])



### Different values :


```python
arr_3 = np.full((4,4) , 12)
arr_3
```




    array([[12, 12, 12, 12],
           [12, 12, 12, 12],
           [12, 12, 12, 12],
           [12, 12, 12, 12]])



### Identity matrix ( I ) :


```python
i_3 = np.identity(3, dtype=int)
i_3
```




    array([[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]])



### Eye :


```python
eye = np.eye(3 , dtype=int)
eye
```




    array([[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]])




```python
eye = np.eye(4, dtype= int , k = 1)
eye           # k = 1 --> mail row will up by 1
```




    array([[0, 1, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1],
           [0, 0, 0, 0]])



### Arrange :


```python
arrange = np.arange(0,100,10)       # like a python range() function
arrange
```




    array([ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90])



### Linspace :


```python
linspace = np.linspace(1,100,20)      # (start , end , how many values)
linspace
```




    array([  1.        ,   6.21052632,  11.42105263,  16.63157895,
            21.84210526,  27.05263158,  32.26315789,  37.47368421,
            42.68421053,  47.89473684,  53.10526316,  58.31578947,
            63.52631579,  68.73684211,  73.94736842,  79.15789474,
            84.36842105,  89.57894737,  94.78947368, 100.        ])




```python
linspace = np.linspace(1,100,20 , dtype=int)      # (start , end , how many values)
linspace
```




    array([  1,   6,  11,  16,  21,  27,  32,  37,  42,  47,  53,  58,  63,
            68,  73,  79,  84,  89,  94, 100])



### Empty :


```python
empty = np.empty((1,5))
empty
```




    array([[4.67422725e-310, 0.00000000e+000, 4.67494390e-310,
            4.67494390e-310, 1.97626258e-323]])



## Array Indexing :

### Index :


```python
a = np.array([1,2,3,4,5,6,7])
a[0]            # as like normal indexing
```




    1



### Random array :


```python
random = np.random.randint(1,100 , size = (5,5))
random        # 1-100 random number 5x5 matrix
```




    array([[89, 28, 72,  1, 35],
           [52, 45, 99, 53, 35],
           [93,  6,  2, 31, 35],
           [ 7, 57, 80, 87, 33],
           [81, 96, 97, 48, 31]])



### Index access 2-D array :


```python
x = random[0][0]           # row 0 , culumn 0
x
```




    89




```python
y = random[0,0]           # rew 0 , culumn 0         
y
```




    89



### Index access 3-D array :


```python
random = np.random.randint(1,100 , size=(2,3,4))
random          # size(2,3,4) --> 3 : row  , 4 : column and 2 stage
```




    array([[[ 4, 78, 15, 48],
            [24, 49, 60, 83],
            [45, 64, 95, 54]],
    
           [[26, 60, 11, 75],
            [35, 96, 47, 22],
            [19, 40, 49,  6]]])




```python
x = random[0][0][0]
x
```




    4




```python
x = random[0,0,0]
x
```




    4



## Array Slicing :

### Slicing 1-D array :


```python
a = np.array([1,2,3,4,5,6,7,8,9])
a[1:4]
```




    array([2, 3, 4])




```python
a[:6]
```




    array([1, 2, 3, 4, 5, 6])




```python
a[2:]
```




    array([3, 4, 5, 6, 7, 8, 9])



### Slicing 2-D array :


```python
b = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
b[0:2 , 0:1]   # row , column
```




    array([[1],
           [4]])



## Manipulate array shape :


```python
# Total 5 way:
    # 1. reshape() 
    # 2. resize()
    # 3. revel()
    # 4. flatten()
    # 5. defining array shape
```

### 1. reshape() :


```python
b = np.array([[1, 2, 3] , 
              [4, 5, 6]])
np.reshape(b,(3,2))     # if element is not emough it will show element error
```




    array([[1, 2],
           [3, 4],
           [5, 6]])



### 2. resize() :


```python
# to solve this element error we can use resize()
b = np.array([[1, 2, 3] , 
              [4, 5, 6]])
np.resize(b, (4,3))   # repeat the element if extra need
```




    array([[1, 2, 3],
           [4, 5, 6],
           [1, 2, 3],
           [4, 5, 6]])



### 3. revel () :


```python
# change main array 
b = np.array([[1, 2, 3] , 
              [4, 5, 6]])
ravel = np.ravel(b)
ravel
```




    array([1, 2, 3, 4, 5, 6])




```python
ravel[0] = 100              # return a view of array and change main array 
ravel
```




    array([100,   2,   3,   4,   5,   6])



### 4. flatten() :


```python
# convart any array to 1-D array
# don't change main array
b = np.array([[1, 2, 3] , 
             [4, 5, 6]])
flatten = b.flatten()       # return a copy of arry and can't change main array
flatten
```




    array([1, 2, 3, 4, 5, 6])




```python
flatten[0] = 100            # change flatten only not b
b
```




    array([[1, 2, 3],
           [4, 5, 6]])



### 5. defining array shape :


```python
b = np.array([[1, 2, 3] , 
             [4, 5, 6]])
b.shape = (3, 2)            # need equal element
b
```




    array([[1, 2],
           [3, 4],
           [5, 6]])



## Array staking :

### hstake() :


```python
a = np.arange(1,10).reshape(3,3)    # create a 2-D array 1 to 9
b = 2*a                             # 2 * all element
b
```




    array([[ 2,  4,  6],
           [ 8, 10, 12],
           [14, 16, 18]])




```python
x = np.hstack((a,b))                # a + b in horizontal
x
```




    array([[ 1,  2,  3,  2,  4,  6],
           [ 4,  5,  6,  8, 10, 12],
           [ 7,  8,  9, 14, 16, 18]])



### vstake() :


```python
y = np.vstack((a,b))                # a + b in vartical 
y
```




    array([[ 1,  2,  3],
           [ 4,  5,  6],
           [ 7,  8,  9],
           [ 2,  4,  6],
           [ 8, 10, 12],
           [14, 16, 18]])



### column stake :


```python
z = np.column_stack((a , b))        # semilar to hstack
z
```




    array([[ 1,  2,  3,  2,  4,  6],
           [ 4,  5,  6,  8, 10, 12],
           [ 7,  8,  9, 14, 16, 18]])




```python
z = np.row_stack((a , b))           # semilar to vstack
z
```




    array([[ 1,  2,  3],
           [ 4,  5,  6],
           [ 7,  8,  9],
           [ 2,  4,  6],
           [ 8, 10, 12],
           [14, 16, 18]])



### concatinate :


```python
z = np.concatenate((a,b) , axis=1)  # axis 1 = horaizonal and azis 0 = vartical
z
```




    array([[ 1,  2,  3,  2,  4,  6],
           [ 4,  5,  6,  8, 10, 12],
           [ 7,  8,  9, 14, 16, 18]])


