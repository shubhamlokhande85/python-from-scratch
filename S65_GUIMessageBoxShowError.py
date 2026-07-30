'6.3. Message Box with ShowError()'
'''
'messagebox.showerror()'
-messagebox.showerror() is a function in the Tkinter messagebox module that
 displays an error dialog box containing an error message and an OK button.
 It is used to notify the user when an error or problem has occurred
 
-Syntax
messagebox.showerror(title, message)
where,
title   - Specifies the title displayed in the title bar of the error dialog
message - Specifies the error message displayed inside the dialog'''

#Eg 
import tkinter as tk
from tkinter import messagebox 

def login_clicked():
    messagebox.showerror("Error","Username Or Password Is Incorrect")
    
root=tk.Tk()
root.title("Message Box ShowError Example ")
root.geometry("500x500")

button=tk.Button(root,text="Login",command=login_clicked)
button.pack(pady=30)

root.mainloop()
