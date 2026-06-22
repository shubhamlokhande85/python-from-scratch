'''SET '''
'''SET COMPARISON METHOD'''

'1.issubset()'
'''The issubset() method checks whether all elements of one set are present in another set'''
'''its return boolean values True if set present in another set otherwise False '''

'syntax'
'set_name1.issubset(set_name2)'

'eg'
s1 = {1,2,3,4,5}
s2={1,2,3,4,5,6,7,8,9,10}
print(s1.issubset(s2)) # its basically see im present or not in you 
# True

'2.issuperset()'
'''The issuperset() method checks whether a set contains all elements of another set'''
'''its return boolean values True if set contain another set otherwise False '''
'syntax'
'set_name1.issuperset(set_name2)'

'eg'

s3={1,2,3,4,5}
s4={1,2,3}
print(s3.issuperset(s4)) # its check your all elements are peresent in me or not 
# True

'3.isdisjoint()'
'''The isdisjoint() method  checks whether two set have no common elements'''
'''it returnd true if the two sets have no commmon elements and return false even if both
the set share atleast one common element'''

'its checks set are different or not from each other'

'syntax'
'set_name1.isdisjoint(set_name2)'

'eg.1'

s5={1,2,3,4,5}
s6={6,7,8,9,10}
print(s5.isdisjoint(s6))
#True

'eg.2'
s7={1,2,3,4,5,6}
s8={6,7,8,9,10}
print(s7.isdisjoint(s8))
# False 

