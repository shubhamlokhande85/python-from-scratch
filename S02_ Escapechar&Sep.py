"""


Topic: Escape Sequences, Escape Characters and Separators

======================================================================
1.ESCAPE SEQUENCES
======================================================================

Definition:
Escape sequences are special character combinations used inside
strings to represent characters that have a special meaning.

An escape sequence usually starts with a backslash (\).

Common Escape Sequences:

\n   -> New Line
\t   -> Tab
\\   -> Backslash
\'   -> Single Quote
\"   -> Double Quote
\b   -> Backspace
\r   -> Carriage Return
"""


# ==============================================================
# 1. \n - NEW LINE
# ==============================================================

"""
Definition:
\n moves the following text to a new line.

Example:
"""

print("Hello\nPython")

# Output:
# Hello
# Python


# ==============================================================
# 2. \t - TAB
# ==============================================================

"""
Definition:
\t inserts a horizontal tab space.

Example:
"""

print("Name:\tRahul")

# Output:
# Name:   Rahul


# ==============================================================
# 3. \\ - BACKSLASH
# ==============================================================

"""
Definition:
\\ is used to display a backslash character inside a string.

Example:
"""

print("Python\\Programming")

# Output:
# Python\Programming


# ==============================================================
# 4. \' - SINGLE QUOTE
# ==============================================================

"""
Definition:
\' is used to include a single quote inside a string
created using single quotes.

Example:
"""

print('It\'s Python')

# Output:
# It's Python


# ==============================================================
# 5. \" - DOUBLE QUOTE
# ==============================================================

"""
Definition:
\" is used to include a double quote inside a string
created using double quotes.

Example:
"""

print("He said, \"Hello Python\"")

# Output:
# He said, "Hello Python"


# ==============================================================
# 6. \b - BACKSPACE
# ==============================================================

"""
Definition:
\b moves the cursor one position backward.

Example:
"""

print("Helloo\b")

# Output may appear as:
# Hello


# ==============================================================
# 7. \r - CARRIAGE RETURN
# ==============================================================

"""
Definition:
\r moves the cursor to the beginning of the current line.

When used with print(), text after \r can overwrite the
beginning of the existing text depending on the output environment.

Example:
"""

print("Python\rJava")

# Output commonly appears as:
# Javan

'''
==============================================================
2.SEPARATOR IN PYTHON
==============================================================
'''
"""
Definition:
The sep parameter of the print() function is used to define
the separator between multiple values.

By default:

sep = " "

This means Python places a space between values.

Syntax:

print(value1, value2, value3, sep="separator")

Example:
"""

print("Python", "Java", "C++", sep=" | ")

# Output:
# Python | Java | C++


# ==============================================================
# 8. sep = "-"
# ==============================================================

"""
Definition:
We can use any string as a separator.

Example:
"""

print("2026", "09", "09", sep="-")

# Output:
# 2026-09-09


# ==============================================================
# 9. sep = ","
# ==============================================================

"""
Definition:
A comma can also be used as a separator.

Example:
"""

print("Python", "Java", "C++", sep=",")

# Output:
# Python,Java,C++


"""
======================================================================
3.END PARAMETER
======================================================================

Definition:
The end parameter of the print() function defines what should
be printed at the end of the output.

By default:

end = "\n"

This means print() moves to a new line after displaying the output.

Syntax:

print(value, end="something")

Example:
"""

print("Hello", end=" ")
print("Python")

# Output:
# Hello Python


"""
======================================================================
                    SEP AND END TOGETHER
======================================================================

The sep parameter controls the separator between values.

The end parameter controls what happens after print() finishes.

Example:
"""

print("Python", "Programming", "Language", sep="-", end="!")

# Output:
# Python-Programming-Language!


"""
======================================================================
                         QUICK REVISION
======================================================================

ESCAPE SEQUENCES
----------------

\n   -> New line
\t   -> Tab
\\   -> Backslash
\'   -> Single quote
\"   -> Double quote
\b   -> Backspace
\r   -> Carriage return


PRINT SEPARATORS
----------------

sep
-> Defines the separator between multiple values.

Example:
print("A", "B", "C", sep="-")

Output:
A-B-C


END PARAMETER
-------------

end
-> Defines what is printed after the print() statement.

Default:
end = "\n"

Example:
print("Hello", end=" ")
print("Python")

Output:
Hello Python

"""
