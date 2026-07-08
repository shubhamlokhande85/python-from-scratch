'OS module function for file handling'

'''
a. the os module in pyhton is a built in module that provides functions to interact with 
operating system

b.it stands for operating system module and help python programs perform system level 
task  like file and directory mangement

c.when we use OS module for file handling we must import os module as import os

d.in python role of os module in file handling is that it is used for file operatios
that go beyond reading and writing files , such as renaming a file ,deleting a file , 
checking if a file exists etc'''

'1.os.rename()'
'''
it is used to change the name of a file if the file does not exist then
python raise a FileNotFoundError'''

'syntax'
'os.rename("old_file_name","new_file_name")'
# eg 

import os 

'os.rename("sample.txt","Example.txt")'

print("file renamed successfully")


'2.os.path.exists()'
'''
it is used to to check whether a file or directory exists or not It return True if file or
folder exists and returns false if the file or folder does not exist'''

'syntax'
' os.path.exists("file_name") '

#eg
# import os 

print(os.path.exists("Example.txt"))

#True

'3.os.remove()'

'''
it is used to delete or remove a file from the system (it permantly deletes file)'''

'syntax '
'os.remove("file_name")'

#eg
with open("Example2.txt","w") as file:
    file.write("we create new Example2 file here to demonstrate how to remove file ")
    print("new file - Example2 is here created")
    
# import os 
os.remove("Example2.txt")
print("file removed successfully")

