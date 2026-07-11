"Data Abstraction"
'showing only important details '
'''
-Data abstraction is the concept of hiding the internal implementation 
details of data and showing only essentials features to user 
-In python abstraction is implemented mainly using abstract classes(base class), abstract
method from ABC module
-Abstraction means a method whose implementation is provided in the the 
derived class , while the method is declared in the abstract (base) class
without defining its internal details '''

# eg 01 
from abc import ABC , abstractmethod   # abc = abstract module 
class base(ABC): # ABC = abstract method 
    @abstractmethod # decorator 
    def show(self):
        pass
class derived(base):
    def show(self):
        print("java is interpeter langauges")
        
dd=derived()
dd.show()