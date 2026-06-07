# logical operators 

# A) logical - (and, or , not )

# i) AND 
# its return value when all inputs are true 
# Q.find greatest number
a,b,c=10,20,30 
if a > b and a > c : # false
    print(a,"is greater than",b ,"and",c)
elif b > a and b > c : # false 
    print(b,"is greater than",a, "and",c)
else: # true 
    print(c,"is greater than",a,"and",b)
# output - 30 is greater than 10 and 20

# ii) OR
# its return value when one of the input is true 
# Q.find the number in range or not
num = 100
if num < 100 or num == 100 : # true - num = 100
    print("number is in range of 1 to 100")
else: 
    print("number is not in range of 1 to 100")
 
 # output - number is in range of 1 to 100
 
#  3)NOT 

p = 10
q = 10 
if (not(p==q)): # when input true the return false and when input is false then return true value 
    print(p,"equal",q)
else: 
    print(p,"is not equal to",q)
# output - 10 is not equal to 10


# B) membership operator  -(in , not in )
# its check values exist or not in sequence(list,tuple ..etc)

# i) in 
list1 = [1,2,3,4,5,6,7]
print(7 in list1)
# output - True 

# ii) not in 
print(10 not in list1)
# output - True


# C)identity operator  - (is , is not )
# its checks two variables refer to same objects(memory address) or not
# i) is 
aaa,bbb=10,10 
print(aaa is bbb) 
# output - True 
ccc = 10 
ddd = 30 
print(ccc is not ddd)
# output - True 