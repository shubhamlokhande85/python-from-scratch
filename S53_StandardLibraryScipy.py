'SCIPY'
'''
-Scipy is a predefined python library used for scientific, mathematical and 
enginnering computation
-It is built on top of numpy and provides many adavance function so you 
don't have to write complex algorithms from scratch
-
| Module              | What to Learn                    | Use                        |
| ------------------- | -------------------------------- | -------------------------- |
| `scipy.stats`       | Statistics, tests, distributions | Data analysis              |
| `scipy.linalg`      | Matrix operations, eigenvalues   | Linear algebra, ML         |
| `scipy.optimize`    | Optimization, curve fitting      | Finding best solutions     |
| `scipy.integrate`   | Integration (`quad`)             | Calculating integrals      |
| `scipy.interpolate` | Interpolation (`interp1d`)       | Estimating values          |
| `scipy.signal`      | Signal processing, filters       | Audio & sensors            |
| `scipy.spatial`     | Distance, geometry, KD-tree      | Clustering, nearest search |
| `scipy.fft`         | Fourier Transform                | Frequency analysis         |
| `scipy.ndimage`     | Image processing                 | Image filtering            |
| `scipy.sparse`      | Sparse matrices                  | Large data matrices        |
| `scipy.special`     | Special functions                | Advanced math              |
| `scipy.constants`   | Scientific constants             | Scientific calculations    |
| `scipy.io`          | File input/output                | Data import/export         |
'''



'1.Statistical functions(stats)'
'''
scipy.stats is a module in the SciPy library that provides a wide range of statistical functions
for analyzing data. It includes functions to calculate descriptive statistics, probability 
distributions, hypothesis tests, correlation, regression, and other statistical measures.

| Function              | Description                                     |
| --------------------- | ----------------------------------------------- |
| `stats.gmean()`       | Calculates the geometric mean.                  |
| `stats.hmean()`       | Calculates the harmonic mean.                   |
| `stats.tmean()`       | Calculates the trimmed mean.                    |
| `stats.mode()`        | Finds the most frequent value.                  |
| `stats.describe()`    | Returns a statistical summary.                  |
| `stats.skew()`        | Measures skewness of data.                      |
| `stats.kurtosis()`    | Measures kurtosis (peakedness).                 |
| `stats.variation()`   | Calculates the coefficient of variation.        |
| `stats.sem()`         | Calculates the standard error of the mean.      |
| `stats.zscore()`      | Calculates the z-score of data.                 |
| `stats.ttest_ind()`   | Performs an independent t-test.                 |
| `stats.ttest_rel()`   | Performs a paired t-test.                       |
| `stats.ttest_1samp()` | Performs a one-sample t-test.                   |
| `stats.chisquare()`   | Performs a chi-square test.                     |
| `stats.pearsonr()`    | Calculates the Pearson correlation coefficient. |
| `stats.spearmanr()`   | Calculates the Spearman rank correlation.       |
| `stats.linregress()`  | Performs linear regression.                     |
'''


'A.trimmed mean(stats.tmean())'
'''
-A trimmed mean is a measure of average in which a certain percentage of the
smallest and largest values are removed before calculating the mean.
-Why use it?
It reduces the effect of outliers 
(extremely high or low values) that can distort the ordinary arithmetic mean

-stats.tmean() in scipy calculates the trimmed mean (or restricted mean) of a
dataset unlike normal mean , it can ignore values outside specified limits
-syntax 
stats.tmean(data_values,limits)
where, 
1)data - data_values 
2)limits- we use limits parameter in stats.tmean() to exclude values that are 
too small ot too large from the mean calculation this is useful when dataset
contains outliers or  values that could distort the average'''

from scipy import stats 
#eg 01  normal mean 
data = [10,20,30,40,50]
print(stats.tmean(data))
# 30.0

#eg 02 mean within limits(range)
data2=[10,20,30,40,50]
print(stats.tmean(data2,limits=(29,45)))
# 35.0



'B.Geometric Mean(stats.gmean())'
'''
-The geometric mean is a type of average found by multiplying all the numbers
together and then taking the nth root of the result, where n is the total
number of value
-Geometric mean is a type of average used to find the central values of a set 
of numbers that are multiplied together instead of added 
syntax
stats.gmean(data)
-formula 
Geometric mean = nsqrt(X1*x2*...*Xn)'''

#eg 01 gmean using formula 
data3=[2,8]
'''
gmean= 2sqrt(2*8)
     = 2sqrt(16)
     = 4 
'''
#eg 02 gmena using scipy 
gmean =stats.gmean(data3)
print(gmean)
#4.0



'C. Harmonic Mean(stats.hmean())'
'''
-The harmonic mean is a type of average that is calculated by dividing the 
total number of values by the sum of their reciprocals (the inverse of each
value)
-Harmonic mean is another type of average used when we deal with rates , ratios
or speeds
-syntax
stats.hmean(data)
-formula                           /
Hormnic mean = number_of_value(n) / 1/X1 + 1/X2 +...+ 1/Xn 
                                 /                       '''
                                 
#eg 01 hmean using formula 
data4=[2,4]

'''
hmean=2/1/2+1/4
hmean=2/0.5+0.25
     =2/0.75
     =2.6666666666666665
   
'''
#eg 02 hmena using scipy stats 
hmean=stats.hmean(data4)
print(hmean)
# 2.6666666666666665
     
    
    
'2.Scipy.linalg'
'''
-scipy.linalg is a module used for linear algebra operations like working with
matrices and solving system of equations it is more advanced and optimized than
numpys linear algebra functions
-Why we use linalg ?
i) solve linear equations 
ii) matrix multiplication and inverse 
iii) Eigen values and Eigen vectors 
iv) Determinant calculation 
v) decompositon of matrices 

-Common scipy.linalg functions for matrices
| Function                | Purpose                                     |
| ----------------------- | ------------------------------------------- |
| `linalg.solve(A, b)`    | Solves linear equations **Ax = b**          |
| `linalg.inv(A)`         | Computes matrix inverse                     |
| `linalg.det(A)`         | Computes determinant of a matrix            |
| `linalg.eig(A)`         | Finds eigenvalues and eigenvectors          |
| `linalg.norm(A)`        | Computes matrix/vector norm                 |
| `linalg.lu(A)`          | Performs LU decomposition                   |
| `linalg.svd(A)`         | Performs Singular Value Decomposition (SVD) |
| `linalg.qr(A)`          | Performs QR decomposition                   |
| `linalg.cholesky(A)`    | Performs Cholesky decomposition             |
| `linalg.matrix_rank(A)` | Finds the rank of a matrix                  |
| `linalg.pinv(A)`        | Computes pseudo-inverse of a matrix         |
| `linalg.schur(A)`       | Performs Schur decomposition                |
'''


'''
'A.linear Equation in matrix '

suppose we have two linear equations and we have to find x and y values ? '''

'Eg  01 mathematical way to solve linear equation  '
a = [[3,2],
     [1,2]]
b = [5,5]
'''
here ,
a = equation value 
b = constants 

3x + 2y = 5   ...eq1
x  + 2y = 5   ...eq2

- in linear equation we first make x or y position's one of the value same in
both eqaution, then we subtract that equation from each other then we 
absolutly find x or y value  


# method 01 
lets find value of x 

:substracting eq2 from eq1 cause here y position's value are same both equation 
 
3x + 2y = 5
-
x  + 2y = 5
-------------
   -      - 
2x +  0 = 0 
      x = 0/2
      x = 0    

:substituing value of x in from eq2

x + 2y = 5 
0 + 2y = 5
    2y = 5 
    y  = 5/2
    y  = 2.5
    
Ans : Now our x = 0 and y = 2.5 

# method 02 
-In linear equation we first make x or y positions one of values same in both 
equations but here x postion values eq1 3x and eq2 x is different from each
other in that case we use equalibrium of equation concept 

lets see how its done 

:Multiply by eq2 by 3 
x + 2y    = 5 
3x+ 3(2y) = 3*5 
3x + 6y   = 15  ...eq3  # this is equalibrium equation 

:substracting eq1 from eq3 

3x + 6y = 15 
3x + 2y = 5
-------------
   -     - 
0  + 4y = 10 
     4y = 10 
      y = 10/4
      y = 2.5 
      
:substiuting y value in eq 2 
x + 2y    = 5 
x + 2(2.5)= 5   
x + 5     = 5 
        x = 5-5 
        x = 0 
        
Ans : Now y = 2.5 and x = 0  
'''
'# eg 02 solve linear equation using scipy.linalg '

'A.1 solve()'
'''solve() in scipy.linalg is used to solve a system of linear equations of the form: Ax=b
where,
A is a square coefficient matrix
b is a vector or matrix of constants
x is the unknown solution'''

from scipy.linalg import solve 
aa = [[3,2],
      [1,2]]
bb = [5,5]

print(solve(aa,bb))
# [0.  2.5] 


'B.Matrix'
'''
-In scipy.linalg, matrices are typically represented using NumPy arrays (numpy.ndarray).
SciPy's linear algebra functions operate on these arrays

-
'''

'B.1 Identity matrix'
'''
-An identity matrix is a matrix that acts like the number 1 in matrix 
multiplication. When any matrix is multiplied by an identity matrix,
the original matrix remains unchanged
-In scipy.linalg, you can create an identity matrix using the scipy.linalg.eye() function 
but its old way now new we use np.eye()
-syntax 
I = np.eye(N, dtype=int)
where ,
N is the number of rows and columns (the dimension of the identity matrix).
dtype=int makes the matrix elements integers (1 and 0) instead of float
-formula
I = A * inverse matrix (A-1)

where 
A   = original matrix 
A-1 = Inverse matrix 
I = identity matrix ( like 1 for matrices)

i)2*2 
    |1   0|
I = |     |
    |0   1|
    
ii) 3*3 
    |1 0 0|         
I = |0 1 0|
    |0 0 1|
    
'''
#eg 01  create a identity matrix 
'from scipy.linalg import eye' #  this old origin 
'''
because recent SciPy releases have removed some basic array-creation functions like eye.
NumPy is now the recommended library for creating arrays and matrices, 
while SciPy focuses on advanced linear algebra operations.'''

import numpy as np 
I = np.eye(2,dtype=int) 
print(I)
# [[1 0]
#  [0 1]]

#eg 02 matrix multiplication 
'NOTE : The @ operator in Python is the matrix multiplication operator'

a = np.array([[2, 3],
              [4, 5]])
I = np.eye(2, dtype=int )

print(a @ I)
#[[2 3]
#  [4 5]]

'B.2 inverse matrix'
'''
-An inverse matrix is a matrix that gives the identity matrix when
multiplied with the original matrix
-The inv() function in scipy.linalg computes the inverse of a square matrix.
-syntax 
A_inv = inv(A)
where , 
A → The original matrix whose inverse you want to find.
inv(A) → The inv() function from scipy.linalg that calculates the inverse of matrix A.
A_inv → A variable name used to store the inverse matrix of A

-Formula for 2*2 D matrices
              |d  -b|
A-1 = 1/ad -bc|     |
              |-c  a|   ...eq1
              
formula for 3*3 D matrices
| a b c |
| d e f |
| g h i |

A-1 = 1 / det(A).adj(A) ...eq2
where,
det(A) = determinant of matrix A
adj(A) = adjugate (transpose of the cofactor matrix)

'''
#eg 01 let see how to make origianl 2*2 matrix into 2*2 D inverse matrix  mathematical way 
'''

    |1  2| 
A = |    |
    |3  4|
    
substuting this values in eq1 

                       |4 -2| 
A-1 = 1 / 4*1 -(-2)(-3)|    |
                       |-3 1|
                       
            |4 -2| 
    = 1/4-6 |    |
            |-3 1| 
            
            |4 -2| 
    = 1/-2  |    |
            |-3 1|  
            
       |-2      1|
A-1 =  |         |
       |1.5  -0.5|
                        
                   
'''

#eg 02 let see how to make origianl 2*2 matrix into 2*2 D inverse matrix  scipy.linalg
from scipy.linalg import inv 
a = np.array([[1,2],
             [3,4]])
a_inv2 =inv(a)
print(a_inv2)
# [[-2.   1. ]
#  [ 1.5 -0.5]]

#eg 03 3*3
ar = np.array([[2,3,2],
               [1,2,4],
               [4,4,6]])

a_inv3 = inv(ar)
print(a_inv3)
# [[-0.28571429 -0.71428571  0.57142857]
#  [ 0.71428571  0.28571429 -0.42857143]
#  [-0.28571429  0.28571429  0.07142857]]

'B.3 Determinant'
'''
-A determinant is a special number calculated from a square matrix that 
tells us important information about the matrix, such as whether it has 
an inverse
NOTE :
The determinant is found only for square matrices
If the determinant is not zero, the matrix has an inverse
If the determinant is zero, the matrix has no inverse
-synatx 
detrmint_variable =det(matrix_array_name)
-formula  for 2*2 matrix determint
  |a b|
A=|   |
  |c d|
 
det(A) = ad-bc

-formula for 3*3 matrix determinant 
    | a b c |
A = | d e f |
    | g h i |
    
det(A)=a(ei-fh)-b(di-fg)+c(dh-eg)

#eg 01 2*2 matrix determinant mathematical way 
  | 1  2 | 
A=|      |
  | 3  4 |
  
det(A)= ad-bc 
det(A)=(1*4)-(2*3)
      =4-6
      =-2 

'''
'eg 02 2*2 matrix determinant scipy.linalg way  '
from scipy.linalg import det
arrr =np.array([[1,2],
            [3,4]])
d2= det(arrr)
print(d2)
# -2.0

'''
#eg 03 3*3 matrix determinant mathematical way 

  | 1 2 3 | 
A=| 4 5 6 |
  | 7 8 9 |
  
det(A)=a(ei-fh)-b(di-fg)+c(dh-eg) 
det(A)=1((5)(9)-(6)(8))-2((4)(9)-(6)(7))+3((4)(8)-(5)(7))
      =1(45-48)-2(36-42)+3(32-35)
      =1(-3)-2(-6)+3(-3)
      =-3+12-9
      =9-9
      =0
'''
'eg 04 3*3 matrix determinant scipy.linalg way'
from scipy.linalg import det 

ar = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
d3 = det(ar)
print(d3)
# 0.0

'3.Constants '
'''
-A constant is a value or quantity that does not change during a calculation,
equation, or situation'''

#eg  01 
from scipy import constants 
print(constants.pi)
# 3.141592653589793
#eg 02 
print(constants.e)
# 1.602176634e-19