'''a.List[]'''
# it is a collection of object or values that stored in sequence 
# list are mutubles 
# list stores multiples datatypes 
# list allow duplicate values 
# list denote by []

list = [1,2,3,4,5,6,7,8,9]
print(list)
#[1,2,3,4,5,6,7,8,9]

'''in previous chaptar we seen that we do indexing 
operation with list  so list mutuble'''

'''a.a. list methods'''

'''1.append()'''
'''append method used in python to add new value end of list '''
list.append("shubham")
print(list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 'shubham']

'''2.insert()'''
'''insert method used python to add value in list
at specific index position using Index'''
'''syntax
    list_name.insert(index, element)'''

list.insert(0,"jay hind")
print(list)
# ['jay hind', 1, 2, 3, 4, 5, 6, 7, 8, 9, 'shubham']

'''3.extend()'''
'''the extend() method used in python to add elements ([list iterable])
at end of a list '''
'''syntax 
     list_name.extend([iterable])'''
     
# eg
list2=[1,2]
print(list2) 
# [1,2]
list2.extend(["extending",4,5,6,7,8,9])
print(list2)
#[1, 2, 'extending', 4, 5, 6, 7, 8, 9]

'''4.remove()'''
'''remove() method used in python to remove specific element from list'''
'''syntax 
       list_name.remove(value)'''
       
l=["happy","sad","love","angry"]
l.remove("angry")
print(l)
#['happy', 'sad', 'love']

'''5.pop()'''
'''pop() method used to delete specific element form list but unlike
remove() its delete elements using index and also if index not provided 
its delete last element of list '''

'''syntax 
       list_name.pop(index)'''
#eg
l2=["india","china","russia","usa","england"]
#index   1      2       3       4      5
l2.pop() 
print(l2)
# output - ['india', 'china', 'russia', 'usa']

l2.pop(1)
print(l2)
# output - ['india', 'russia', 'usa']

# note - if you used pop() at empty list raise indexError

'''6.sort()'''
'''sort() method is used to arrange elements of a list in a specific 
order and by default its sorts list in ascending order '''

l3 = [2,4,6,8,0,3,5,7,1]
l3.sort()
print(l3)
# output - [0, 1, 2, 3, 4, 5, 6, 7, 8]

'''7.index()'''
'''index() is used to find position of an element in list'''
'''syntax  
        list_name.index(element)'''
        
l4=["rose","cherry_blossoms","morning_glory","hibscus"]
print(l4.index("rose"))
# output - 0 

'''8.count()'''
'''count() method used in python to count appeareance of specific
element in a list '''

'''syntax 
       list_name.count(element or value)'''
       
l5 = [85,False,True,(8+9j),85,"fire","water",85,False,85]
counts =l5.count(85)
print(counts)
# output - 4 