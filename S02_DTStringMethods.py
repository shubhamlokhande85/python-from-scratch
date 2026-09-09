"""
STRING IN PYTHON


Definition:
A String is a sequence of characters used to represent text in Python.

A string can contain:
- Letters
- Numbers
- Spaces
- Special characters
- Symbols

Strings can be created using:
- Single quotes     -> 'Hello'
- Double quotes     -> "Hello"
- Triple quotes     -> '''Hello''' 

- Strings are immutable.
- This means an existing string cannot be changed directly.

======================================================================
"""


# ==============================================================
# 1. STRING CREATION
# ==============================================================

"""
Definition:
String creation means storing text inside a variable using
single quotes, double quotes, or triple quotes.

Example:
"""

name = "Python"

print("\n========== STRING CREATION ==========")
print("String:", name)
print("Type:", type(name))


# ==============================================================
# 2. len()
# ==============================================================

"""
Definition:
len() returns the total number of characters in a string.

Syntax:
len(string)

Example:
"""

text = "Python"

print("\n========== len() ==========")
print("Length:", len(text))

# Output:
# Length: 6


# ==============================================================
# 3. upper()
# ==============================================================

"""
Definition:
upper() converts all alphabetic characters in a string
to uppercase.

Syntax:
string.upper()

Example:
"""

text = "python"

print("\n========== upper() ==========")
print("Uppercase:", text.upper())

# Output:
# Uppercase: PYTHON


# ==============================================================
# 4. lower()
# ==============================================================

"""
Definition:
lower() converts all alphabetic characters in a string
to lowercase.

Syntax:
string.lower()

Example:
"""

text = "PYTHON"

print("\n========== lower() ==========")
print("Lowercase:", text.lower())

# Output:
# Lowercase: python


# ==============================================================
# 5. capitalize()
# ==============================================================

"""
Definition:
capitalize() converts the first character of a string
to uppercase and the remaining characters to lowercase.

Syntax:
string.capitalize()

Example:
"""

text = "python programming"

print("\n========== capitalize() ==========")
print("Result:", text.capitalize())

# Output:
# Result: Python programming


# ==============================================================
# 6. title()
# ==============================================================

"""
Definition:
title() converts the first character of each word
to uppercase.

Syntax:
string.title()

Example:
"""

text = "python programming language"

print("\n========== title() ==========")
print("Result:", text.title())

# Output:
# Result: Python Programming Language


# ==============================================================
# 7. swapcase()
# ==============================================================

"""
Definition:
swapcase() converts uppercase characters to lowercase
and lowercase characters to uppercase.

Syntax:
string.swapcase()

Example:
"""

text = "Python Programming"

print("\n========== swapcase() ==========")
print("Result:", text.swapcase())

# Output:
# Result: pYTHON pROGRAMMING


# ==============================================================
# 8. strip()
# ==============================================================

"""
Definition:
strip() removes spaces or specified characters from
both the beginning and the end of a string.

Syntax:
string.strip()

Example:
"""

text = "  Python  "

print("\n========== strip() ==========")
print("Result:", text.strip())

# Output:
# Result: Python


# ==============================================================
# 9. lstrip()
# ==============================================================

"""
Definition:
lstrip() removes spaces or specified characters from
the left side of a string.

Syntax:
string.lstrip()

Example:
"""

text = "  Python"

print("\n========== lstrip() ==========")
print("Result:", text.lstrip())

# Output:
# Result: Python


# ==============================================================
# 10. rstrip()
# ==============================================================

"""
Definition:
rstrip() removes spaces or specified characters from
the right side of a string.

Syntax:
string.rstrip()

Example:
"""

text = "Python  "

print("\n========== rstrip() ==========")
print("Result:", text.rstrip())

# Output:
# Result: Python


# ==============================================================
# 11. center()
# ==============================================================

"""
Definition:
center() returns a string centered within a specified width.

Syntax:
string.center(width)

Example:
"""

text = "Python"

print("\n========== center() ==========")
print(text.center(20, "-"))

# Output:
# -------Python-------


# ==============================================================
# 12. count()
# ==============================================================

"""
Definition:
count() returns the number of times a specified value
occurs in a string.

Syntax:
string.count(value)

Example:
"""

text = "Python is easy. Python is powerful."

print("\n========== count() ==========")
print("Python Count:", text.count("Python"))

# Output:
# Python Count: 2


# ==============================================================
# 13. find()
# ==============================================================

"""
Definition:
find() searches for a specified value and returns
its first position (index).

If the value is not found, it returns -1.

Syntax:
string.find(value)

Example:
"""

text = "Python Programming"

print("\n========== find() ==========")
print("Position:", text.find("Programming"))

# Output:
# Position: 7


# ==============================================================
# 14. index()
# ==============================================================

"""
Definition:
index() searches for a specified value and returns
its first position (index).

If the value is not found, index() raises a ValueError.

Syntax:
string.index(value)

Example:
"""

text = "Python Programming"

print("\n========== index() ==========")
print("Position:", text.index("Programming"))

# Output:
# Position: 7


# ==============================================================
# 15. replace()
# ==============================================================

"""
Definition:
replace() replaces one value with another value
inside a string.

Syntax:
string.replace(old, new)

Example:
"""

text = "I like Python"

print("\n========== replace() ==========")
print("Result:", text.replace("Python", "Java"))

# Output:
# Result: I like Java


# ==============================================================
# 16. startswith()
# ==============================================================

"""
Definition:
startswith() checks whether a string starts with
a specified value.

It returns True or False.

Syntax:
string.startswith(value)

Example:
"""

text = "Python Programming"

print("\n========== startswith() ==========")
print("Starts with Python?:", text.startswith("Python"))

# Output:
# Starts with Python?: True


# ==============================================================
# 17. endswith()
# ==============================================================

"""
Definition:
endswith() checks whether a string ends with
a specified value.

It returns True or False.

Syntax:
string.endswith(value)

Example:
"""

text = "Python Programming"

print("\n========== endswith() ==========")
print("Ends with Programming?:", text.endswith("Programming"))

# Output:
# Ends with Programming?: True


# ==============================================================
# 18. isalpha()
# ==============================================================

"""
Definition:
isalpha() checks whether all characters in a string
are alphabetic characters.

It returns True or False.

Syntax:
string.isalpha()

Example:
"""

text = "Python"

print("\n========== isalpha() ==========")
print("Is Alphabetic?:", text.isalpha())

# Output:
# Is Alphabetic?: True


# ==============================================================
# 19. isdigit()
# ==============================================================

"""
Definition:
isdigit() checks whether all characters in a string
are digits.

It returns True or False.

Syntax:
string.isdigit()

Example:
"""

text = "12345"

print("\n========== isdigit() ==========")
print("Is Digit?:", text.isdigit())

# Output:
# Is Digit?: True


# ==============================================================
# 20. isnumeric()
# ==============================================================

"""
Definition:
isnumeric() checks whether all characters in a string
are numeric characters.

It returns True or False.

Syntax:
string.isnumeric()

Example:
"""

text = "12345"

print("\n========== isnumeric() ==========")
print("Is Numeric?:", text.isnumeric())

# Output:
# Is Numeric?: True


# ==============================================================
# 21. isalnum()
# ==============================================================

"""
Definition:
isalnum() checks whether all characters in a string
are alphabetic or numeric characters.

It returns True or False.

Syntax:
string.isalnum()

Example:
"""

text = "Python123"

print("\n========== isalnum() ==========")
print("Is Alphanumeric?:", text.isalnum())

# Output:
# Is Alphanumeric?: True


# ==============================================================
# 22. isspace()
# ==============================================================

"""
Definition:
isspace() checks whether all characters in a string
are whitespace characters.

It returns True or False.

Syntax:
string.isspace()

Example:
"""

text = "   "

print("\n========== isspace() ==========")
print("Contains Only Spaces?:", text.isspace())

# Output:
# Contains Only Spaces?: True


# ==============================================================
# 23. isprintable()
# ==============================================================

"""
Definition:
isprintable() checks whether all characters in a string
are printable characters.

It returns True or False.

Syntax:
string.isprintable()

Example:
"""

text = "Python"

print("\n========== isprintable() ==========")
print("Is Printable?:", text.isprintable())

# Output:
# Is Printable?: True


# ==============================================================
# 24. split()
# ==============================================================

"""
Definition:
split() divides a string into multiple parts and returns
the result as a List.

By default, split() separates the string using whitespace.

Syntax:
string.split()

Example:
"""

text = "Python is easy"

print("\n========== split() ==========")
print("Result:", text.split())

# Output:
# Result: ['Python', 'is', 'easy']


# ==============================================================
# 25. join()
# ==============================================================

"""
Definition:
join() joins multiple strings together using a specified
separator.

Syntax:
separator.join(iterable)

Example:
"""

words = ["Python", "is", "easy"]

print("\n========== join() ==========")
print("Result:", " ".join(words))

# Output:
# Result: Python is easy


# ==============================================================
#                    STRING OPERATORS
# ==============================================================

"""
String operators are used to perform operations on strings.

+       Concatenation
*       Repetition
in      Membership
not in  Membership
"""


# ==============================================================
# 26. + STRING CONCATENATION
# ==============================================================

"""
Definition:
The + operator joins two or more strings together.

Example:
"""

first_name = "Rahul"
last_name = "Patil"

print("\n========== STRING CONCATENATION ==========")
print(first_name + " " + last_name)

# Output:
# Rahul Patil


# ==============================================================
# 27. * STRING REPETITION
# ==============================================================

"""
Definition:
The * operator repeats a string a specified number of times.

Example:
"""

text = "Hi "

print("\n========== STRING REPETITION ==========")
print(text * 3)

# Output:
# Hi Hi Hi


# ==============================================================
# 28. in OPERATOR
# ==============================================================

"""
Definition:
The in operator checks whether a value exists inside
a string.

It returns True or False.

Example:
"""

text = "Python Programming"

print("\n========== in OPERATOR ==========")
print("Python" in text)

# Output:
# True


# ==============================================================
# 29. not in OPERATOR
# ==============================================================

"""
Definition:
The not in operator checks whether a value does not
exist inside a string.

It returns True or False.

Example:
"""

text = "Python Programming"

print("\n========== not in OPERATOR ==========")
print("Java" not in text)

# Output:
# True


"""
======================================================================
                         QUICK REVISION
======================================================================

String Basics:
- String Creation
- Indexing
- Slicing
- Concatenation
- Repetition
- Membership
- String Methods

Formatting:
- upper()
- lower()
- capitalize()
- title()
- swapcase()

Whitespace:
- strip()
- lstrip()
- rstrip()
- center()

Searching:
- count()
- find()
- index()

Modification:
- replace()

Checking:
- startswith()
- endswith()
- isalpha()
- isdigit()
- isnumeric()
- isalnum()
- isspace()
- isprintable()

Splitting and Joining:
- split()
- join()

Operators:
- +
- *
- in
- not in


"""
