'STANDARD LIBRARY'
'1.NumPy'
'''
-It stands for numerical python
-Numpy is used for mathematical functions ,statistical function, linear algebra 
operations,arrary manipulation, random number generation and scientific 
computing in python 
-
'A.NumPy Mathematical functions'
'B.NumPy Trigonometric functions'

A.NumPy Mathematical function '''
import numpy as np

'1.Addition'
'-In numpy we add number using .add()'
'-and it take only two arguments'
#eg
ad=np.add(10,10)
print(ad)           # 10
print(np.add(10,20))# 30

'2.Substraction'
'-In numpy we subtract number using .subtract()'
'-and it take only two arguments'
#eg 
sub=np.subtract(30,15)
print(sub)               # 15
x,y=40,20
print(np.subtract(x ,y)) # 30

'3.Multiplication'
'-In numpy we multiply number using .multiply()'
'-and it take only two arguments'
#eg
multi=np.multiply(10,30)
print(multi)
# 300

'4.Division'
'-In numpy we divide number using .divide()'
'-and it take only two arguments'
a,b=13,1
divide=np.divide(a,b)
print(divide)
#13.0

'5.Square root'
'-In numpy we get square root of a number using .sqrt())'
'-and it take only one arguments'
#eg 
print(np.sqrt(49))
#7.0

'6.Power'
'-In numpy we get raise second number into power of first number using .power()'
'-and it take only two arguments'
m,n=4,3
p=np.power(m,n) # 4*4*4*4
print(p)
#256

'7.log()'
'.log() calculates the natural logarithem of a number -logarithem to the base e'
#eg 
print(np.log(4))
#1.3862943611198906

'8.exp()'
'.exp() calculates the exponential value where e = 2.718'
#eg
print(np.exp(5))
#148.4131591025766

'9.abs()'
'''.abs() returns the the absolute value of numbers . it converts negative
into positive numbers '''
#eg 
print(np.abs(-11))
# 11

'B.Trigonometric Functions'
'''
-in python trigonometric function in NumPy usally take angles in radians not 
degree


-to convert degree into radians 
'formula'

radians=pi/180 * degrees

where
pi = mathematical pi = 3.14

'1.sin()'

#eg1: 30 degree in radians using maths for a  - sin(30)
radians = pi/180*30
        =pi/6  # this used in NumPy 
        =3.14/6
        =0.5
        
IMP NOTEs : In NumPy we use pi/6 as a radians value not 0.5
'''
'#eg2 : 30 degree in radians using NumPy for a  -sin(30)'
s=np.pi/6  # np.30
'here pi/6 is radians value of 30 degree'
print(np.sin(s))
#0.49999999999999994
 
'2.cos()'
'#eg : 45 degeree in radians for a cos(45)'
c=np.pi/4
print(np.cos(c))
#0.7071067811865476


'3.tan()'
'#eg : 60 degree in radians for tan(60)'
t=np.pi/3
print(np.tan(t))
#1.7320508075688767
 
 
# this how we can use multiple mathematical and trigonomatric function in numpy
# to solve complex mathematical calculations and problems
 