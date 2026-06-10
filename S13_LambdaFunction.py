'''1.Anomymous or lambda()'''
'''a lambda function is one line function that can take 
any number of arguments but return only on expreesion '''

'''syntax
      lambda arguments : expression'''
      
# eg.1  
square = lambda num : num * num 
print(square(13))    
print(square(14))    
print(square(15))
    
# output 
# 169
# 196
# 225

#eg.2 
product = lambda a , b , c : a*b*c
result=(product(2,4,6))
print(result)
# outpt -  48


'''2.Method used with lambda '''
'''2.1 .map()'''
'''it used to apply a function to every elements of iterable (list,tuple..etc)'''
'''syntax 
     map(funtion,iterable )'''
     
list1 = [1,2,3,4,5]
addition =map(lambda num : num + 10 , list1)
print(addition)

'''output is object - <map object at 0x000001A74BA8B080>'''

# its return output in object that why 
# we need to use iterable datatype function (list()) like here used list iterable 
# so 
list2 = [1,2,3,4,5]
addition2=list(map(lambda num: num + 10 , list2))
print(addition2)
# output 
'''[11, 12, 13, 14, 15]'''

'''2.2. filter()'''
'''it is used to select elements from iterable based on function condition 
its return only those elements for which the condition is true''' 

tuple1=(1,2,3,4,5,6,7,8,9,)
odd = tuple(filter(lambda num : num % 2 !=0 , tuple1)) 
# here num refer as arguments(each element) and function is performed on each elements one by one 
print(odd)
# output - odd numbers
# (1, 3, 5, 7, 9)