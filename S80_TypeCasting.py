"""


Topic: Type Casting in Python

Two Types of Type Casting
1.IMPLICIT TYPE CASTING
2.EXPLICIT TYPE CASTING


======================================================================
1.IMPLICIT TYPE CASTING
======================================================================

Definition:
Implicit type casting occurs automatically when Python converts
one data type into another without the programmer explicitly
performing the conversion.

Python usually converts a smaller or less precise numeric type
into a larger or more precise numeric type when required.

Example:
"""

number = 10
decimal = 2.5

result = number + decimal

print("\n========== IMPLICIT TYPE CASTING ==========")
print("Result:", result)
print("Type:", type(result))

# Output:
# Result: 12.5
# Type: <class 'float'> 



"""
======================================================================
2.EXPLICIT TYPE CASTING
======================================================================

Definition:
Explicit type casting occurs when the programmer manually converts
one data type into another using functions such as:

int()
float()
str()
bool()
list()
tuple()
set()

Example:
"""

age = "20"

age = int(age)

print("\n========== EXPLICIT TYPE CASTING ==========")
print("Age:", age)
print("Type:", type(age))

"""


======================================================================
TYPE CASTING
======================================================================

Definition:
Type Casting is the process of converting a value from one data type
to another data type.

Python provides built-in functions for type casting.

Common Type Casting Functions:

int()     -> Converts a value to an integer
float()   -> Converts a value to a floating-point number
str()     -> Converts a value to a string
bool()    -> Converts a value to a Boolean
list()    -> Converts a value to a list
tuple()   -> Converts a value to a tuple
set()     -> Converts a value to a set

======================================================================
"""


# ==============================================================
# 1. int()
# ==============================================================

"""
Definition:
int() converts a compatible value into an integer.

Syntax:
int(value)

Example:
"""

number = "25"

result = int(number)

print("\n========== int() ==========")
print("Original Value:", number)
print("Converted Value:", result)
print("Type:", type(result))

# Output:
# Original Value: 25
# Converted Value: 25
# Type: <class 'int'>


# ==============================================================
# 2. float()
# ==============================================================

"""
Definition:
float() converts a compatible value into a floating-point number.

Syntax:
float(value)

Example:
"""

number = "25.5"

result = float(number)

print("\n========== float() ==========")
print("Original Value:", number)
print("Converted Value:", result)
print("Type:", type(result))

# Output:
# Original Value: 25.5
# Converted Value: 25.5
# Type: <class 'float'>


# ==============================================================
# 3. str()
# ==============================================================

"""
Definition:
str() converts a value into a string.

Syntax:
str(value)

Example:
"""

number = 100

result = str(number)

print("\n========== str() ==========")
print("Original Value:", number)
print("Converted Value:", result)
print("Type:", type(result))

# Output:
# Original Value: 100
# Converted Value: 100
# Type: <class 'str'>


# ==============================================================
# 4. bool()
# ==============================================================

"""
Definition:
bool() converts a value into a Boolean value.

The result will be either:
True
False

Example:
"""

number = 10

result = bool(number)

print("\n========== bool() ==========")
print("Original Value:", number)
print("Converted Value:", result)
print("Type:", type(result))

# Output:
# Original Value: 10
# Converted Value: True
# Type: <class 'bool'>


# ==============================================================
# 5. list()
# ==============================================================

"""
Definition:
list() converts an iterable into a List.

Example:
"""

text = "Python"

result = list(text)

print("\n========== list() ==========")
print("Original Value:", text)
print("Converted Value:", result)
print("Type:", type(result))

# Output:
# Original Value: Python
# Converted Value: ['P', 'y', 't', 'h', 'o', 'n']
# Type: <class 'list'>


# ==============================================================
# 6. tuple()
# ==============================================================

"""
Definition:
tuple() converts an iterable into a Tuple.

Example:
"""

numbers = [10, 20, 30]

result = tuple(numbers)

print("\n========== tuple() ==========")
print("Original Value:", numbers)
print("Converted Value:", result)
print("Type:", type(result))

# Output:
# Original Value: [10, 20, 30]
# Converted Value: (10, 20, 30)
# Type: <class 'tuple'>


# ==============================================================
# 7. set()
# ==============================================================

"""
Definition:
set() converts an iterable into a Set.

Duplicate values are automatically removed.

Example:
"""

numbers = [10, 20, 20, 30]

result = set(numbers)

print("\n========== set() ==========")
print("Original Value:", numbers)
print("Converted Value:", result)
print("Type:", type(result))

# Output:
# Original Value: [10, 20, 20, 30]
# Converted Value: {10, 20, 30}
# Type: <class 'set'>


"""
======================================================================
                         QUICK REVISION
======================================================================

Type Casting
-> Converting one data type into another.

Common Functions:

int()
-> Converts to integer

float()
-> Converts to float

str()
-> Converts to string

bool()
-> Converts to Boolean

list()
-> Converts to list

tuple()
-> Converts to tuple

set()
-> Converts to set


Two Types of Type Casting:

1. Explicit Type Casting
   -> Done manually by the programmer.

2. Implicit Type Casting
   -> Done automatically by Python.

"""
