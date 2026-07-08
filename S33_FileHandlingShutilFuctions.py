'Shutil'
''' the Shutil module used for high level file operations especially when working with complete 
directory structures and file copying - moving files '''

'1.shutil.rmtree()'
'its remove filled directory that conatains files and subdirectory  in python '
"this will delete all files inside , delele all subdirectories and delete the directory itself "
'syntax'
'shutil.rmtree("directory_name)'

#eg
'''import os 
os.makedirs("shutil_directory/shutil.png")
print("directory created successfully")'''


'''import shutil 
shutil.rmtree("shutil_directory")
print("directory removed successfully")'''


'2.shutil.copy()'
'in python this function copies files data  into another file and file data into a another directory '
'in this method when data copied in file then the  exist data will be eraised '
'''when we copy file into directory we have use forward slash end of the directory path or name '''
' '
'syntax'
'shutil.copy(src.dst)'
''' where
src = path or source of file 
dst = path odf destination file or directory'''
    

#eg - 01 - file into file 
'''
with open("database.txt","x") as file:
     file.write("real data is here")
with open("backup.txt","w") as file:
     file.write("all set")
with open ("backup.txt","r") as file1:    
     data=file1.read()
     print(data)
     
import shutil 
shutil.copy("database.txt","backup.txt")
print("data copied succesfully")

# to check data copied or not
with open("backup.txt","r")as file:
    data=file.read()
    print(data)'''

#eg 02 - file into directory 
'''when we copy file into directory we have use forward slash end of the directory path or name '''
'''import os 
os.mkdir("daily")
print("daily directory created successfully")

import shutil 
shutil.copy("sample.txt","daily/")    # / used end of directory name 
print("data copied successfully from file to directory ")'''
    
"note : you can not copy directory into file when we have to copy directory use another directory as destination" 

    
'3.shutil.copytree()'
'is used to copy directory into another directory '
'when we have to copy directory into another directory we use  dirs_exist_ok=True inside the shutil.copytree()'

# Syntax
# shutil.copytree(src.dst,dirs_exist_ok=True) 



#eg -01 ='if when we have to copy directory(parent) inside the directory(parent)
'''import os 
 os.makedirs("shutil_directory2")
 print("directory created successfully2")

 import shutil
 shutil.copytree("C:/python_from_scratch/shutil_directory/shutil.png","C:/python_from_scratch/shutil_directory2",dirs_exist_ok=True)
 print("directory copied successfully")'''

#eg - 02 
'''import os 
os.mkdir("backupPythonRepoShubham")
print("backupPythonRepoPranand directory created successfully")'''

'''import shutil
shutil.copytree("C:/python_practice_repo", "C:/python_from_scratch/backupPythonRepoShubham",dirs_exist_ok=True)
print("directory copied successsfully")'''


'4.shutil.move()'

'''shutil.move() is a function in Python's built-in shutil module that 
moves a file or directory from one location to another'''

'syntax'
'shutil.move(src.dst,copy_function=shutil.copy2)'
'where'
'''copy_function=shutil.copy2 = is optional:Function used for copying if moving across different file systems.
The default is shutil.copy2, which preserves metadata.'''

#eg 

'''with open("db1.txt","w") as file:
     file.write("Here we go again")
     file.write("\n accelarating my things from scratch")
     
with open("db1.txt","r") as file2:
     data=file2.read()
     print(data)

import os 
os.mkdir("backup_db") 

import shutil

shutil.move("db1.txt","backup_db")
print("data moved successfully from db1 to backup_db")'''

'5.shutil.make_archive()'

'''shutil.make_archive() is a function in Python's built-in shutil module that
creates a compressed archive (such as ZIP or TAR) from a directory'''

'syntax 01'
'''import shutil

shutil.make_archive(
    base_name,
    format,
    root_dir=None,
    base_dir=None,
    verbose=0,
    dry_run=False,
    owner=None,
    group=None,
    logger=None
)'''
'where' # copied from chatgpt
'''
| Parameter   | Description                                                                       |
| ----------- | --------------------------------------------------------------------------------- |
| `base_name` | The name (and optional path) of the archive file **without the extension**.       |
| `format`    | Archive format. Common values: `'zip'`, `'tar'`, `'gztar'`, `'bztar'`, `'xztar'`. |
| `root_dir`  | The root directory where archiving starts.                                        |
| `base_dir`  | Directory inside `root_dir` to archive.                                           |
| `verbose`   | Deprecated. Previously controlled verbosity.                                      |
| `dry_run`   | If `True`, performs a trial run without creating the archive.                     |
| `owner`     | Owner name for TAR archives (Unix).                                               |
| `group`     | Group name for TAR archives (Unix).                                               |
| `logger`    | Logger object for recording operations.                                           |
'''
'syntax 02'
'''shutil.make_archive(base_name, format, root_dir)'''
'''
| Argument    | Value         | Description                                                                                                                                                                    |
| ----------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `base_name` | `"backup"`    | **Name of the archive file** to create, **without the extension**. It is **not** a directory. Python automatically adds the appropriate extension based on the archive format. |
| `format`    | `"zip"`       | The archive format. Here, it creates a ZIP file.                                                                                                                               |
| `root_dir`  | `"my_folder"` | The directory whose contents will be archived (compressed).                                                                                                                    |
'''


'formats'
'''
| Format    | File Extension |
| --------- | -------------- |
| `'zip'`   | `.zip`         |
| `'tar'`   | `.tar`         |
| `'gztar'` | `.tar.gz`      |
| `'bztar'` | `.tar.bz2`     |
| `'xztar'` | `.tar.xz`      |'''

#eg 01 - this normal file to create archive 
'''
import shutil
archived=shutil.make_archive("backup_db2","zip","my_folder1")
print(archived)'''
#C:\python_from_scratch\backup_db2.zip

# eg 02 - to store all archives in one file we use - archive/base_name inside the shutil.make_archive()
'''
import shutil 
my_archived=shutil.make_archive("archive/my_backup","zip","my_folder2")
print(my_archived)'''
# C:\python_from_scratch\archive\my_backup.zip 


'''
archive = for all archive can store in one location at  the directory
base_name = archive file name that we going create - user defined name 
format = here archive file format like  - "zip" , "tar"
root_dir = which file we want archive that file name or  (directory name)'''



'6.shutil.unpack_archive()'
'''
shutil.unpack_archive() extracts (unpacks) the contents of an 
archive such as a ZIP or TAR file into a directory.'''

'syntax'
'''import shutil

shutil.unpack_archive(
    filename,
    extract_dir=None,
    format=None
)'''

'where'
'''
| Parameter     | Description                                                                                                                        |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `filename`    | The path to the archive file (`.zip`, `.tar`, `.tar.gz`, etc.).                                                                    |
| `extract_dir` | The directory where the files should be extracted. If omitted, the current working directory is used.                              |
| `format`      | Optional. The archive format (`"zip"`, `"tar"`, `"gztar"`, etc.). Usually Python detects it automatically from the file extension. |'''


#eg 
'''
import os 
os.mkdir("extracted_archives")
import shutil 
unpack_archived=shutil.unpack_archive("archive/my_backup.zip","extracted_archives")
print("data extracted successfully")
'''


'''
python_from_scratch/
│
unpack_archived=shutil.unpack_archive("archive/my_backup.zip","extracted_archives")
|
├── archive/
│   └── my_backup.zip      ← Still here - just archived at original location
│
├── extracted_archives/    - files data are now in extracted_archives directory 
│   ├── file1.txt
│   ├── file2.txt
│   └── images/
│
└── program.py'''