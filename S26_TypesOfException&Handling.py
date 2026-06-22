'1.Types of Exceptions and Exceptions handling'

'1.1 ZeroDivisionError'
'''
It raised when a program tries to divide a Number by Zero'''
#eg - Exception
t=10
z=0
'print("division= ", t/z) '
#ZeroDivisionError: division by zero

'ZeroDivisionError:Exception handing'
try:
    print("division2= ", t/z)
except ZeroDivisionError as zde :  # zde is temporary name for ZeroDivisionError
    print(zde)  
finally:
    print("ZeroDivisionError Exception handled very well")
# Output
# division by zero
# ZeroDivisionError Exception handled very well

'1.2. IndexError'
'''
Is raised when you try to access an index that is the outside of the
valid range or a sequence such as a list , tuple or string'''


l=[1,"steve_jobs",False,True,(5+8j)]
'print(l[5])' 
#IndexError: list index out of range

'IndexError:Exceptiion handling'
try:
    print(l[5])
except IndexError as ide:
    print(ide)
else:
    print(l[5]) # [ ] here take those index that taken in try block
    'its executes only when no error occurs in try block'
finally:
    print("IndexError Is Handled Very Well")
#list index out of range
# IndexError Is Handled Very Well

'1.3.KeyError'
'''it is raised when you try to access a dictionary key that does not exist
in dictionary'''

d={1:"sataya_nadala",2:"sundar_pichai"}
'print(d[3])' # accessing value of index 3 in dictionary d
#KeyError: 3

'KeyError Exception handling'
try:
    print(d[3])
except KeyError as ke:
    print(ke)
else:
    print(d[3])
finally:
    print("KeyError Is Handled Very Well")
#3
# KeyError Is Handled Very Well

'1.4.NameError'
'''
Is raised when you try to use or access variable that not defined'''

#eg
'print(y)'
#NameError: name 'y' is not defined   

'NameError Exceeption Handling'
try:
    print(y)
except NameError as ne:
    print(ne)
else:
    print(y)
finally:
    print("NameError Is Handled Very Well")
#name 'y' is not defined
#NameError Is Handled Very Well

'1.5. ModuleNotFoundError'
'''
It is raised when python cannot find the module you try to import'''
# if you want learn about import and module look import and module session
# eg
'import m1'
#import m1
# ModuleNotFoundError: No module named 'm1'

'ModuleNotFoundError Exception Handling'
try:
    import m1 
except ModuleNotFoundError as mnfr:
    print(mnfr)
finally:
    print("ModuleNotFoundError Handled Very Well")
    
#No module named 'm1'
# ModuleNotFoundError Handled Very Well

'1.6.ImportError'
''''
It is raised when python fails to import module , package or name'''
#eg
'from My_Package import m1 '
#from My_Package import m1
#ImportError: cannot import name 'm1' from 'My_Package' (unknown location) 

'ImportError Exception Handling'
try:
    from My_Package import m1 
except ImportError as ie: 
    print(ie)
finally:
    print("ImportError handled very well")
    
#cannot import name 'm1' from 'My_Package' (unknown location)
# ImportError handled very well

'1.7.FileNotFoundError'
'''
It is raised in python when you try to access a file that does 
not exist at specified path '''
# if want learn about with open() look at FileHandling session 
'''
with open("python.txt","r") as file:
    data = file.read()
    print(data)'''
#FileNotFoundError: [Errno 2] No such file or directory: 'python.txt'  

'FileNotFoundError Exception handling'

try:
    with open("python.txt","r") as file: # with open() to this function file name always pass as string
        data=file.read()
        print(data)
except FileNotFoundError as fnfr:
    print(fnfr)
else:
    print(data)
finally:
    print("FileNotFoundError is handled very well")
    
# [Errno 2] No such file or directory: 'python.txt'
# FileNotFoundError is handled very well

'1.8.TyprError'
'''
it is raised in python when an operation or function is applied to a 
value of an inappropriate data like different datatypes operations 
without using type casting'''

# if want learn about type casting look for type casting session 

s=10
n="New_York"
'print(s+n)'
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

'TypeError exception handling'
try:
    print(s+n)
except TypeError as te:
    print(te)
else:
    print(s+n)
finally:
    print("TypeError is handled very Well")
#unsupported operand type(s) for +: 'int' and 'str'
#TypeError is handled very Well

'1.9.IndentationError'
'''
it is raise when python find incorrect spacing or alignment 
(indentation) in your code'''

a,b=100,200
# if a>b:
# print(a,"is greater than",b)
#IndentationError: expected an indented block after 'if' statement on line 183

# important notes
'''
a.indentation is compile - time error 
b.python checks code line by line and also
indentation before running program
c.so this error usually cannot handle by try-except 
because the program does not execute'''

'1.10.AttributeError'

'''
it is raise when you try to access attribute or method that 
an object does not have'''
#eg
class test:
    num = 10
    def display(self):
        print("hey hi guys my name is shubham")
t = test()
'print(t.p)'
#AttributeError: 'test' object has no attribute 'p'
't.show()'
#AttributeError: 'test' object has no attribute 'show'

'AttributeError Exception handling'

try:
    print(t.p)
except AttributeError as ae:
    print(ae)
else:
    print(t.p)
finally:
    print("AttributeError is handled very well")

#'test' object has no attribute 'p'
# AttributeError is handled very well

try:
    t.show()
except AttributeError as ae:
    print(ae)
finally:
    print("AttributeError is handled very well")
    
#'test' object has no attribute 'show'
# AttributeError is handled very well

'if attribute or method is present'
try:
    t.display()
except AttributeError as ae:
    print(ae)
finally:
    print("AttributeError is handled very well")
#hey hi guys my name is shubham
# AttributeError is handled very well
' 1.11.KeyBoardError'
'''
It is raised when the user manually interrupts 
the program or python program'''

'Notes'
'''
a.when a python program is running (especially when loops or long program)
we many need to forcefully stop it before it finishes, pressing ctrl + c
sends an signal interrupt signal to python which raises a 
KeyBoard intterrupt exception and stops execution

b. we use ctrl + c in python to stop or interrupt running program
manually
'''
for i in range(1,10000):
    print(i)
    
#     print(i)
#    ~~~~~^^^
# KeyboardInterrupt


'IMP'
'2.AssertionError'  
'''
An assertion is a debugging feature used 
to check if condition is ture'''

'''
if the condition is True then python return nothing but if condition 
is False then python raise AssertionError '''

'syntax'
'assert condition , "Error_message'
# here
# assert is keyword
#condition is here True or False
#Error_Message is here to user defined Erroe Message

#eg
m,n=20,10
assert m>n,"m is greater than n"
# output -     'its return nothing cause condition is true'

mm,nn=10,20
assert mm>nn,"mm is greater than nn"
#    assert mm>nn
#            ^^^^^
# AssertionError: mm is greater than nn



