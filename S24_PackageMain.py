'Package'
'''A package in python is a collection of 
related modules orgnaized inside a folder(directory)'''
'A package is a folder that contains multiple python modules and __init__py file'
'package file and main program file must be have in one directory'
'and the package extension not required but main program exetension must .py'


'A.importing package modules in main program'

'1.syntax to import functions from package module in main program'
'from package_name import module_name'
#eg1
from My_Package import module1

'2.syntax Accessing a functions from module in main program'
'module_name.function_name(arguments)'

#eg1
module1.product(10,10)
#100

#eg2 
from My_Package import module2

module2.addition(10,10)
#20

'3.__init__py'



