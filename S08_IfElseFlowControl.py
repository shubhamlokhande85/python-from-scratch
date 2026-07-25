'''
conditonal statement
-A conditional statement in Python is a statement that allows a program to make decisions
based on whether a condition is True or False
-
| Conditional Statement        | Meaning                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------- |
| `if`                         | Executes a block of code only when the condition is **True**                    |
| `if-else`                    | Executes one block if the condition is **True**, otherwise another block        |
| `if-elif-else` (elif ladder) | Checks **multiple conditions** one by one and executes the first true condition |
| **Nested if**                | An **if statement inside another if statement** to check multiple conditions    |

'''
# types of conditional statement

'''1. simple if statement
-An if statement in Python is a conditional statement that executes a block of code only when 
a given condition is True'''
#eg
a , b = 10 ,10 
if a == b : 
    print(a ,"is Equal", b)

# output - 10 is Equal 10
    
    
if a > b : 
    print(a,"is greater b ", b)    

# output - blank screen cause condition is false 


''' 2.if-else statement
-An if-else statement in Python is a conditional statement that executes one block of code
when a condition is True and another block of code when the condition is False'''

#eg
c , d = 10 , 20
if c >= d : 
    print(c,"is greater than", d)
else: 
    print( d ,"is greater than", c)
# output - 20 is greater than 10

'''3.elif - else if  or elif ladder
-An elif ladder (else-if ladder) in Python is a conditional statement used to check multiple
conditions one by one. If the first condition is false, it checks the next condition until it 
finds a true condition'''

#eg
aa,bb,cc,dd=10,20,85,44
if aa >bb and aa>cc and aa >dd :
    print(aa,"is geater than",bb,cc,"and",dd)
elif bb > aa and bb >cc and bb > dd:
    print(bb,"is greater than",aa,cc,"and",dd)
elif cc > aa and cc > bb and cc > dd:
    print(cc,"is greater than",aa,bb,"and",dd)
else:
    print(dd,"is greater than",aa,bb,"and",cc)

# output - 85 is greater than 10 20 and 44

''' 4.Nested if statements
A nested if statement in Python is an if statement placed inside another if statement.
It is used when we need to check a second condition only after the first condition is true'''
#eg
num = int(input("Enter the any Number: "))
if num > 0 : 
    print(num,"is Positive Number")
    if num % 2 == 0 :
        print(num,"is Even Number")
    else:
        print(num,"is Odd Number")
else:
    print(num,"is Negative Number")
    
# output  - 10 is Positive Number
#           10 is Even Number