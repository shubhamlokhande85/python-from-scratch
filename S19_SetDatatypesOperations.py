'''SET'''
'''1. Set operation'''

'''1.1 union operation (|) '''

'''The union operation combines elements from two or 
more sets and returns a new set containin unique elements '''

'''return unique values and also return first appearence of duplicate values '''

set1={1,2,44,5,6,True, (7+8j)}
set2={"shubham","Nipoon",False,1,2,33,44,5}

# method -1 
nset1=set1.union(set2)
print(nset1)
# output - {False, 1, 2, 33, 5, 6, 44, 'Nipoon', 'shubham', (7+8j)}

#method -2 
nset2=set1|set2
print(nset2)
# output - {False, 1, 2, 33, 'shubham', 5, 6, 44, 'Nipoon', (7+8j)}

'''look above example you see that True is not inclued '''
'''reason '''
'''In Python, True and False are boolean values, but since bool is a subclass of int,
True is treated as 1 and False as 0. Therefore, sets consider
True and 1 (or False and 0) to be the same element and store only one of them.'''

#eg
s = {1, True}
print(s)
# {1}

s2 = {True , 1}
print(s2)
#{True}

'''same example goes for False'''


'''2.2 intersection operation (&)'''
 
'''The intersection operation gives the common elements present in two or more sets'''

'''removes uniqune values from both set and more set and 
return new set of duplicate values from both set or more set'''

'''its return only duplicate values from both set '''

s3={1,2,3,4,5,6}
s4=(4,5,6,7,8,9)
# print(s3&s4)
print(s3.intersection(s4))
# output - {4, 5, 6}

'''3.3 difference operations ( - )'''

'''the difference operation returns elements that 
are present in the first set but not in the second set'''

'''its only return unique values from first set '''

s5={1,2,3,4,5,6}
s6={4,5,6,7,8,9}

# method - 01
print(s5-s6)
# ouput - {1, 2, 3}

# method 02 
print(s5.difference(s6))
# output -{1, 2, 3}

'''4.4 symmetric_Differences operation ( ^ )'''

'''its return unique values from both set'''

s7 = {1,2,3,4,5,6,7,8}
s8={5,6,7,8,9,10,11,12}

print(s7^s8)
#{1, 2, 3, 4, 9, 10, 11, 12}
print(s7.symmetric_difference(s8))
#{1, 2, 3, 4, 9, 10, 11, 12}





