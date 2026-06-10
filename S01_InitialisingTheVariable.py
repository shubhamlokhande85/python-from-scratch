
'''The proficient programmer is who write code in short 
 and with powerful logic and also most meaningful program'''



# types of initilize variables in python
#1.one value and many variables 
a=b=c=d=100
print(a)
print(b)
print(c)
print(d)

#2.many values many variables 

e,f,g,h=100,"shubahm","vidya",(8+9j)
print(e)
print(f)
print(g)
print(h)

#3.value unpacks

l = [1,"parthiksha", "ashiwini","dhanashri"]
i,j,k,n=l
print(i)
print(j)
print(k)
print(n)

#4.id - its shows memory address of variables
print(id(a))
print(id(b))



#5.type - its shows of datatype of variable
print(type(a))
print(type(h))

#6.rules to intialise variables legal way
# 1) never start the variables with numbers - 1234= 
# 2) never give space in variable - hello world - insted of we can use hello_world or HelloWorld (camel method)
# 3) write variable in small letter - SPAM= - insted of spam=
#4) dont use special character as variable like class- as - if - else -