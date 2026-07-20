'Random Module'
'''
-In NumPy random module used to generate random numbers 
-It allow you to generate number for simulations, testing , machine learning
more '''

import numpy as np
'Types of Random module'

'1.rand()'
'''
-we use np.random.rand() in numpy to generate random floating point between
0 to 1
-syntax
| Array Type               | `rand()` Syntax                     | Meaning                                                                              |
| ------------------------ | ----------------------------------- | ------------------------------------------------------------------------------------ |
| Single value (0D/scalar) | `np.random.rand()`                  | Returns one random float between `0.0` and `1.0`.                                    |
| 1D                       | `np.random.rand(n)`                 | `n` = number of elements.                                                            |
| 2D                       | `np.random.rand(rows, cols)`        | `rows` = number of rows, `cols` = number of columns.                                 |
| 3D                       | `np.random.rand(depth, rows, cols)` | `depth` = number of 2D matrices, `rows` = rows per matrix, `cols` = columns per row. |
'''
#eg 01 single scalar with single floating number generation
flo_num=np.random.rand()
print(flo_num)
#0.6908476280117011
#0.3612773842407242

#eg 02 1D dimentional array with mutliple floating number generation 
flo_num1D=np.random.rand(5)
print(flo_num1D)
#[0.88492262 0.88608031 0.13809073 0.42968457 0.41088392]

#eg 02 2D dimentional array with multiple floating number generation 
flo_num2D=np.random.rand(3,3)
print(flo_num2D)
# [[0.85141439 0.15995541 0.62755571]
#  [0.3186341  0.54135243 0.80922227]
#  [0.02015841 0.88925841 0.19254272]]

#eg 03 3D dimentional array with multiple floating number generation 
flo_num3D=np.random.rand(3,3,3)
print(flo_num3D)
# [[[0.99368789 0.75090594 0.52901553]
#   [0.80028434 0.97373932 0.77481346]
#   [0.79158395 0.28366201 0.70476209]]

#  [[0.17006699 0.44279017 0.20679976]
#   [0.24018418 0.72440359 0.34359448]
#   [0.17328096 0.30366978 0.45590926]]

#  [[0.30451459 0.59328857 0.11414443]
#   [0.19982958 0.81868364 0.40584608]
#   [0.24480046 0.2799205  0.89889355]]]


'2.Randint()'
'''
-We use np.random.radiant() in numpy to generate random intergers within 
a specific range
-syntax 
| Array Type               | `randint()` Syntax                                       | Meaning                        |
| ------------------------ | -------------------------------------------------------- | ------------------------------ |
| Single value (0D/scalar) | `np.random.randint(low, high)`                           | One random integer.            |
| 1D                       | `np.random.randint(low, high, size=n)`                   | `n` = number of elements.      |
| 2D                       | `np.random.randint(low, high, size=(rows, cols))`        | Creates a `rows × cols` array. |
| 3D                       | `np.random.randint(low, high, size=(depth, rows, cols))` | Creates a 3D array.            |
'''
#eg 01 generating random integer number
'np.random.randint(low, high)'
int_random1=np.random.randint(10) 
print(int_random1)
#10

int_random2=np.random.randint(1,11) 
print(int_random2)
#8

#eg 02 1D dimentional array with multiple integer number generation 
int_1D=np.random.randint(1,100,size=(5))  # size = (row ,column)
print(int_1D)
#[85 15  3 60 48]

#eg 03 2D dimentional array with multiple integer number generation
int_2D=np.random.randint(1,100,size=(3,4))
print(int_2D)
# [[38 85  5 81]
#  [65 90 68 47]
#  [66 62 43 91]]

#eg 04 3D dimentional array with multiple  integer number generation
int_3D=np.random.randint(1,100,size=(3,3,3))
print(int_3D)
# [[[88 42 85]
#   [88 62 18]
#   [29 25 77]]

#  [[ 1 37  8]
#   [47 54 71]
#   [92 87 98]]

#  [[66  5 98]
#   [ 9 99 66]
#   [57 32 74]]]



'3.randn()'
'''
-we use np.random.randn() generate random numbers from a standard normal distribution 

'normal distribution or Guassian distribution
--a normal distribution is a symmetric probability distribution in which the left and right 
sides of are mirror images of each other around the mean with most values clustered near the 
centre and fewer values occuring far their way 
--Diagram 
-bell shape

          * - mean= 0
       *     * -std=1 
     *         *
   *             *
 *                 *
----------------------  Number line 
          0                
-in numpy  
mean = 0
standard deviation = 1 

Note:
Most numbers are close to 0.
Some are around 1 or -1.
Very few are as large as 3 or -3.

The 68–95–99.7 Rule
For a normal distribution:
About 68% of values lie within 1 standard deviation of the mean.
About 95% lie within 2 standard deviations.
About 99.7% lie within 3 standard deviations.

-syntax 
| Dimension     | Syntax                               | Example                  | Shape     |
| ------------- | ------------------------------------ | ------------------------ | --------- |
| Single number | `np.random.randn()`                  | `0.45`                   | `()`      |
| 1D array      | `np.random.randn(n)`                 | `np.random.randn(10)`    | `(10,)`   |
| 2D array      | `np.random.randn(rows, cols)`        | `np.random.randn(3,4)`   | `(3,4)`   |
| 3D array      | `np.random.randn(depth, rows, cols)` | `np.random.randn(2,3,4)` | `(2,3,4)` |

 
'''
# eg 01 generating single random number from normal (Gaussian) distribution
nd_rand=np.random.randn()
print(nd_rand) 
#-1.4834409184165038

#eg 02 creating 1D array from random number that belong normal distribution 
nd_rand1D=np.random.randn(5)
print(nd_rand1D)
# [ 0.2075782   0.36471317 -0.41938588  0.00827499 -1.02390681]

#eg 03 creating 2D array from random number that belong normal distribution
nd_rand2D=np.random.randn(3,4)
print(nd_rand2D)
# [[-1.21658999  0.66653297 -0.24590471 -1.58492673]
#  [ 0.22795432 -0.30581604 -1.66883442 -0.46841813]
#  [-0.51605805 -0.00723334  1.19634248 -1.21598491]]

#eg 04 creating 3D array from random number that belong normal distribution
nd_rand3D=np.random.randn(3,3,3)
print(nd_rand3D)
# [[[-0.6004185  -0.65216634 -0.6914863 ]
#   [-0.44514548  2.38707124 -0.47932123]
#   [ 0.58709872 -0.73616222 -2.78751433]]

#  [[-0.99081115 -2.45215591 -1.47844412]
#   [ 0.43347267 -1.02551091  1.65044907]
#   [-0.50651446 -0.20004402  0.16310205]]

#  [[-0.31146545  1.63784712 -0.52508535]
#   [-0.54648399 -2.08734157  0.10962595]
#   [ 1.10095595 -0.81980513  0.31967427]]]

'Normal Distribution Grapha'

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(100000)

plt.hist(x, bins=50)
plt.show()


'4.choice()'
'''
-we use np.random.choice() in NumPy to randomly pick one or more elements
from a given array or list
-syntax
| Array Type               | `choice()` Syntax                               | Meaning                                          |
| ------------------------ | ----------------------------------------------- | ------------------------------------------------ |
| Single value (0D/scalar) | `np.random.choice(a)`                           | Returns one random element from `a`.             |
| 1D                       | `np.random.choice(a, size=n)`                   | `n` = number of elements to choose.              |
| 2D                       | `np.random.choice(a, size=(rows, cols))`        | Creates a `rows × cols` array of random choices. |
| 3D                       | `np.random.choice(a, size=(depth, rows, cols))` | Creates a 3D array of random choices.            |
'''
#eg 01 selecting single random number from array
arr = np.array([24,5,64,32,67,85])
pic_rand=(np.random.choice(arr))
print(pic_rand)
# 5
# 85

#eg 02 selecting multiple random numbers to creating 1D dimentional array 
arr2 = np.array([24,5,64,32,67,85])
pic_rands=np.random.choice(arr2,size=3)
print(pic_rands)
# [67 24 64]

#eg03 selecting multiple random number to create 2D dimentional array
pic_rands2=np.random.choice(arr2,size=(2,3))
print(pic_rands2)
# [[85 64 32]
#  [ 5 64 64]]

#eg04 selecting multiple random number to create 3D dimentional array
arr3=np.array([1,2,3,4,5,6,7,8,9,10])
pic_rands3=np.random.choice(arr3,size=(3,3,3))
print(pic_rands3)
# [[[ 2  5  1]
#   [ 3  3  5]
#   [ 4 10  6]]

#  [[ 5  3 10]
#   [ 3  1  2]
#   [ 6  7  3]]

#  [[ 5  3  8]
#   [ 1  8  5]
#   [ 3  3  4]]]