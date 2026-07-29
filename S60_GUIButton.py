'3.Button'
'''
-A Button is a GUI widget that allows the user to click and perform a specific 
 action or execute a command in an application
-It is used to execute commands like submitting data, closing a window, or 
 displaying a message
 -syntax 
 tk.Button(window, text="Button Name", command=function_name)
 where,
 window(root)  - Parent window where the button will be placed.
 text(" ")     - Sets the text displayed on the button.
 command       - Specifies the function that runs when the button is clicked.'''
 
 
 #Eg Button Example 
import tkinter as tk 
root=tk.Tk()
root.title("Buttton Example")
root.geometry("500x500")

def button_clicked():
    print("Form Submitted")
    

button =tk.Button(root,text="Submit", command=button_clicked)
button.pack(pady=30)

root.mainloop()


'A.Explanation'
'''
1.def button_clicked():
    print("Form Submitted")
-Creates a function that runs when the button is clicked.
-It displays "Form Submitted" in the output screen


2.button = tk.Button(root, text="Submit", command=button_clicked)
-Creates a Button widget in the window.
 text="Submit" displays the button name.
 command=button_clicked connects the button click with the function
 
3.button.pack(pady=30)
-Places the button in the GUI window.
 pady=30 adds 30 pixels of vertical space around the button '''




'B.Concepts'

'1.button='
'''
-button is a variable used to store the Button widget object.
-It helps us access or modify the button later in the program'''


'2.tk.Button()'
''''
-tk.Button() is a Tkinter widget used to create a clickable button in a GUI window.
-It allows the user to perform an action when the button is clicked
-syntax 
 tk.Button(window, text="Button Name", command=function_name)
 where,
 window(root)  - Parent window where the button will be placed.
 text(" ")     - Sets the text displayed on the button.
 command       - Specifies the function that runs when the button is clicked
'''


'3.button.pack()'
'''
-pack() is a Tkinter method used to display and place the button in the GUI window.
-It automatically arranges the button inside the parent window
-syntax
 button.pack(pady=value)
 where,
 -pady - adds vertical space (top and bottom) around the button
 -padx - adds horizontal space (left and right) around the button'''
