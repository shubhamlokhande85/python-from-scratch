'''SET'''
'''set is a collection of objects or values that are not stored
sequence and hence also unindexed'''

'''-set are unorderd '''
'''-set can store different types data types'''
'''-set are immutable datatype and set cannot be updated using index '''
'''-set does not allow duplicate values'''
'''set denotes curly brackets { }'''

s = {"welcome",True,False,45,(7+8j)}
print(s)

s2= set()  # empty set - define like this set()
print(type(s2))
print(s2)
# <class 'set'>
# set()

s3={}
print(type(s3))
print(s3)
#<class 'dict'>
# {}

s4=[]
print(type(s4))
print(s4)
#<class 'list'>
# []

'''1.set methods '''

'''1.1 add()'''

# it is used to add element in the set
'''syntax
     set_name.add(element)'''
     
s.add("hello")
print(s)
# {False, True, 'hello', (7+8j), 45, 'welcome'}

'''2.2.update'''
# it is used to add multiple elements in set at once
'''syntax
       set_name.update(iterable)'''
       
s.update([46,856,"night","midnight"])
print(s)
# {False, True, 'hello', 'midnight', 856, (7+8j), 'night', 45, 46, 'welcome'}

'''3.3. remove()'''
# it is used to delete a specific element from a set 
'''syntax
     set_name.remove(element)'''
     
s.remove("night")
print(s)
#{False, True, 'hello', 856, 'midnight', (7+8j), 'welcome', 45, 46}


# if element not preset its raise error (KeyError)
s.remove("shubham")
''' print(s) '''
# its raise KeyError cause shubham element not in the set 

'''3.4.discard'''
# its is used to delete specific element from a set 
# but when element not exist in set its not raise any error(KeyError) unlike remove() method

'''syntax
      set_name.discard(element)'''
      
s.discard("shubham") # shubham is not in set still discard not raise error 
print(s)

s.discard(True)
print(s)
# {False, 'midnight', 'welcome', 856, (7+8j), 45, 46, 'hello'}

'''3.5.pop()'''
# it is used to remove and return a random element from set 
# also we can see which item removed by pop()
'''syntax
      set_name.pop()'''
      

# also we can see which item removed by pop()
r=s.pop()
print(r)
#False

'''3.6.clear()'''
# it is used to  remove all elements from a set 
# and return empty set 
'''syntax
        set_name.clear()'''
s.clear()
print(s)
# set()


'''bonus point'''
'''delete'''
# its delete entire set

del s  # its delete enitre set 
# print(s)
#NameError: name 's' is not defined. Did you mean: 's2'?