"""
PYTHON OPERATORS


Introduction:
Operators are special symbols or keywords used to perform
operations on values and variables.

Example:
a + b

Here, '+' is an operator that adds two values.

Python provides several types of operators:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
"""


"""
------------------------------------------------------------
1. ARITHMETIC OPERATORS
------------------------------------------------------------

Definition:
Arithmetic operators are used to perform mathematical
operations such as addition, subtraction, multiplication,
division, modulus, exponentiation, and floor division.

Operators:
+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulus
**  Exponentiation
//  Floor Division

Simple Example:
"""

a = 10
b = 3

print("\n========== ARITHMETIC OPERATOR ==========")
print("Addition:", a + b)


"""
------------------------------------------------------------
2. ASSIGNMENT OPERATORS
------------------------------------------------------------

Definition:
Assignment operators are used to assign or update values
in variables.

Operators:
=   Assignment
+=  Add and assign
-=  Subtract and assign
*=  Multiply and assign
/=  Divide and assign
%=  Modulus and assign

Simple Example:
"""

x = 10
x += 5

print("\n========== ASSIGNMENT OPERATOR ==========")
print("Value of x:", x)


"""
------------------------------------------------------------
3. COMPARISON OPERATORS
------------------------------------------------------------

Definition:
Comparison operators are used to compare two values.
They return either True or False.

Operators:
==  Equal to
!=  Not equal to
>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to

Simple Example:
"""

age = 20

print("\n========== COMPARISON OPERATOR ==========")
print("Is age greater than 18?", age > 18)


"""
------------------------------------------------------------
4. LOGICAL OPERATORS
------------------------------------------------------------

Definition:
Logical operators are used to combine multiple conditions.

Operators:
and  Returns True if all conditions are True
or   Returns True if at least one condition is True
not  Reverses the result

Simple Example:
"""

age = 20
has_id = True

print("\n========== LOGICAL OPERATOR ==========")
print("Can enter?", age >= 18 and has_id)


"""
------------------------------------------------------------
5. IDENTITY OPERATORS
------------------------------------------------------------

Definition:
Identity operators are used to check whether two variables
refer to the same object in memory.

Operators:
is       Returns True if both refer to the same object
is not   Returns True if they refer to different objects

Simple Example:
"""

a = [1, 2]
b = a

print("\n========== IDENTITY OPERATOR ==========")
print("Are a and b the same object?", a is b)


"""
------------------------------------------------------------
6. MEMBERSHIP OPERATORS
------------------------------------------------------------

Definition:
Membership operators are used to check whether a value
exists inside a sequence such as a list, tuple, string, etc.

Operators:
in      Returns True if the value exists
not in  Returns True if the value does not exist

Simple Example:
"""

fruits = ["Apple", "Banana", "Mango"]

print("\n========== MEMBERSHIP OPERATOR ==========")
print("Is Apple present?", "Apple" in fruits)


"""
------------------------------------------------------------
7. BITWISE OPERATORS
------------------------------------------------------------

Definition:
Bitwise operators perform operations on the binary
representation of numbers.

Operators:
&   AND
|   OR
^   XOR
~   NOT
<<  Left Shift
>>  Right Shift

Simple Example:
"""

a = 5
b = 3

print("\n========== BITWISE OPERATOR ==========")
print("Bitwise AND:", a & b)


"""
============================================================
                    QUICK REVISION
============================================================

Arithmetic
-> Used for mathematical calculations
-> Example: 10 + 3

Assignment
-> Used to assign/update values
-> Example: x += 5

Comparison
-> Used to compare values
-> Example: 10 > 5

Logical
-> Used to combine conditions
-> Example: age >= 18 and has_id

Identity
-> Used to compare object identity
-> Example: a is b

Membership
-> Used to check whether a value exists
-> Example: "Apple" in fruits

Bitwise
-> Used to perform operations on binary values
-> Example: 5 & 3


"""
