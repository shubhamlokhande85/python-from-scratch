'''Tuple'''
# it is a collection of object or values that stored in sequence 
# tuple is immutable datatype 
# tuple stores multiple datatypes 
# tuple stores duplicate values 
# tuple denotes by ()
# tuple  does not support item deletation 

t = (34234,"shubham",True , (9+4j),True,"shubham")
print(t)
# output - (34234, 'shubham', True, (9+4j), True,'shubham')


'''tuple methods'''

'''1.index()'''
'''in tuple index() method used to  return index position of element'''
print(t.index((9+4j)))
# output - 3 

'''2.count()'''
'''in tuple count() method used to return how many appearence of specific element '''
print(t.count("shubham"))
# output - 2 

'''3.delete'''
'''del t[0] ''' # tuple  does not support item deletation 
print(t) 

del t # this is delete entire tuple 
# print(t)
# its raise error 
# NameError: name 't' is not defined


'''indexing'''
t2=("shubhm",32,True,False)
print(t2[1])

# 32 


