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
print(next(iterator)) # if here we does not used next fuction then it will return output in object type likle -<list_iterator object at 0x00000226DB3C05B0>
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

'B.Generator'
'''
In python a generator produces values one at time using YIELD . pausing after each value and resuming from the same 
point when the next value is requested'''
#eg 01
def hello():
    yield 1 
    yield 2 

h = hello()
print(next(h))
print(next(h))
#1
#2

#eg 02
def square_generator():
    for i in range (1,10):
        yield  i * i
        
        
square = square_generator()
print(next(square))
print("pause")
print(next(square))
print("pause")
print(next(square))
print("pause")
print(next(square))
# 1
# pause
# 4
# pause
# 9
# pause
# 16

'C.closure'
'''
-It is Nested function that remember values
-In python a  closure is a function that remembers varaibles from its outer(enclosing) function even after the outer 
function has  finished execution'''
# eg 01 
def outer_function(n):
# first outer function created now n= 5 
    def inner_function(m):
    # n = 5 value goes into inner_function and refer n = 5 
        return m * n  
        
    return inner_function
    # here inner_function dont have () parentheses so it refer back to fuction object like outer_function=inner_function 
    # so this statement refers back to the object where the outer_function is called
    # -- before -- closure=outer_function --after -- closure=inner_function

closure=outer_function(5)  
# its first call outer_funtion with n = 5
# and then return inner_function is runned it refers is back to object of outer_function 
# now after then reference outer_function=inner_function
print(closure(10))  
# this is actual outer_function(10)=inner_function(m)
#output - 50 
print(closure(40))
# this is actual outer_function(40)=inner_function(m)
#output - 200

#eg 02
def outer_function(n):
    # outer_function is called with n = 5

    def inner_function(m):
        # inner_function uses n from the outer function.
        # It does NOT copy n into itself.
        # Instead, it keeps a reference to n (closure).

        return m * n

    return inner_function
    # Return the function object itself (not calling it).


closure = outer_function(5)
# Step 1: outer_function(5) is executed.
# Step 2: n = 5
# Step 3: inner_function is created.
# Step 4: inner_function remembers n = 5.
# Step 5: outer_function returns the inner_function object.
# Step 6: closure now refers to that returned function.

print(closure(10))
# This is equivalent to:
# inner_function(10)
#
# m = 10
# n = 5 (remembered from outer_function)
#
# return 10 * 5
#
# Output: 50 

#eg 03 
def outer(x):
    def inner(y):
        return x*y 
    return inner 

cl=outer(5)
#  here when object created  x = 5 
# then refer back to function object then  outer = inner
print(cl(20)) # inner(20) = inner(y)
#output = 100 

'D.decorator '
'''
-A Decorator in python is a function that modifies the behaviour of another function without changing its code
-@decorator  :
is used to apply a decorator to a function in a simple readble way 
-decorators are used to add extra work before after or around a function without changing the original function code
-Wrapper() used here add extra work here'''
# eg -01 



def decorator(function):
    # decorator() is defined here.
    # It receives the original function (display) as an argument.
    # At this point, decorator() is only created, it is not running yet.

    def wrapper():
        # wrapper() is the new function that replaces display().
        # It controls when the original display() function runs.
        # Any extra behavior can be added before or after calling display().

        print("hello from Wrapper first time")

        function()
        # function refers to the original display() function.
        # When this line executes, control goes inside display()
        # and display() starts running.

        a, b = 100, 200
        # After display() finishes, control comes back here.
        # Now wrapper() continues executing the remaining code.

        print("sum of :", a, "and", b, "is", a + b, "from wrapper second time")

    return wrapper
    # decorator() returns the wrapper function.
    # The returned wrapper replaces the original display function.


@decorator
def display():
    # This function is created normally first.
    # But because of @decorator, Python internally does:
    #
    # display = decorator(display)
    #
    # The original display function is sent into decorator().
    # decorator() returns wrapper.
    # Now the name "display" points to wrapper, not the original display.

    print("hello from display")


display() # it is actually wrapper()
# This actually calls wrapper(), not the original display().
# wrapper() then calls the original display() using function().
#after the return wrapper display = decorator(display) become display = wrapper

'E.Property'
'''
-A property is an object that holds a reference to methods (getter/setter/deleter) not a normal variable or value 
-A property allows you to access a method like an attribute 
'''
'1.how to access attribute from class '
'syntax'
'print(object_name.attribute_name)'
#eg
class variable:
    a =10
    
v=variable()
print("here we access attribute from class is ", v.a)
#here we access attribute from class is  10

'2.how to access method from class'
'syntax'
'object_name.method_name([argument])'
#eg 
class method:
    def display():
        print("here we access method from class display()")
        
m=method()
method.display()
#here we access method from class display()

'3.how access method from class using property like attribute'
class pro:
    def __init__(self,age):
        self.__age=age
    @property
    def show(self):
        print("Age of shubham is ",self.__age)
        
p=pro(24)
p.show
#Age of shubham is  24   