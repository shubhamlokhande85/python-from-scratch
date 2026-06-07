'''conditonal statement'''
# types of conditional statement
'''1. simple if statement'''
a , b = 10 ,10 
if a == b : 
    print(a ,"is Equal", b)

# output - 10 is Equal 10
    
    
if a > b : 
    print(a,"is greater b ", b)    

# output - blank screen cause condition is false 


''' 2.if-else statement'''

c , d = 10 , 20
if c >= d : 
    print(c,"is greater than", d)
else: 
    print( d ,"is greater than", c)
# output - 20 is greater than 10

'''3.elif - else if  or elif ladder'''
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

''' 4.Nested if statements'''
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