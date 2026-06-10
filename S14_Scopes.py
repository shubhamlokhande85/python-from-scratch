'''A.global scope '''
# - outside function or class which scope we have is global scope
'''1.global variable'''
'''a global variable is variable is defined outside of any
function or class and it can be accessed from anywhere in 
same module(file)'''

'''1,1 method 1 '''
# declaring variable in global scope is global variable 

x = "hello world" # global variable 
def display():
    print(x)
display()
# output - hello world

'''1.2 method 2'''

'''decalaring global variable in local space using 
global keyword it is also global variable '''

def display2():
    global y# its tell python y is now global variable  so we access y outside the function 
    y= "hi I'm shubham " 
display2()

print(y) 

# when you decalear global keyword to varialble in local scope now  even if we have duplicate that 
# variable outside the loacl scope  in previous that value changed now 
# output 
# hi I'm shubham 

'''B.Local scope '''
'''a scope inside the function or class called local scope '''

'''. local variable '''
'''a variable decalared in inside the function or class called local variable '''
def display3():
    z = "I would like to introduce myself and thanks for giving my this oppurtinity"
    print(z)
localz =display3()
'''print(z) ''' # its give error nameError because z in local scope 
#output - NameError: name 'z' is not defined

print(localz)
# output -
# I would like to introduce myself and thanks for giving my this oppurtinity
