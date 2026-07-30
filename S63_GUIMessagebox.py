'6.1 Message Box with showinfo()'
'''
'Message box'
-A message box is a small dialog window used to display information, 
 warnings, errors, or confirmation messages to the user. It usually 
 contains a message and one or more buttons such as OK, Cancel, Yes, 
 or No
 
'messagebox.showinfo()'
-messagebox.showinfo() is a function in the Tkinter messagebox module that
 displays an information dialog box containing a message and an OK button. 
 It is used to inform the user about successful operations or provide general
 information

-Syntax

 from tkinter import messagebox
 messagebox.showinfo("Title", "This is an information message.")
 
 where,
 -showinfo()   - displays an information dialog with an OK button and returns the string
 -title (str)  - Specifies the title of the message box
 -message(str) - Specifies the text to display'''
 
#Eg simple messagebox
import tkinter as tk 
from tkinter import messagebox

root=tk.Tk()
root.title("MessageBox Example")
root.geometry("500x500")

root.withdraw() # It hide main window 

messagebox.showinfo("Message"," Welcome To GUI Session  ")

root.mainloop()

'A.Explanation'
'''
1.root.withdraw()
-withdraw() is a method of the Tk class.
-It removes (hides) the main window from the screen without destroying it.
-The program continues to run in the background

2.messagebox.showinfo()
-messagebox.showinfo() is a function in Tkinter used to display an information
 message box with an OK button'''
