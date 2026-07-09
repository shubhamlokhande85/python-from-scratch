'OBJECT ORIENTED PROGRAMMING'

'A.ENCAPSULATION'

'CLASS'
'1.ATTRIBUTE '
'it is variable that defined inside class'

'2.METHOD'
'it is functions that defiend inside the class'

'3.CONSTRUCTOR(__INIT__() )'
'special method that runs automatically when object is created'
'self is mandatory to __init__() method as the first parameter which refer to current object of the class'

# eg 01 - calling class insidely - its run automatically
class student:
    def __init__(self , name , marks):
        self.name=name
        self.marks=marks
        print("Name:", self.name) # calling variable / attribute from inside class
        self.show()               # calliong function / method from inside class
    def show(self):
        print("Marks:", self.marks)
            
s=student("sam",80)

#eg 02 - calling class outsidely - its run when we try to access atrribute or method
class empolyee: 
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def display(self):
        
        print("Marks:",self.salary)
        
        
ss=empolyee("suraj",15000)
print("Name:",ss.name) # calling class attribute outside the class
ss.display()           # calling class method outside the class

'4.SELF Keyword'
'''
a.A reference variable that points to the current object the class
b.it is used to access object variables and accesss object methods inside the class
c.self is special keyword that in python that represents the current ojects of class
d.self is mandatory to __init__() method as the first parameter which refer to current object of the class
'''

# eg 01 - self in case of constructor(__init__())
class product:
    def __init__(self,product,value):
        self.product=product
        self.value=value
        print("Product Name:",self.product)
        self.price()
    def price(self):
        print("Value:",self.value)


p=product("Scented Candle",100)

# eg 02 - self in case of normal class 

class product2:
    product="Candle"
    value=200
    def price(self):
        print("Value:",self.value)
pp=product2()
print("Product Name:",pp.product)
pp.price()
   
# eg 03 - Exception case - depend on scope or reference
'''
in case of same attribute name's self always execute that attribute or method
that refer(self) to object(object attribute) and igonores local attribute'''

'let me show how that works '
'a.'
class student2:
    name="shubham" # object attribute
    def display(self):
        name="rahul" # local attribute 
        print("Student Name:",self.name) # self is refered to object variable
ss=student2()
ss.display()
#Student Name: shubham 

'b.'
class student3:
    name="shubham" # object attribute
    def display(self):
        name = "rahul" # local attribute
        print("Student Name:",name) # self is not defined here so name is now local attribute
sss=student3()
sss.display()
#Student Name: rahul

