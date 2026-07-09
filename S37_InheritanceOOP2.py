'1.base class'
'''
A base class is a class whose attributes and methods are inherited by 
another class'''
# eg 
class parent: # base class 
    aa = 10
    def show(self):
        print("This is the base class")
class child(parent):  # derived class
    pass
s=child()
s.show()
print(s.aa)
#This is the base class
# 10

'2.derived class'
'''
A derived class is a class that inherits attributes and methods from
another class (called base class)'''

#eg
class base:
    a,b=10,20

class derived(base):
    def sum(self):
        self.s=self.a+self.b
        print("sum:",self.s)
    
d=derived()
d.sum()

'3.Methods of accessing'
'A.To access attribute from base class to derived class  '

# eg 01  - accessing base class attribute in derived class - normal inheritance
class base :
    e = 10000   
class derived(base): 
    pass 
dd=derived()
print(dd.e)
# 10000
    
#eg 02 - accessing base class attribute in derived class methods - self keyword
'self keyword'
'We use self keyword to access attribute from base class in drerived class '
#eg
class base1:
    f,g=30,40
    
class derived1(base1):
    def product(self):
        print("product:", self.f* self.g)
        
ddd=derived1()
ddd.product()
# product: 1200

'B.accessing method from base class to derived class'
'super()'
'We use super() to access method from base class in drerived class '
#eg
class base1:
    def show(self,name):
        print("hello world")
        print("Hi My Name is ",name)
        
        
class derived1(base1):
    def access_method_from_base(self):
        super().show("shubham")
d4=derived1()
d4.access_method_from_base()
# hello world
# Hi My Name is  shubham

'C.Storing base class attribute in derived class'
class base :
    k = 20 
    
class derived(base):
    l = base.k  # base class attribute stored in it using -  derived_class_attribute = base_class_name.attribute_name
    m = 40
    def show(self):
        print("stored attribute in derived class",self.l ,"and sum of of it with derived class attribute",self.m,"sum:", self.l+self.m)
        print(self.k)
        
d5= derived()
d5.show()
# stored attribute in derived class 20 and sum of of it with derived class attribute 40 sum: 60
# 20
    