'1.os.mkdir(name)'
'syntax'
'os.mkdir("directory_name")'
'its create new directory in current directory(folder) using user defined name '
'''creating new direactory'''
#eg
# import os 
# os.mkdir("my_folder")
# print("New directory created")


'2.os.mkdir(path)'
'its create new directory using path (location) and user defined name'
'syntax'
'os.mkdir(path)'
'where,'
'path= location of directory where this directory will get create'
#eg
# import os 
# os.mkdir("C:/python_from_scratch/my_folder2")
# print("second directory created")


'3.os.makedirs()' '-' 'nested directories'
'this function used create multiple(nested) directories at onece'
#eg
# import os 
# os.makedirs("project_umbrella/images")
# print("Multiple (nested)  directories created")

'4.1.os.renames()'
'this function is used to rename directory using file name'
#eg
'''import os 
os.rename("project_umbrella","Umbrella_Corporation")
print("Directory name changed successfully")'''


'4.2.os.renames(path)'
'this function is used to rename directory using specific path'
'if file not found then its raise FileNotFoundError '

#eg 
'''import os 
os.rename("C:/python_from_scratch/my_folder","C:/python_from_scratch/my_folder1")
print("directory rename successfully using path")'''


'5.os.getcwd()'
"its function used in python to display current working directory"

import os 
print("hello world")
print(os.getcwd())
print("hello world")


