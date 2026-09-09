'Module '

'NOTE : Here Just Understand Concept - Module , Import ,From .....Import  '
"""

Topic: Modules in Python

======================================================================
                            MODULE
======================================================================

Definition:
A Module is a Python file containing code such as variables,
functions, classes, or statements that can be reused in another
Python program.

A module is saved with the .py extension.

Example:
MY_Module.py

======================================================================
                       CREATING A MODULE
======================================================================

Example:

File 01 : My_Module.py

Create a file named:

    MY_Module.py

Add the following code:

"""

def greet():
    print("Hello from my module!")

'''
File 02 : Module.py3

create a file named :

 Module.py
'''

from My_Module import greet

greet() 

# output 
# Hello from my module!




"""
======================================================================
                       IMPORTING A MODULE
======================================================================

Definition:
The import statement is used to access code from another module.

Syntax:

import module_name

Example:

"""

import math

print("\n========== MODULE EXAMPLE ==========")

print("Square root:", math.sqrt(25))


"""
======================================================================
                       FROM IMPORT
======================================================================

Definition:
The from ... import statement is used to import a specific
function, variable, or class from a module.

Syntax:

from module_name import item

Example:
"""

from math import sqrt

print("\n========== FROM IMPORT ==========")

print("Square root:", sqrt(25))


"""
======================================================================
                         QUICK REVISION
======================================================================

Module
-> A Python file containing reusable code.

Extension
-> .py

import
-> Imports a module.

from ... import
-> Imports a specific item from a module.

Example:

import math
print(math.sqrt(25))


"""
