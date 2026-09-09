"""
Topic: String Slicing in Python

======================================================================
                       STRING SLICING
======================================================================

Definition:
String slicing is used to extract a portion of a string.

Python uses indexes to access characters from a string.

Syntax:

string[start:end]

The start index is included.
The end index is excluded.

Example:

String:   Python
Index:    0 1 2 3 4 5
Negative: -6 -5 -4 -3 -2 -1

======================================================================
"""


# ==============================================================
# 1. BASIC SLICING
# ==============================================================

"""
Definition:
Basic slicing extracts characters from a starting index
up to, but not including, the ending index.

Syntax:

string[start:end]

Example:
"""

text = "Python"

print("\n========== BASIC SLICING ==========")
print(text[0:3])

# Output:
# Pyt


# ==============================================================
# 2. SLICING FROM BEGINNING
# ==============================================================

"""
Definition:
If the start index is omitted, Python starts slicing
from the beginning of the string.

Syntax:

string[:end]

Example:
"""

text = "Python"

print("\n========== SLICING FROM BEGINNING ==========")
print(text[:3])

# Output:
# Pyt


# ==============================================================
# 3. SLICING TO THE END
# ==============================================================

"""
Definition:
If the end index is omitted, Python continues slicing
until the end of the string.

Syntax:

string[start:]

Example:
"""

text = "Python"

print("\n========== SLICING TO THE END ==========")
print(text[2:])

# Output:
# thon


# ==============================================================
# 4. COPYING A STRING
# ==============================================================

"""
Definition:
Using [:] creates a slice containing the complete string.

Syntax:

string[:]

Example:
"""

text = "Python"

print("\n========== COPYING A STRING ==========")
print(text[:])

# Output:
# Python


# ==============================================================
# 5. NEGATIVE INDEX SLICING
# ==============================================================

"""
Definition:
Negative indexes allow us to access characters from
the end of the string.

Example:

String:    P  y  t  h  o  n
Negative: -6 -5 -4 -3 -2 -1
"""

text = "Python"

print("\n========== NEGATIVE INDEX SLICING ==========")
print(text[-4:-1])

# Output:
# tho


# ==============================================================
# 6. SLICING WITH STEP
# ==============================================================

"""
Definition:
The step value determines how many positions Python
moves while slicing.

Syntax:

string[start:end:step]

Example:
"""

text = "Python"

print("\n========== SLICING WITH STEP ==========")
print(text[0:6:2])

# Output:
# Pto


# ==============================================================
# 7. SLICING WITH STEP 1
# ==============================================================

"""
Definition:
A step of 1 moves through every character.

Syntax:

string[start:end:1]

Example:
"""

text = "Python"

print("\n========== STEP 1 ==========")
print(text[0:6:1])

# Output:
# Python


# ==============================================================
# 8. SLICING WITH STEP 2
# ==============================================================

"""
Definition:
A step of 2 skips every second character.

Example:
"""

text = "Python"

print("\n========== STEP 2 ==========")
print(text[0:6:2])

# Output:
# Pto


# ==============================================================
# 9. SLICING WITH NEGATIVE STEP
# ==============================================================

"""
Definition:
A negative step moves through the string from right to left.

Example:
"""

text = "Python"

print("\n========== NEGATIVE STEP ==========")
print(text[::-1])

# Output:
# nohtyP


# ==============================================================
# 10. REVERSE A STRING
# ==============================================================

"""
Definition:
[::-1] is a common slicing technique used to reverse
a string.

Syntax:

string[::-1]

Example:
"""

text = "Python"

print("\n========== REVERSE STRING ==========")
print(text[::-1])

# Output:
# nohtyP


# ==============================================================
# 11. FIRST THREE CHARACTERS
# ==============================================================

"""
Definition:
The first three characters can be obtained by using
a slice from index 0 to index 3.

Example:
"""

text = "Programming"

print("\n========== FIRST THREE CHARACTERS ==========")
print(text[:3])

# Output:
# Pro


# ==============================================================
# 12. LAST THREE CHARACTERS
# ==============================================================

"""
Definition:
Negative indexing can be used to extract characters
from the end of a string.

Example:
"""

text = "Programming"

print("\n========== LAST THREE CHARACTERS ==========")
print(text[-3:])

# Output:
# ing


# ==============================================================
# 13. SKIP CHARACTERS
# ==============================================================

"""
Definition:
A step greater than 1 can be used to skip characters
while slicing.

Example:
"""

text = "Programming"

print("\n========== SKIP CHARACTERS ==========")
print(text[0:11:2])

# Output:
# Pormig


# ==============================================================
#                    SLICING QUICK CHART
# ==============================================================

"""
======================================================================
                       STRING SLICING CHART
======================================================================

Syntax                  Meaning
----------------------------------------------------------------------

string[start:end]       Start to end - 1

string[:end]            Beginning to end - 1

string[start:]          Start to the end

string[:]               Complete string

string[start:end:step]  Slicing with step

string[::-1]            Reverse the string

string[-3:]             Last three characters

string[:3]              First three characters

======================================================================
"""


"""
======================================================================
                         IMPORTANT RULES
======================================================================

1. String indexes start from 0.

2. The start index is included.

3. The end index is excluded.

4. Negative indexes start from the end.

5. The default step is 1.

6. A negative step moves from right to left.

7. String slicing does not modify the original string.

======================================================================
"""


# ==============================================================
#                    FINAL PRACTICE EXAMPLE
# ==============================================================

"""
This example combines start, end, and step in one slice.
"""

text = "PythonProgramming"

result = text[0:16:2]

print("\n========== FINAL SLICING EXAMPLE ==========")
print("Original:", text)
print("Sliced:", result)


"""
======================================================================
                         QUICK REVISION
======================================================================

Indexing:
-> Accesses one character.
-> Example: text[0]

Slicing:
-> Extracts multiple characters.
-> Example: text[0:3]

Step:
-> Controls how characters are selected.
-> Example: text[0:6:2]

Negative Index:
-> Accesses characters from the end.
-> Example: text[-1]

Reverse:
-> Reverses a string.
-> Example: text[::-1]

"""
