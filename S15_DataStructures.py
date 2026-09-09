'PYTHON DATA STRUCTURES'


'''
------------------------------------------------------------
1. LIST
------------------------------------------------------------
Introduction:
A List is one of the most commonly used data structures
in Python. It is used to store multiple items in a single
variable.

Important Features:
- Ordered
- Mutable (changeable)
- Allows duplicate values
- Allows different data types
- Created using square brackets []

Example:
'''
fruits = ["Apple", "Banana", "Mango"]
print(fruits)


'''
------------------------------------------------------------
2. TUPLE
------------------------------------------------------------
Introduction:
A Tuple is a collection used to store multiple items in a
single variable. It is similar to a List, but its values
cannot be changed after creation.

Important Features:
- Ordered
- Immutable (not changeable)
- Allows duplicate values
- Allows different data types
- Created using parentheses ()

Example:

'''
colors = ("Red", "Green", "Blue")
print(colors)


'''
------------------------------------------------------------
3. SET
------------------------------------------------------------
Introduction:
A Set is a collection used to store unique items. It is
useful when we want to remove duplicate values or perform
mathematical set operations.

Important Features:
- Unordered
- Mutable (changeable)
- Does not allow duplicate values
- Allows different data types (with hashable elements)
- Created using curly brackets {}

Example:

'''
numbers = {10, 20, 30, 40}
print(numbers)

'''
------------------------------------------------------------
4. DICTIONARY
------------------------------------------------------------
Introduction:
A Dictionary is a collection of data stored in the form
of key-value pairs. Each key is used to access its value.

Important Features:
- Stores data as key-value pairs
- Mutable (changeable)
- Keys must be unique
- Fast access using keys
- Created using curly brackets {}

Example:
'''
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}
print(student)

'''
============================================================
                 QUICK INTRODUCTION
============================================================

List:
Store multiple items that may need to be changed.
Example: fruits = ["Apple", "Banana", "Mango"]

Tuple:
Store multiple items that should not be changed.
Example: colors = ("Red", "Green", "Blue")

Set:
Store unique items without duplicates.
Example: numbers = {10, 20, 30}

Dictionary:
Store information using key-value pairs.
Example: student = {"name": "Rahul", "age": 20}


'''