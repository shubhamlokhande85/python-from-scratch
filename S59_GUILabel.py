'2.Label'
'''
-A label is a widget that displays text or information on a graphical user interface.
It is usually used to describe buttons, show messages, or provide instructions to users.
-syntax
tk.Label(window, text="Hello")
where,
tk.Label     - creates a Label widget
window(root) - the parent window where the label will appear
text="Hello" - the text displayed on the label
'''

#Eg   label Example

import tkinter as tk 
root=tk.Tk()
root.title("Label Example")
root.geometry("500x500")
label=tk.Label(root,text="Entre Your Name")
label.pack(pady=20)
root.mainloop()

'A.Explanation'
'''
1.label=tk.Label(root,text="Entre Your Name")

Label      - is a Tkinter widget used to display text or images in a GUI window.
tk.Label() - creates a label object.
root       - is the parent window where the label will be placed.
text=" "   - sets the text shown on the label. Here it displays a blank space


2.label.pack(pady=20)
pack()      - is a Tkinter method used to place (display) a widget inside the window.
pady=20     - adds 20 pixels of vertical space (padding) above and below the label
'''

'B.Concepts'   
'1.label='
'''
-label is a variable used to store the Label widget object.
-It helps us control or modify the label later in the program'''


'2. tk.Label()'
'''
-tk.Label() is a Tkinter widget used to display text or images on a GUI window
-syntax 
tk.Label(window, text="Hello")
where, 
window(root) - is the parent window where the label will be placed
text(" " )   - sets the text shown on the label. Here it displays a blank space

2.label.pack()
-pack() is a Tkinter method used to place and display the label in the GUI window
-syntax 
label.pack(pady=value padx=value)
pady - adds vertical space (top and bottom) around the label.
padx - adds horizontal space (left and right) around the label'''
