'5.TextBox'
'''
-A Text Box is a GUI element that allows the user to type, enter, 
 and edit text or data in an application
-Textbox is a Tkinter widget used to create a multi-line text box in a GUI window.
-It allows users to enter, edit, and display multiple lines of text.

-syntax
textbox = tk.Text(window, width=value, height=value)
where,
window(root) → Parent window where the text box will be placed.
width        → Sets the width of the text box.
height       → Sets the height of the text box
'''


#Eg TextBox Example 

import tkinter as tk 

root = tk .Tk()
root.title("TextBox Example")
root.geometry("500x500")

def button_clicked():
    print("Application Submited")
    
label=tk.Label(root,text="Entre Your First Name")
label.pack(pady=20, padx=30)

textbox=tk.Text(root,width =50 , height = 5)
textbox.pack(pady=10,padx=10)


button=tk.Button(root,text="Submit",command=button_clicked)
button.pack(pady=10)

root.mainloop()

'A.Expalnation'

'1.textbox=tk.Text(root,width =50 , height = 5)'
'''
textbox   → A variable used to store the Text widget object.
tk.Text() → Creates a multi-line text box where users can enter or edit text.
root      → The parent window where the text box will be placed.
width=50  → Sets the width of the text box (50 characters).
height=5  → Sets the height of the text box (5 lines)'''

'B.concept'
'''
1.textbox=
-textbox is a variable used to store the Text Box widget object.
-It helps us access or modify the text box later in the program


2.tk.Text()
-tk.Text() is a Tkinter widget used to create a multi-line text box in a GUI window.
-It allows users to enter, edit, and display multiple lines of text.

3.root          → The parent window where the text box will be placed.

4.width=value   → Sets the width of the text box (in characters).

5.height=value  → Sets the height of the text box (in lines)'''

