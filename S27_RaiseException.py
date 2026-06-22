'Raise Exception'

'its used to raise user defined error or error raised by user'
'syntax'
'raise Exception ("Error_Message")'

#eg
age = 12
if(age<18):
    raise Exception ("AgeError : you are not eligible for voting")
else:
    print("you are eligible for vote")
    
# Exception: AgeError : you are not eligible for voting
print(10)
    
