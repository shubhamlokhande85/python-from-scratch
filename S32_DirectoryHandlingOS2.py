'6.os.chdir(path)'
"It is used in python to change or switch current working directory"
'''it is used when we want run a program from another directory in current directory instead
of building new directory from scratch '''

# 
'''import os 
print(os.getcwd())

os.chdir("C:/python_practice_repo")
print("directory changed successfully")

print(os.getcwd())'''

'7.os.listdir()'

"It is used in python to list contents of directory"
"this will show all files and folder inside the directory"
#eg
import os 
print(os.listdir("C:/python_practice_repo"))


'8.os.rmdir()'
"its used to remove a empty directory in python"
"if directory contains file then its raise OsError"
#eg 01
'''os.rmdir("C:/python_from_scratch/New folder") # New folde is empty directory
print("empty directory removed successfully")'''
#empty directory removed successfully

#eg 02
'''os.rmdir("C:/python_from_scratch/New folder (2)")
print("filled directorey removed successfully")'''


'9.shutil.rmtree()'
"its is used to remove a filled directory that contain file or subdirectories in python"
"this will delete all files inside , delele all subdirectories and delete the directory itself "

#eg
import shutil
shutil.rmtree("C:/python_from_scratch/New folder (2)") #  New folde (2) is filled directory
print("filled directory removed successfully using shutil.rmtree()")
#filled directory removed successfully using shutil.rmtree()