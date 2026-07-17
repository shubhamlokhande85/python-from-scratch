'C.Array in NumPy'
'''
-In numpy an array is a collection of elements stored in a structured from for fast 
mathematical operations
-In numpy np.array() is used to creates an array (ndarray) from python list , tuple 
or other sequences
-A NumPy array is designed to store same type of data (homogeneous) for efficiency
-Means 
    - tuple only tuple 
    - list only list
    - set only set 
-Array is commonly used for numerical operations for mathematical operations 
 
:Various number type in array
Type	Type Code	Example
Integer	    'i'	     array('i', [1, 2, 3])
Float	    'f'	     array('f', [1.5, 2.5, 3.5])
Double	    'd'	     array('d', [1.2, 2.3])
Character	'u'	     array('u', ['a', 'b', 'c'])
 
''' 

#eg
from array import array
arr = array('i', [10,20,30,40])
print(type(arr))
#<class 'array.array'>

'C.1.Array attributes '
'''
-array attributes used to get information about an array.'
1)arr.ndim   # Number of dimensions
2)arr.shape  # Shape of the array
3)arr.size   # Total number of elements
'''
'C.1.1) .ndim '
'It return number of dimensions that array contained'
import numpy as np 
arr =np.array([[1,2,3,4,5],
               [6,7,8,9,10]])
print(arr.ndim)
# 2 

'C.1.2  .shape'
'It shows shape of a array '
print(arr.shape)
#(2, 5)  
# (row , columns)

'C.1.3 .size'
'it show how many elements that array contained'
print(arr.size)
#10

'C.2.Array mainpulation'
'''
| Operation        | Function                                |
| ---------------- | --------------------------------------- |
| Reshape          | `reshape()`                             |
| Flatten          | `flatten()`, `ravel()`                  |
| Transpose        | `.T`, `transpose()`                     |
| Join arrays      | `concatenate()`, `vstack()`, `hstack()` |
| Split arrays     | `split()`, `array_split()`              |
| Insert           | `insert()`                              |
| Delete           | `delete()`                              |
| Append           | `append()`                              |
| Repeat           | `repeat()`                              |
| Tile             | `tile()`                                |
| Sort             | `sort()`                                |
| Reverse          | `[::-1]`                                |
| Boolean indexing | `arr[arr > x]`                          |
| Fancy indexing   | `arr[[i, j]]`                           |

'''

'''
C.2.1.Creating Array
   1. 1D array
   2. 2D array 
   3. 3D array
'''
'1D array'
#eg 
import numpy as np
arr2 =array('i',[1,2,3,4])  # normal method to defined array
arr3 =np.array([1,2,3,4,5]) # array defined using numpy library
print(arr2)
#array('i', [1, 2, 3, 4])
print(arr3)
#[1 2 3 4 5]

'2D Array'
arr4=np.array([[1,2],[3,4],[5,6]])
print(arr4)
# [[1 2]
#  [3 4]
#  [5 6]]

'3D Array'
arr5=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
print(arr5)
#  [[[ 1  2  3]
#   [ 4  5  6]]

#  [[ 7  8  9]
#   [10 11 12]]

#  [[13 14 15]
#   [16 17 18]]]

'C.2.2 reshape()'
'It Change the shape without changing the data'
#eg 01
arr6  =np.array([[1,2,3],
                 [4,5,6]])
print(arr6.reshape(3,2))
# [[1 2]
#  [3 4]
#  [5 6]]

#eg 02 

arr7=np.arange(9)   
print(arr7)
#[0 1  2  3  4  5  6  7  8 ]
print(arr7.reshape(3,3))
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

'C.2.3 Flatten()'
'It converts mutliple dimensional array into 1 dimensional array'
arr8=np.array([[[1,2,3],
                [4,5,6]],
               [[7,8,9],
                [10,11,12]]])
print(arr8.ndim) # used to know dimentions of array
# 3 
print(arr8.flatten())
#[ 1  2  3  4  5  6  7  8  9 10 11 12] 
print(arr.ravel())   # Returns a view when possible
#[ 1  2  3  4  5  6  7  8  9 10]


'C.2.4 Transpose array'
'Swaps raws and columns'
#eg 01 
arr9=np.array([[1,2],
               [3,4]])
print(arr9)
# [[1 2]
#  [3 4]]
print(arr9.T)
# [[1 3]
#  [2 4]]

'C.2.5 Changing dimensions'
'''
-Adds new axis
-When you use np.newaxis, you're creating either the row axis or the column axis 
depending on where you insert it.

Code	                Shape	Result         For
arr10[:, np.newaxis]	(3,1)	Column vector  Column axis
arr10[np.newaxis, :]	(1,3)	Row vector     Row axis
'''
#eg 
arr10=np.array([1,2,3])
print(arr10.ndim)# 1 
print(arr10[:,np.newaxis])  #  it creates temporary 2D view not permantnent changes in original array 
# [[1]
#  [2]
#  [3]]
print(arr10.ndim)# 1 
'''here 
arr10[:,np.newaxis] == array[ existing dimension , new dimension ] 
where,
:          →  Take all elements from the existing dimension
np.newaxis →  Add a new dimension after it '''

'C.2.6 Joining array'

'1.np.concatenate()'
'-Its concat arrays in single array'
#eg
arr11 = np.array([1,2,3,4,5])
arr12 = np.array([6,7,8,9,10])
print(np.concatenate((arr11,arr12)))  # here array's passed as one collection using tuple like one argument'''
#[ 1  2  3  4  5  6  7  8  9 10]

'''here 
-NumPy receives one collection of arrays and joins them
-it means the function expects one argument that contains multiple arrays, not multiple separate array arguments
-When a NumPy function says it needs multiple arrays, 
it often wants them wrapped inside a container (tuple is container)
-so instead passing like this print(np.concatenate(arr11,arr12)) we pass print(np.concatenate((arr11,arr12))) 
                                                    |      |                                         |
                                                    1st    2nd arguments                            single argumnet (tuple)
'''
'2.np.stack()'
'np.stack() is a NumPy function used to join (combine) multiple arrays by creating a new axis (dimension)'
#eg 
arr13= np.array([1,2,3])
arr14= np.array([4,5,6])
stk =np.stack((arr13,arr14))
print(stk)
# [[1 2 3]
#  [4 5 6]]
print(stk.shape)
# (2, 3)

'3.np.vstack()'
'np.vstack() means vertical stack. It joins arrays vertically (row-wise) by placing one array below another'
#eg
arr15=np.array([[1,2],
                [3,4]])
arr16=np.array([[5,6],
                [7,8]])
vstk=np.vstack((arr15,arr16))
print(vstk)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
print(vstk.shape)
#(4, 2)

'4.hstack()'
'np.hstack() means horizontal stack. It joins arrays horizontally (column-wise), meaning it places arrays side by side---'
# eg 
arr17=np.array([[1,2,3],
                [4,5,6]])
arr18=np.array([[7,8,9],
                [10,11,12]])
hstk=np.vstack((arr17,arr18))
print(hstk)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
print(hstk.shape)
# (4, 3)

'C.2.7 Split array'

'''In NumPy, you can split arrays using functions like np.split(), np.array_split(), 
np.hsplit(), np.vsplit(), and np.dsplit()
- 
| Function           | Purpose                 |
| ------------------ | ----------------------- |
| `np.split()`       | Equal splits only       |
| `np.array_split()` | Unequal splits allowed  |
| `np.hsplit()`      | Split columns           |
| `np.vsplit()`      | Split rows              |
| `np.dsplit()`      | Split depth (3D arrays) |

'''
'1.np.split()'
'In numpy this functions split arrays eqaully if element not in equal numbers it raise ValueError '
#eg
arr19=np.array([1,2,3,4,5,6])
sp=np.split(arr19,3)
print(sp)
#[array([1, 2]), array([3, 4]), array([5, 6])]

'2.np.array_split()'
'Unlike np.split(), it works even if the array cannot be divided equally '

arr20=np.array([1,2,3,4,5,6,7])
sp2=np.array_split(arr20,3)
print(sp2)
#[array([1, 2, 3]), array([4, 5]), array([6, 7])]

'3.np.hsplit()'
'''
-np.hsplit() is used to split an array horizontally, 
meaning it splits along the columns (axis=1) for 2D arrays
-syntax 
numpy.hsplit(ary, indices_or_sections) 
where,
ary → Input array
indices_or_sections → Number of equal columns splits or positions where splitting occurs
'''
#eg 
arr21=np.array([[1,2,3,4],
                [5,6,7,8]])
sp3=np.hsplit(arr21,2)
print(sp3)
# [array([[1, 2],
#        [5, 6]]),
#  array([[3, 4],
#        [7, 8]])]

'4.np.vsplit()'
'''
-np.vsplit() is used to split an array vertically,
meaning it splits along the rows (axis=0) for 2D arrays
-syntax
numpy.vsplit(ary, indices_or_sections)
where,
ary → Input array
indices_or_sections → Number of equal row splits or positions where splitting occurs

'''
arr22=np.array([[1,2,3],
                [4,5,6],
                [7,8,9],
                [10,11,12]])
sp4=np.vsplit(arr22,2)
print(sp4)
# [array([[1, 2, 3],
#        [4, 5, 6]]), 
#  array([[ 7,  8,  9],
#        [10, 11, 12]])]


'5.np.dsplit()'
'''
-np.dsplit() is used to split an array depth-wise, 
meaning it splits along the third axis (axis=2) of a 3D array
-syntax
numpy.dsplit(ary, indices_or_sections)
-where 
ary → Input 3D array
indices_or_sections → Number of equal depth splits or positions where splitting occurs
'''
#eg  - 3D
print(np.arange(16))
#[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]

arr23 =np.arange(16).reshape(2,2,4)
# np.arange(n).reshape(a, b, c)  
# where
# a First dimension = 2
# b Second dimension = 2
# c Third dimension = 4
print(arr23)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]]

#  [[ 8  9 10 11]
#   [12 13 14 15]]]

arr24=np.dsplit(arr23,2)
print(arr24)
# [array([[[ 0,  1],
#         [ 4,  5]],

#        [[ 8,  9],
#         [12, 13]]]), 
#  array([[[ 2,  3],
#         [ 6,  7]],

#        [[10, 11],
#         [14, 15]]])]

'remain methods are included in next S45 session '