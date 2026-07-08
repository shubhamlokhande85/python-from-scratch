'File handling function and method'

'1 - file.write()'
'''
it is used to write data into the file '''

#eg
with open ("sample.txt","w") as file:
    file.write("hello world")
    print("data written in sample")
    
'2 - file.read()'

'''
it is used to read data from a file in python'''

# eg
with open("sample.txt","r") as file2:
    data=file2.read()
    print(data)

'3 - open()'
'''
it used to open a file so we can read from it or write to it'''

#eg
file=open("sample.txt","r")
print("sample file opened")
file.close()

'4 - close()'

'''
it is used to close a file after working with '''
'it closing a file saves memory and resources'

'syntax'
'file_name.close() '

#eg
file2=open("sample.txt","r") 
print("sample file opened again")
file2.close()


'5.closed method'
'''
closed is an attribute that checks whether a file is closed or not
it return false if the file is open 
it return True if the file is closed '''

# eg 
f=open("Example.txt","r")
print(f.closed)
#False
f.close()
print(f.closed)
# True

