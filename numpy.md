# Numpy for Data Science

**Import Numpy :**
```py
import numpy as np
```

## Array Attribute :
**1-D Array :**
```py
type(a)             # numpy ndarray ---> numpy n dimantion array
a.shape             # (5, )     ---> 5 coloms
a.ndim
print(a.ndim)       # 1 ---> 1 dimantion array
```

**2-D Array :**
```py
b = np.array([[1, 2, 3,] , 
              [4, 5, 6]])
b.shape         # (2 , 3) ---> 2 row and 3 comomn
b.dtype         # int64 ---> data type
b.size          # size = 6 ---> total element
```

**3-D Array :**
```py
c = np.array([[[1, 2, 3],       # 3-D array
               [4, 5, 6],       # imagize thant 1-9 is up of 10 to 18
               [7, 8, 9]],
             
             [[10, 11, 12],
              [13, 14, 15],
              [16, 17, 18]]])
```

**Memory Check :**
```py
a.nbytes , b.nbytes , c.nbytes         # memory chekck
```

## Array Indexing :

```py
array1 = np.array([1, 2, 3, 4] , dtype=float)       # dtype ---> data type
```

**Zeros :**
```py
zero_arr = np.zeros((3,3) , dtype=int)      # make all 0 and data type is int
ones_arr = np.ones((3,3) , dtype=int)       # make all 1 and data type is int
```

**Different Values :**
```py
arr2 = np.full((3,3) , 10)                  # create 3 row , 3 colomn array with all 10 value
```

**Identity Metrix (I) :**
```py
I3 = np.identity(3, dtype=int)              # identity matrix
```

**Eye :**
```py
eye = np.eye(3, dtype=int , k=1)            # main row will up by 1
```

**Arrange :**
```py
arr4 = np.arange(0, 100 , 10)               # like a range function
```

**Linspace :**
```py
linspace = np.linspace(1, 100 , 50 , dtype=int)         # start , end , how many values
```

**Empty :**
```py
empty = np.empty((1, 5))                    # Create a emplty array
```

## Array indexing :
**Indexing :**
```py
a = np.array([1, 2, 3, 4, 5])
a[0]        # 1 --> as like normal indexing
```

**Random Array :**
```py
random = np.random.randint(1, 100 , size=(3,3))     # 1 to 100 values
                                                    # size 3 row and 3 colomn
```

**Index access 2-D arrays :**
```py
x = random[0][0]            # [0][0] --> row 0 and colomn 0
x = random[0,0]             # [0 ,0] --> row 0 and colomn 0 (Both are same)
```

**Index access 3-D arrays :**
```py
random = np.random.randint(1, 100 , size=(2, 3, 3))  
y = random[0 , 1 , 1]
y = random[0], [1] , [1]            
```

## Array Slicing :
**Slicing 1-D arrays :**
```py
a = np.array([1, 2, 3, 4, 5])
x = a[1:4]          # index 1 - 4
x = a[:4]           # index start - 4
x = a[2:]           # index 2 - end
```

**Slicing 2-D arrays :**
```py
b = np.array([[1, 2, 3] , 
              [4, 5, 6] ,
              [7, 8, 9]])
x = b[0:2 , 0:1]        # [0:2] --> row and [0:1] --> colomn
```

## Manipulate array shape :
```py
# Total 5 way:
    # 1. reshape() 
    # 2. resize()
    # 3. revel()
    # 4. flatten()
    # 5. defining array shape
```

**1. reshape() :**
```py
b = np.array([[1, 2, 3] , 
              [4, 5, 6]])
x = np.reshape(b ,(3,2))        # x will be create with 3 row and 2 colomn
# y = np.reshape(b ,(3,3))      # element error --> not enough element   
```

**2. resize() :**
```py
# to solve this element error we can use resize()
b = np.array([[1, 2, 3] , 
              [4, 5, 6]])
x = np.resize(b ,(4,3))         # repeat this element for if extra need
```
**3. revel() :**
```py
# convert any array to 1-D array
# change main array 
b = np.array([[1, 2, 3] , 
              [4, 5, 6]])
ravel = np.ravel(b)         # x = [1 2 3 4 5 6]
ravel[0] = 100              # return a view of array and change main array 
```

**4. flatten() :**
```py
# convart any array to 1-D array
# don't change main array
b = np.array([[1, 2, 3] , 
             [4, 5, 6]])
flatten = b.flatten()       # return a copy of arry and can't change main array
flatten[0] = 100            # change flatten only not b
```

**5. defining array shape :**
```py
b = np.array([[1, 2, 3] , 
             [4, 5, 6]])
b.shape = (3, 2)            # need equal element
```

## Array staking :
**hstack() and vstack() :**
```py
a = np.arange(1,10).reshape(3,3)    # create a 2-D array 1 to 9
b = 2*a                             # 2 * all element
x = np.hstack((a,b))                # a + b in horizontal
y = np.vstack((a,b))                # a + b in vartical 
```

**Column stack :**
```py
z = np.column_stack((a , b))        # semilar to hstack
z = np.row_stack((a , b))           # semilar to vstack
```

**Concatinate :**
```py
z = np.concatenate((a,b) , axis=1)  # axis 1 = horaizonal and azis 0 = vartical
```


