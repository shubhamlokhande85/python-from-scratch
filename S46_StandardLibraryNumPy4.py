'E . Statistical functions in NumPy'
'''
Statistical functions are functions used to analyze numerical data by
calculating measures such as average, middle value, spread, minimum,
and maximum. In NumPy,these functions make it easy to perform statistical
calculation on arrays'''

'1. Mean (np.mean())'
'''
-Finds the average of the numbers.
-formula 
Mean=Number of values/Sum of all values
'''
# eg 
import numpy as np 
arr=np.array([10,20,30,40])
m=np.mean(arr)
print(m)
# 25.0

'2. Median (np.median())'
'''
-Finds the middle value after arranging the data in order.
'''
#eg 
arr2 = np.array([70, 80, 90, 60, 85])
med=np.median(arr2)
print(med)
# 80.0

'3. Standard Deviation (np.std())'
'''
-Measures how spread out the data is from the average.
'note'
Small value → Data is close to the mean.
Large value → Data is spread out.
# To learn this concept and formula look for chatgpt...etc'''
#eg
arr3 = np.array([70, 80, 90, 60, 85])
sd=np.std(arr3)
print(sd)
# 10.770329614269007

'4. Variance (np.var())'
'''
Measures how much the data varies from the mean
b.population variance 
a.sample variance 
# To learn this concept and formula look for chatgpt...etc
'''
#eg 
arr4 = np.array([70, 80, 90, 60, 85])
vr=np.var(arr4)
print(vr)
#116.0

'5. Minimum (np.min())'
'''
Finds the smallest number.'''
#eg
arr5 = np.array([70, 80, 90, 60, 85])
mn=np.min(arr5)
print(mn)
# 60

'6. Maximum (np.max())'
'Finds the largest number.'
#eg 
arr6 = np.array([70, 80, 90, 60, 85])
mx=np.max(arr6)
print(mx)
#90

'7. Sum (np.sum())'
'Adds all numbers together.'
arr7 = np.array([100,200,300])
sm=np.sum(arr7)
print(sm)
#600

'8. Count()'
'(array.size or np.size() or len())'
'NumPy uses arr.size, np.size(), len() to count elements.'
#eg 01 
arr8=np.array([1,2,3,4,5,6,7,8,42,7,6,874,562,])
print(arr8.size)
#13

#eg 02 
count=np.size(arr8)
print(count)
#13

#eg03 
print(len(arr8))
#13

'9. Average (np.average())'
'Similar to mean(). It can also calculate a weighted average'
#eg
arr9 = np.array([3,6,9,15,18,27,33])
ave=np.average(arr9)
print(ave)
#15.857142857142858

'10. Percentile (np.percentile())'
'''
-A percentile tells you the value below which a certain percentage of the
 data falls.
-In NumPy, the np.percentile() function finds the value at a specified
 percentile in a dataset
 -syntax
 np.percentile(array, percentile)
 where,
 array → The data values.
 percentile → A number between 0 and 100.'''
#eg 
arr10=np.array([10,20,30,40,50,60,70,80,90,100])
per=np.percentile(arr10,50)
print(per)
#55.0

'''
Why do we use np.percentile()?

-The main purpose of np.percentile() is to understand the position of data,
not just the average.

-Sometimes, the mean (average) does not tell the whole story. 
A percentile tells us how a value compares with the rest of the data.'''