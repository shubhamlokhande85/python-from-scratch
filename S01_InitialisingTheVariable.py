'                                     Welcome! To __python_from_scratch__ Repository                                           '  

                          
'''
Here we will learn python from beginning ,
A proficient programmer is someone who writes short, meaningful programs with powerful logic.
let dive in it ! Happy Coding! 🚀 
'''


'1.Variable'

'''
-A variable in Python is a name used to store data or values in a program. The value stored 
in a variable can be changed during program execution


'''

'A.rules to intialise variables in python '

'''
# 1) Never start the variables with numbers - 1234= 
# 2) Never give space in variable - hello world - insted of we can use hello_world or HelloWorld (camel method)
# 3) Write variable in small letter - SPAM= - insted of spam=
# 4) Dont use special character as variable like class- as - if - else -
# 5) Always give meaningful name to variable, to specifiy what actual that variable contained
'''
# Eg
intro = "Hello World! Welcome"
print(intro)

'B.Types of initilize variables in python'

'#1.one value and many variables '
a=b=c=d=100
print(a)
print(b)
print(c)
print(d)
# 100
# 100
# 100
# 100


'#2.many values many variables '

e,f,g,h=100,"shubahm","vidya",(8+9j)
print(e)
print(f)
print(g)
print(h)
# 100
# shubahm
# vidya
# (8+9j)


'#3.value unpacks'

l = [1,"parthiksha", "ashiwini","dhanashri"]
i,j,k,n=l
print(i)
print(j)
print(k)
print(n)
# 1
# parthiksha
# ashiwini
# dhanashri

'#4.id - its shows memory address of variables'
print(id(a))
print(id(b))
# 140714182283480
# 140714182283480


'#5.type - its shows of datatype of variable'
print(type(a))
print(type(h))
# <class 'int'>
# <class 'complex'>
