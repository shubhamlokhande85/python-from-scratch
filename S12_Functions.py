'''function'''
'''function is a group of statements that are executed together to perform 
specific or particular task'''

'''1. user defined functions'''
# -syntax of fuction
'''def function_name(parameter):
      # block of code to be executed 
    
# -syntax of function call 
    function_name(arguments)'''
    
    
# eg.
def show(): # function defination 
    print("HTML stands for hyper text markup language")
    
show()
# output - HTML stands for hyper text markup language

''' A. parameter'''
'''parameters are input function is designed to accept variable 
passed to the function defination from function call'''

def display(a,b): # here a and b is parameters 
    print(a+b)
display(2,2)
# 4 

'''B.arguments'''
'''arguments are real values that are passed to the function as a parameter  
so it can perform task'''
#eg
def display2(a,b): # here a and b is parameters 
    print(a+b)
display2(2,2) # 2,2 argumnets & its reference to the a and b parameters
# output - 4

''' C . return statement'''
'''it is keyword that return output to the function call '''
# note - function call store the returned output from function to itself

#eg 
def display3(a,b):
    return a-b
result = display3(5,3) # function call store returned output from fuction in function call itself
print(result)
# output  - 2

'''D.Types of arguments'''

'''D.1 . positional arguments '''
'''here values matched to a parameter by its position
in the function calls arguments positon '''

def show1(a,b,c,d):
    print("position of  a",a)
    print("position of  b",b)
    print("position of  c",c)
    print("position of  d",d)

show1(1,2,3,4)
# position of  a 1
# position of  b 2
# position of  c 3
# position of  d 4

'''D.2 . Default arguments '''
'''in this format parameter values are already predefined in function defination as
default values and its executes when arguments values not in fuction call '''
#eg1
def show2(a,b=1,c=4): # a = 5 
    print(a+b+c)
show2(5)
# 10 
# eg2
def show3(a,b=10 ,c=4): # b = 5 --here b=10 default value 
    print(a+b+c)
show3(5,5)
#14

''' D.3 keyword arguments '''
'''in this format arguments passed to function call using parameter name '''
def show4(name,age,qualification):
    print("name:",name)
    print("age:",age)
    print("qualification:", qualification)
    
show4(name="shubham lokhande",age = "24",qualification="Data Engineer")
#here even if make argumnets order unoreded its still work because we specified their name

'''D.4 arbitory or variable-length arguments - *args - (multiple arguments)'''
'''its used when you want a function to accept any numbers of arguments 
without knows how many will be passed'''
'''note 1. * are used to call extra positon arguments for defined position parameter(*z)
        2. output is stored in a tuple'''
     
def show5(y,*z):
    print("y: ",y)
    print("z: ",z)
show5(1,2,3,4,5,6,7,8,9)
# y:  1
# z:  (2, 3, 4, 5, 6, 7, 8, 9)

'''2. predefined functions  '''
'''A. print()'''
'''its prints statements in python and () is denotes starting and ending of statements '''
print() # its print() blank line at teminal 
print("css is stands for cascading style sheets ")
# output
#
# css is stands for cascading style sheets 

'''B.input()'''
'''its used take inputs from user '''
'''input() takes default values as strings '''
name = input("Enter your name :" ) # shubham
print("welcome", name)
# welcome shubham

'''c.len()'''
'''its used measure length of characters for example  string,intger ..etc'''
'''len() return intger value '''
a= "shubham"
print(len(a))
# 7 