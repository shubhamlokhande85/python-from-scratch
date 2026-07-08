'OBJECT ORIENTED PROGRAMMING'

'A.ENCAPSULATION'

'01.Class'

'''-A class in python is user defined datatype conatains attributes 
and methods
a.
In python a class is blueprint for creating object
b.
It helps you group data (variables/attributes) and actions (functions/methods) together in one place
c.
A class is like a design or template for making object
d.
class= car design
object = actual car made from that design 
e.
1.A class is a blueprint for creating objects.
2.An object is an instance of a class.
3.__init__() is the constructor and runs automatically when an object is created.
4.self refers to the current object and is used to access its attributes(variable) 
and methods(functions).
'''
'''
f.01-syntax of class without __init__()'''
'''class ClassName:
    def method_name(self):
        # Method body
        pass '''
#eg - 01 
class student : 
    name = "shubham"
    def display(self):
        print("Student Name:", self.name)
# object
s=student()
s.display()

'''
f.02-syntax of class with __inti__()'''
'''
class ClassName:
    def __init__(self, parameter1, parameter2, ...):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        ...

    def method_name(self):
        # Method body
        pass'''

#eg.02 
class student2:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks 
        print("Hello from __init__")
        self.display()
    def display(self):
        print("Hello from display()")
        print("Student ID:",self.id)
        print("Student Name:",self.name)
        print("Student Marks:",self.marks)
         
# object 
ss=student2("1","shubham","76")

'02.Object'
'''
An object is an instance of a class.'''

'syntax'
'object_name=class_name("arguments")'

#eg 01 - without __init__()
class empolyee:
    name="sam"
    salary=50000
    def show(self): # here self is denoting object (sss=employee())
        print("Name :",self.name)
        print("salary :",self.salary)
        
'a.simple object creation'
sss=empolyee()

'b.accessing atrribute(variable) defined inside the class '
print(sss.name)

'c.accessing Method(Function) defined inside the class '
sss.show()
