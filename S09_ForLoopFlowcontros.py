'''loops'''
'''1.For loops'''
''' it is used when you know how many
times you want to repeat something'''

# syntax
'''for variable in sequence : 
       #block of code to be excecuted'''
       
# eg.1 list
fruits = ["apples","mangoes","oranges","stroberries"]

for i in fruits :
    print(i)
    
# outputs -
# apples
# mangoes
# oranges
# stroberries

# eg.2 tuple
furniture = ("table","desk",1,(8+9j),"mat",)
for i in furniture:
    print(i)
# output -
# table
# desk
# 1
# (8+9j)
# mat

#eg.3 sets 

market = {"PE","Stocks","buy","sell","funds"}
# set are unordered 
for i in market:
    print(i)
#output - 
# PE
# funds
# sell
# buy
# Stocks

'''1.1 range()'''
'''the range function used to generate sequence of numbers 
usually when you want to run a loop a specific number of times '''

# types of ranges
'''a. range(0,stop)''' # its also range(stop)
for i in range(11): # here is 11 - because last 
# item of range not included in result set
    print(i)
# output - 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

'''b.range(start, stop)'''
for i in range (30 , 41):
    print(i)
    
# 31
# 32
# 33
# 34
# 35
# 36
# 37
# 38
# 39
# 40

'''c. range(start,stop,step)'''
# here step is used to increament in sequence 
# and if step is negative then decrement in sequence here we have set start values big and stop values is small to occure decrement 
 
for i in range(1, 11 , 2):
    print(i)
#output -
# 1
# 3
# 5
# 7
# 9
for i in range(11, 0, -2):
    print(i)
# output - 
# 9
# 7
# 5
# 3
# 1