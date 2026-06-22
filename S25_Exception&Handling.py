'A.Exception(Error)'

'''
In python an exception is an error or unexcepted event that occurs 
while a program is running '''
'''
whene an exception happens , python stoped normal flow of the program
and raises an error message'''
'why error occurs '
'''
1.wrong syntax
2.invalid operations
3.incorrect input
4.logical mistakes in code'''

#eg
x = 10 /0
'print(x)' # its raise DivisinError cause we cannot divide a number by zero
#ZeroDivisionError: division by zero

'B.So handle this errors(Exceptions) we use Exceptions handling'
'''
in python,error are handled using exception handling with try,
except,else and finally blocks'''
'''
when we handle Exceptions then normal flow of the program continues'''

'syntax of Error Handling or Exception Handling'
'''
Try:
    '# code that may cause an error
except:
    '#code that handle the Error'
'''
'lets know about blocks'
'1.Try'
'''
it contains the block of code that might cause an 
error(exception)'''

'2.except'
'''
it contains the block of code that runs when error occurs in the 
try blockand handles errors'''

'3.Else'
'''
it is used to run code only when no error occurs in the try blocks'''

'4.finally'
'''
it is part of Exception handling it always executed in the end of 
exception handling regardless whether an exception occured or not'''



