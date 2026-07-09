'Inheritance'
'a.one class can use features of another class'
'b.existing class = parent class or superclass or base class'
'c.new class = child class or  subclass or derived class'


'Types of inheritance'

'1.single inheritance '
'''it is a type of inheritance in which one derived class inherits from 
only one base class'''
#structure
'''
base
  |
  |
derived 
'''


# eg 
'Note : To access attribute from base class we use self.attribute in derived class'
class base:
    a ,b=10,20

class derived(base) :
    def product(self):
        c = self.a*self.b
        print("product:",self.a*self.b)
d=derived()
d.product()
#product: 200

'2.Multilevel inheritance'
'''it is type of inheritance in which one class inhherits
from another class and third class inherits derived class'''

#structure
'''
grandparent (base)
     |
     |
parent(derived1)
     |
     |
child(derived2)

'''
#eg
class base:
    d=20
    def show(self):
        print("Value of d from base class",self.d)
class derived1(base):
    e= 30 
    def display(self):
        print("Value of e from derived class",self.e)
class derived2(derived1):
    def sum(self):
        f= self.d+self.e
        print("sum of class:",self.d+self.e)
dd=derived2()
dd.show()
dd.display()
dd.sum()

# Value of d from base class 20
# Value of e from derived class 30
# sum of class: 50   
    
    
'3.Hierachial inheritance'
'''
It is type of inhertiance in which multiple derived class are inherited from
one single base class'''
#structure
'''
                              base
                               |
-----------------------------------------------------------------
|                              |                                |
derived1                     derived2                       derived3

'''
#eg 
class base:
    x,y=100,101
    
class derived1(base):
    def remainder(self):
        z=self.y%self.x
        print("Remainder:",self.y%self.x)
        print(z)
        
class derived2(base):
    def product(self):
        p=self.x*self.y
        print("Product:",self.x*self.y)
        print(p)
        
d1=derived1()
d1.remainder()

d2=derived2()
d2.product()
    
# Remainder: 1
# 1
# Product: 10100
# 10100

'4.Mulitple inheritance'
'''It is type of inheritance in which one derived class inherits from 
multiple base class'''

# structure
'''
base1     base2       base3
|         |           |
-----------------------
          |
        derived 
'''

#eg 
class base1:
    a = 10

class base2:
    b= 20 
    
class derived(base1, base2):
    def sum(self):
        c=self.a+self.b
        print("sum:",c) 
        
d3=derived()
d3.sum()       

'5.Hybrid Inheritance'
'''
It is a type of inhertance that combine two or more types 
of inhertance in a single program'''

# structure 
'''
base1                              base2
|                                  |
derived1                        derived2
|                                  |
------------------------------------
                |
            derived3  
            
'''
class base1:
    r,s=10,20    
class derived1(base1):
    def sum(self):
        d=self.r+self.s
        print("sum:",d)
        
        
class base2:
    l,m=30,40 
class derived2(base2):
    def product(self):
        p=self.l*self.m
        print("product:",p)    
        
class derived3(derived1,derived2):
    def combination(self):
        c=self.r+self.s+self.l+self.m
        print("combination:",c)

d4=derived3()
d4.combination()
#combination : 100

''''Note : To learn self , super(), and accessing attribute and methods 
also store attribute from base class to derived class to look session 37'''