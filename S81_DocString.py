"""
DOCSTRINGS

"""


# ============================================================
# 1. DEFINITION OF DOCSTRING
# ============================================================

"""
A docstring (documentation string) is a string used to describe what a Python module, function, class, or method does.

- A docstring can be accessed in the terminal using the __doc__ attribute.
- Docstrings are usually written using triple quotes:
    """ """ 
or
    ''' '''
"""


# ============================================================
# 2. FUNCTION DOCSTRING
# ============================================================

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


print("Function Docstring:")
print(add.__doc__)
print("Result:", add(10, 20))

# ============================================================
# 3. CLASS DOCSTRING
# ============================================================

class Student:
    """Represent a student."""

    def __init__(self, name, marks):
        """Initialize the student's name and marks."""
        self.name = name
        self.marks = marks

    def display(self):
        """Display the student's information."""
        print("Name:", self.name)
        print("Marks:", self.marks)


print("\nClass Docstring:")
print(Student.__doc__)


# ============================================================
# 4. METHOD DOCSTRING
# ============================================================

print("\n__init__ Method Docstring:")
print(Student.__init__.__doc__)

print("\ndisplay Method Docstring:")
print(Student.display.__doc__)


# ============================================================
# 5. ACCESSING DOCSTRING USING __doc__
# ============================================================

def greet():
    """Display a greeting message."""
    print("Hello, Student!")


print("\nAccessing Function Docstring using __doc__:")
print(greet.__doc__)


# Creating an object
s1 = Student("Rahul", 85)

print("\nCalling display():")
s1.display()


# ============================================================
# 6. MODULE DOCSTRING
# ============================================================

"""
The first string in a Python file can be the module docstring.

It describes the purpose of the complete Python file.

The module docstring can be accessed using:

    __doc__

For example, if this file is imported:

    import docstrings

    print(docstrings.__doc__)
"""


# ============================================================
# 7. DOCSTRING VS COMMENT
# ============================================================

def example():
    """This is a docstring."""

    # This is a comment.
    # Comments are used to explain code to programmers.

    print("Hello")


print("\nDocstring:")
print(example.__doc__)

print("\nComment:")
print("Comments cannot be accessed using __doc__.")


# ============================================================
# 8. DIFFERENCE BETWEEN DOCSTRING AND COMMENT
# ============================================================

"""
DOCSTRING:
-----------
1. Used to document Python code.
2. Usually written inside a module, class, function, or method.
3. Can be accessed using __doc__.
4. Helps users understand what the code does.

COMMENT:
--------
1. Used to explain code to programmers.
2. Starts with #.
3. Cannot be accessed using __doc__.
4. Usually explains a particular line or part of the code.
"""


# ============================================================
# 9. TYPES OF DOCSTRINGS
# ============================================================

"""
There are three common types of docstrings:

1. Module Docstring
   - Describes the complete Python file.

2. Function/Method Docstring
   - Describes what a function or method does.

3. Class Docstring
   - Describes what a class represents.
"""


# ============================================================
# 10. SIMPLE EXAMPLE
# ============================================================

def square(number):
    """Return the square of a number."""
    return number * number


print("\nSquare Function:")
print(square.__doc__)
print("Square of 5:", square(5))


# ============================================================
# 11. IMPORTANT POINT
# ============================================================

"""
IMPORTANT:

The docstring must normally be the first statement inside
a function, class, or module.

Correct:
"""
def hello():
        """Print Hello."""
        print("Hello")
hello()      
"""
If the string is written somewhere else, it is not treated
as the function/class docstring.
"""


# ============================================================
# QUICK REVISION
# ============================================================

"""
DOCSTRING = Documentation inside Python code

COMMENT = Explanation for programmers

__doc__ = Used to access a docstring

Example:
"""
def greet():
    """Display a greeting."""
    print("Hello")
greet()  
print(greet.__doc__)
  
  
    
"""

Output:

    Display a greeting.

Easy way to remember:

    Docstring -> Tells WHAT the code does.
    Comment  -> Explains code to the programmer.
"""
