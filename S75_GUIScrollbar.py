'15.Scrollbar'
'''
-A Scrollbar is a Tkinter widget used to add scrolling functionality to other widgets such as 
 Listbox, Text, Canvas, and Frame. It allows the user to move up, down, left, or right to view
 content that does not fit in the available space
-Syntax
 tk.Scrollbar(
    parent,
    orient=value,
    command=function
)

where,
parent → The window or frame where the Scrollbar is placed.
orient → Specifies the direction of the scrollbar:
                                                    tk.VERTICAL → Vertical scrollbar
                                                    tk.HORIZONTAL → Horizontal scrollbar
command → Connects the scrollbar with another widget's scrolling function'''

#Eg Scrollbar Example

import tkinter as tk
root=tk.Tk()
root.title("Scrollbar Example")
root.geometry("500x500")

listbox=tk.Listbox(root,height=10)
listbox.pack(side="left")

scrollbar=tk.Scrollbar(root)
scrollbar.pack(side="right",fill="y")

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

for i in range(1,21):
    listbox.insert("end",F"item{i}")
    
root.mainloop()


'A.Explanation'
import tkinter as tk                  # Import the Tkinter library for creating GUI applications

root = tk.Tk()                        # Create the main application window

root.title("Scrollbar Example")        # Set the title of the window

root.geometry("500x500")              # Set the window size to 500x500 pixels


# Create a Listbox widget
listbox = tk.Listbox(
    root,                             # Place the listbox inside the main window
    height=10                         # Display only 10 items at a time
)

listbox.pack(side="left")             # Place the listbox on the left side of the window


# Create a Scrollbar widget
scrollbar = tk.Scrollbar(root)        # Create a scrollbar inside the main window

scrollbar.pack(
    side="right",                     # Place the scrollbar on the right side
    fill="y"                          # Stretch the scrollbar vertically
)


# Connect the Listbox with the Scrollbar
listbox.config(
    yscrollcommand=scrollbar.set      # Update the scrollbar position when the listbox is scrolled
)

scrollbar.config(
    command=listbox.yview             # Make the scrollbar control the vertical movement of the listbox
)


# Insert multiple items into the Listbox
for i in range(1, 21):                # Loop from 1 to 20 to create 20 items
    listbox.insert(
        "end",                        # Add the item at the end of the listbox
        f"Item {i}"                   # Insert item names like Item 1, Item 2, etc.
    )


root.mainloop()                       # Start the GUI event loop and keep the window running

'B.concepts'
'''
1.tk.Scrollbar()
-tk.Scrollbar() is a Tkinter widget used to create a scrollbar that allows the user to scroll
 through content in widgets like Listbox, Text, Canvas, and Frame when the content is larger
 than the available space
 
2..pack()
-.pack() is a Tkinter geometry manager method used to arrange and display widgets (such as Button,
 Label, Entry, Frame, etc.) inside a window. It automatically places widgets in the available
 space
-syntax
 widget.pack(
    side=value,
    fill=value,
    expand=value,
    padx=value,
    pady=value,
    ipadx=value,
    ipady=value,
    anchor=value
)
where,
| Parameter | What it does                                                       |
| --------- | ------------------------------------------------------------------ |
| `side`    | Sets the position of the widget (`TOP`, `BOTTOM`, `LEFT`, `RIGHT`) |
| `fill`    | Expands the widget to fill available space (`X`, `Y`, `BOTH`)      |
| `expand`  | Allows the widget to take extra space (`True` / `False`)           |
| `padx`    | Adds horizontal space outside the widget                           |
| `pady`    | Adds vertical space outside the widget                             |
| `ipadx`   | Adds horizontal space inside the widget                            |
| `ipady`   | Adds vertical space inside the widget                              |
| `anchor`  | Controls the widget's position (`n`, `s`, `e`, `w`, `center`)      |


3.yscrollcommand=
-yscrollcommand is a Tkinter widget option used to connect a widget with a vertical scrollbar.
 It updates the scrollbar position whenever the content in the widget is scrolled
-syntax
 yscrollcommand=scrollbar.set
 
 where,
 yscrollcommand → Tells the widget to update the scrollbar.
 scrollbar.set → Updates the scrollbar slider position according to the widget's scrolling
 
4. .set
-.set() is a Tkinter method used to update the position of a scrollbar slider. It tells 
 the scrollbar how much content is currently visible and where the user is in the content.
 
5.config()
-.config() (also called .configure()) is a Tkinter method used to change or update the 
 properties (options) of an existing widget after it has been created.
-Examples of properties that can be changed:
 Text
 Color
 Font
 Size
 State (enabled/disabled)
 Commands
 Scroll connections
-syntax
 widget.config(option=value)
 
 
'6..yview
-.yview() is a Tkinter method used to control vertical scrolling of a widget. It tells a 
  widget (such as Listbox, Text, or Canvas) to move up or down when a scrollbar is used
  
7. .xview
-.xview() is a Tkinter method used to control horizontal scrolling of a widget. It allows 
 a widget like Text, Canvas, or Listbox to move left and right when a horizontal scrollbar 
 is used
  

 '''
