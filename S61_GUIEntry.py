'4.Entry'
'''
-A Entry is a GUI widget that allows the user to enter and edit text or data
 in a single-line input box
-syntax
 tk.Entry(window)
 where,
 -tk.Entry()   - creates a text box where the user can enter information
 -windoe(root) - is the parent window where the entry box will be placed'''

#Eg Entry Example 
import tkinter as tk 
root=tk.Tk()
root.title("Entry Example")
root.geometry("500x500")

entry=tk.Entry(root)
entry.pack(pady=30)

root.mainloop()

'A.Expalnation'
'''
1.entry=tk.Entry(root)

-entry=      - is a variable used to store the Entry widget object.
-tk.Entry()  - creates a text box where the user can enter information.
-root        - is the parent window where the entry box will be placed'''
