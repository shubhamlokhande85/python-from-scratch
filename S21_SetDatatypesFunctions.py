'SET'
'predefined function with set'

'1. LEN()'
'it returns count of numbers of elements persent in set'
s1={1,2,3,4}
print(len(s1))
# output - 4

'2.MIN()'
'it returns the smallest element present in set'
print(min(s1))
# 1

'3.MAX()'
'it return the largest element present in set'

print(max(s1))
# 4

'4.sum()'
'it adds up all the elements present in a set '
'this pre-defined sum function works only with numerical set'

print(sum(s1))
# 10

'5.sorted()'
'it sorts the elements present in a set in a specific oreder(either ascending or descending order)'
"by default its sort ascending order"
'its return list values'

s2={10,9,7,5,8,3,6,2,4,1}
print(sorted(s2))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 