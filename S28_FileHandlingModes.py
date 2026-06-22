'file handling'
''''
we use file handling in python to store, read and mange data 
permanently in files without file handling data is lost when the 
program ends '''

'A.With Open()'
'''
we use the with open() statement in python for file handling because
it provides a safe and efficient way to work with files'''

'''the main advantages of with open() is that if automatically closes the 
file after the block of code is executed even if an error occurs during file 
operations this helps prevent file corruption and saves system resourecs 
it also moves the code cleaner and easier to read because we do not need to 
explicity call close()'''


'B.file modes in python'

'1."x"'
'''
it stands for or is known as exclusive creation mode'''
'''
a.the x mode in python is used to create a new file safetly
without overwriting an existing file
b.if file does not exist pyhton automatically create it and then allow
writing data into it
c.however if the file already exist then python does not create a 
new one and raise FileExistError'''

#eg 
'''with open("assignment.txt","x") as file :
    file.write("hi my name is shubham")
    file.write(" and whats your name?")'''
    
    
'if file exist it raise FileExistError '
#FileExistsError: [Errno 17] File exists: 'assignment.txt'


'''
2.'r'

'''
'''
a. 'r' is stand for or is known as read mode is used to open 
    an existing file only for reading data in python
b. if file does not found it raise FileNotFoundError'''

with open("greetings.txt","r") as file:
    data=file.read()
    print(data)
    
    
'''
3. 'w'

'''
'''
'w' - it stand for or is known as write mode and is used to open a file 
for writing data in python
- if the file does not exist its create new file automatically
-if file already exist then all previous content of the file will be 
erased (overwriting)
'''
#eg
with open ("Demo.txt","w") as file2:
    file2.write("hi i would like to introduce myself my name is shubham")
    print("data written successfully in the demo file")
    
# to check data written or not 
with open("Demo.txt","r") as file3:
    data3=file3.read()
    print(data3)

# in case of file already exist then previous data will erased
with open("Demo.txt","w") as file4:
    file4.write(" hey hi guys good to see you all ")
    print("this file over written")
    
# to check file overwritten or not 
with open("Demo.txt","r") as file5:
    data5=file5.read()
    print(data5)    
    
'''
4. 'a'

'''
'''its stand for or is known as append mode and 
is used to add data at the end of existing file in python'''

'''if the file does not exist then python will create a new file automatically'''
'''if the file already exist then the existing content off the file is not overwritten new
 data is added after the existing content
 '''
 
with open("demo.txt","a") as file6:
    file6.write("\n This the python respository teach you lot")
    file6.write("\n about basic python")
    print("data append succussfully in the demo")
    
with open("demo.txt",'r') as file7:
    data7=file7.read()
    print(data7)
    
     













