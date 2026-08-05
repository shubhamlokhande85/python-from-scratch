'a.1. List Comprehension'

''''
-List comprehension is a method of creating a new list in one line by using 
 a loop and, if needed, a condition
-List comprehension is a short and easy way to create a new list from an
 existing list or another iterable using a single line of code. It makes
 programs shorter, cleaner, and easier to read
 
 
-Syntax
1) without condition
new_list = [expression for item in iterable]

2) with condition 
new_list = [expression for item in iterable if condition]

where,
expression              - The value to add to the new list.
item                    - Each element taken from the original list.
iterable                - The list, tuple, or other collection being processed.
if condition (optional) - Filters items before adding them to the new list
'''

#Eg 01 without condition list comprehension example 

numbers=[1,2,3,4,5,6,7,8]

multi=[x*x  for  x  in  numbers ]

print(multi)

#[1, 4, 9, 16, 25, 36, 49, 64]

#Eg 02 with condition list comprehension example 

even_num=[ x  for x in numbers if  x%2==0]

print(even_num)

# [2, 4, 6, 8]