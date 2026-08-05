'Enumerate Function '
'''
-enumerate() is a function that returns both the index and the value of 
 each element while looping through a sequence
 
-The enumerate() function is a built-in Python function that adds an index 
 (position number) to each item in a list, tuple, string, or any iterable. 
 It is useful when you need both the item and its position while using a loop
 
-Advantages of enumerate()
 Gives both index and value at the same time.
 Makes code shorter and easier to read.
 Eliminates the need to manually increase an index variable.
 Works with lists, tuples, strings, and other iterables

-Syntax

enumerate(iterable, start=0)

where,
iterable         - The list, tuple, string, or other collection to loop through.
start (optional) - The starting value of the index. By default, it starts from 0
'''

#Eg 01

tools=["pen","Notebook","keyboard","Mouse"]

for index , tool in  enumerate((tools)):
    print(index,tool)
    
    
'Output'   
# 0 pen
# 1 Notebook
# 2 keyboard
# 3 Mouse


#Eg 02 

for index, tool in enumerate(tools,start=1):
    print(index,tool)

'Output'
# 1 pen
# 2 Notebook
# 3 keyboard
# 4 Mouse
