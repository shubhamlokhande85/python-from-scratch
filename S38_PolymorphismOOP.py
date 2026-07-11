'POLYMORPHISM'
'same method can behave differently '
'''
-It means one name many forms
-It refers to the occurence of something in multiple forms it is the ability
in object oriented programming where a single function, method or operator can
exist in multiple form and behave differently depending on the situation'
-Type of Polymorphism
1.compile-time polymorphism
2.run-time polymorphism
'''
'1.compile-time polymorphism'
'''
-Types of compile-time polymorphism
A.Compile Method overloading 
B.Compile Operator overloading '''

'A.Compile Method Overloading'
'''
-It work with class - (same name methods)
- IMP - it mean same name method but different parameter and their different operations
-It defining multiple methods with the same name but different number of parameter of different
types of parameter
-Python does support Method overloading but it can be achieved using "MULTIPLEDISPATCH" pre-defined
library which allows multiple methods with the same name but different parameter tupes
-in Python by default the last defined method is called because ealier ones are overwritten that 
mean only last one method is executed'''

'To execute all same name methods'
#eg 01 
from multipledispatch import dispatch
class test:
    @dispatch(float,float) # datatype for methods parameter 
    def product(self,a,b):
        print("product of ",a,"and",b,"is",a*b)
        
    @dispatch(int,int,int)
    def product(self,c,d,e):
        print("product of ",c,"x",d,"and",e,"is",c*d*e)
        
    @dispatch(float,int,float,int)
    def product(self,f,g,h,i):
        print("product of ",f,"x",g,"x",h,"and",i,"is",f*g*h*i)
    
    @dispatch(int, float,int,float,int)
    def product(self,j,k,l,m,n):
        print("product of ",j,"x",k,"x",l,"x",m,"and",n,"is",j*k*l*m*n)
        
t=test()
t.product(12.5,12.5)
t.product(111,112,113)
t.product(5.5,700,4.4,800)
t.product(1200,2.2,1300,3.3,1400)
#output
# product of  12.5 and 12.5 is 156.25
# product of  111 x 112 and 113 is 1404816
# product of  5.5 x 700 x 4.4 and 800 is 13552000.0
# product of  1200 x 2.2 x 1300 x 3.3 and 1400 is 15855840000.0
'NOTES'
'''
-We use @dispatch (from multipledispatch library) to implement method overloading in python
cause python cannot support Method Overloading directly
-@dispatch helps difine multiple methods with the same name 
but different parameter types or numbers
-It tells python to "choose the correct method based on arguments passed '''

'B.Compile Operator Overloading'
'''
-It work with object - (same name objects)
-Operator overloading it means giving a new meaning to an existing operator so it can work 
with objects of a class just like it works with normal datatypes 
-Operator overloading is used with 
the same operator but it performs different operations on different objects.
-IMP - Same operator can be used with objects of the same class (or different classes) by defining its behavior 
'''
# eg 01 
class number:
    def __init__(self,value): # value = 10 
        self.value=value  # 
    
    # Overloading  + operator 
    
    def __add__(self,other):
        return number(self.value+other.value)
    
n1=number(10)
print(n1.value)
n2=number(20)
print(n2.value)
n3=n1+n2
print(n3.value)

#eg 02 with explanation 

class boxes : 
    def __init__(self,value ):  # b1.value = 10 when first object created
        self.value =value       # b2.value = 20 when second object created
        #b1.value = 10 
        #b2.value = 20 
        
    def __add__(self,other):  # self = b1 , other = b2 
        # __add__() only trigger when two objects using + operator  (b3 = b1 + b2)
        return boxes(self.value+other.value) # boxes(b1.value + b2.value)
     
b1=boxes(10)
print(b1.value)
b2=boxes(20)
print(b2.value)
b3=b1+b2  # python converts it b1__add__(b2 ) or __add__(b1,b2)
# __add__() only trigger when two objects using + operator 
print(b3.value)
    
    
'B.run-time polymorphism'
'Types of run - time polymorphism'

'1.Run Method Overloading'
'''
It is a feature of object oriented programming in which a child class provides a new implementation
of a method that already defined in the parent class
- IMP - here parent class method is  overwritten in child class in that case the child class method is executed - (inheritance)'''

'syntax'
class parent : 
    def method_name(self,parameter):
        # parent class implementation
        pass
        
class child(parent):
    def method_name(self , parameter):
        # overwritten metod in child class
        pass
    
#eg  01
class base:
    def display(self):
        print("HTML is hyper text markup language")
class derived(base):
    def display(self):
        print("CSS is stand for Cascading style sheet")
        
d=derived()
d.display()
# CSS is stand for Cascading style sheet


'2.Duck typing '
'''
-Duck Typing is a feature of Python where the type of an object does not matter. 
If an object has the required method or behavior, Python allows it to be used.
-IMP - here differnt class work with same method  (no inheritance)'''


# eg 01 
class Dog:
    def sound(self):
        print("Dog says: Bow Bow")

class Cat:
    def sound(self):
        print("Cat says: Meow Meow")

def make_sound(animal):
    animal.sound()

d = Dog()
c = Cat()

make_sound(d)
make_sound(c)


'''
| Method Overriding                   | Duck Typing                                      |
| ----------------------------------- | ------------------------------------------------ |
| Uses **inheritance**                | **No inheritance** needed                        |
| Child class overrides parent method | Different classes just have the same method name |
| Parent → Child relationship         | No relationship between classes                  |
| Example: `Dog(Animal)`              | `Dog` and `Cat` are separate classes             |'''

# eg 02 
class lion:   # seperate class 1 
    def who(self):
        print("King of the jungle")
         
class tiger(): # seperate class 2
    def who(self):
        print("General of the jungle")
        
def jungle_professionals(animal): # method for access class method 
    animal.who() # j1.who()
# NOTEs: The dot (.) operator is used to access an object's methods and attributes
j1=lion()
j2=tiger()
jungle_professionals(j1)
jungle_professionals(j2)
        
print(j1.who()) 
print(j2.who()) 
        