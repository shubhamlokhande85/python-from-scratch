#main program
'Module'
''' A module in python is a file containing python definations 
and statements that can be imported and used in another python program '''
'user defined module and main program must be in same directory(inside the same file and extension of both file must be .py)'




'1.accessing functions from Module'

'syntax to import function from module in main program '
'from module_name import function_nmae1,function_name2......,function_nameN'

from  Module import show, display


'syntax to access function in main program '
'function_call or function_name(arguments)'

show()
#Welcome to Python Directory (bomt)
display()
#here are the Directory files you can explore it

'2.accessing variables from Module'

'syntac import variables in  main program'
'from Module_name import variabele_name1,variable_name2.....variable_nameN'

from Module import x,y

'syntax access variable in main program'
'print(variable_name)'



print(x)
print(y)
print(x+y)
# 40
# 60
# 100


'3. combine example of function and variable importing in main program'
from Module import remainder
from Module import z

print(remainder())
# 20
print(z)
# 30

#imp
'4.for import Everything from module into the main program'
'syntax'
'from module_name import *' 

from Module import *

division()
#1.5

print(a)
print(b)
print(c)
print(d)
# 10
# 50
# 40
# 30