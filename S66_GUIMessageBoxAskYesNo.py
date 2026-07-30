'6.4. MessageBox with askyesno()'
'''
'messagebox.askyesno()'
-messagebox.askyesno() is a function in the Tkinter messagebox module that
 displays a confirmation dialog box with Yes and No buttons. It is used to
 ask the user a question that requires a Yes or No response
 
-Syntax
 messagebox.askyesno(title, message)
 where,
 title   - Specifies the title displayed in the title bar of the dialog box
 message - Specifies the question displayed inside the dialog box
'''
#Eg Messagebox Yes or NO 
import tkinter as tk 
from tkinter import messagebox

root=tk.Tk()
root.title("Yes OR No Message Box Example")
root.geometry("500x500")

def exit_clicked():
    messagebox.askyesno("Confirmation", "Do You Want Exit ?")
    
button=tk.Button(root,text="Exit",command=exit_clicked)
button.pack(pady=30)

root.mainloop()