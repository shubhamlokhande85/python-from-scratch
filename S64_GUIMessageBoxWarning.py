'6.2. Message Box with ShowWarning()'
'''
'messagebox.showwarning()'
 -messagebox.showwarning() is a function in the Tkinter messagebox module that 
  displays a warning dialog box. It is used to alert the user about a situation
  that requires attention but is not necessarily an error. The dialog shows a 
  warning icon and an OK button
  
-Syntax
 messagebox.showwarning("Warning(title)", "This is a warning.")
 where,
 title   - The title displayed in the title bar of the warning dialog
 message - The warning message shown inside the dialog
 
'''

#Eg warning box 

import tkinter as tk 
from tkinter import messagebox

root=tk.Tk()
root.title("Warning Box Example")
root.geometry("500x500")

root.withdraw()

messagebox.showwarning("Warning","Battery Level Is Low")

root.mainloop()

