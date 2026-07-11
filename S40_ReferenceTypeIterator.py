'Reference Type'
'''
In Python, reference type means that a variable name holds a reference to an object, not the object itself.
This concept is important because many advanced Python features (iterators, generators, decorators, 
closures, properties) involve objects that are created, referenced, and passed around'''

'A.Iterator'
'''In python an iterator is an object that is used to traverse(go through)all
the elements of a collection one by one without using indexing '''

'1.__iter__()'
'''
in python we use __iter__() to make an object iterable , meaning we can loop through its items using a for loop'''

#eg 01 
numbers=[1,2,3,4,5,6,7]
for i in numbers:  # here iterator = numbers.__iter__()
    print(i)
# 1
# 2
# 3
# 4
# 5
# 6
# 7

# eg 02
sum_num=[2,4,6,8,10]
iterator=sum_num.__iter__()
print(next(iterator)) # if here we does used next fuction it return output in object type likle -<list_iterator object at 0x00000226DB3C05B0>
print(next(iterator))
print(next(iterator))
print(next(iterator))
# 2
# 4
# 6
# 8

'2.__next__()'
'''
-In python __next__() is used to get the next value from an iterator one step at a time 
-In python an iterator raises StopIteration Error when there are no more items left to return 
'''
# eg 
odd_num=[1,3,5,7,9]
print(type(odd_num))
iterator2=iter(odd_num) # odd_num.__iter__()
print(type(iterator2))

print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
# print(next(iterator2)) # we try accesss next iteration that does defined by user it will StopIteration Error 

# <class 'list'>
# <class 'list_iterator'>
# 1
# 3
# 5
# 7
# 9

# StopIteration