'14.Listbox'
'''
-A Listbox is a Tkinter widget used to display a list of items from which the user can select 
 one or more options. It is commonly used for displaying menus, choices, or lists of data
-synatx
 tk.Listbox(
    parent,
    height=value,
    width=value,
    selectmode=value
)

where,
parent     → The window or frame where the Listbox is placed.
height     → Number of rows displayed in the Listbox.
width      → Width of the Listbox.
selectmode → Controls the selection type:
                                         tk.SINGLE → Select only one item.
                                         tk.MULTIPLE → Select multiple items.
                                         tk.EXTENDED → Select multiple items using Ctrl/Shift'''

#Eg Listbox Example

import tkinter as tk 

root=tk.Tk()
root.title("Listbox Example")                                         
root.geometry("500x500")

listbox=tk.Listbox(root)
listbox.pack(pady=40)

listbox.insert(1,"Python")
listbox.insert(2,"Java")
listbox.insert(3,"C++")
listbox.insert(4,"javascript")

root.mainloop()

'A.Explanation'
import tkinter as tk              # Import the Tkinter library for creating GUI applications

root = tk.Tk()                    # Create the main application window

root.title("Listbox Example")     # Set the title of the window

root.geometry("500x500")          # Set the size of the window to 500x500 pixels


# Create a Listbox widget
listbox = tk.Listbox(root)        # Create a listbox inside the main window

listbox.pack(pady=40)             # Display the listbox with 40 pixels of vertical padding


# Insert items into the Listbox
listbox.insert(1, "Python")       # Add "Python" as the first item in the listbox

listbox.insert(2, "Java")         # Add "Java" as the second item in the listbox

listbox.insert(3, "C++")          # Add "C++" as the third item in the listbox

listbox.insert(4, "Javascript")   # Add "Javascript" as the fourth item in the listbox


root.mainloop()                   # Start the GUI event loop and keep the window running



'B.Concepts'
'''

1.tk.Listbox()
-tk.Listbox() is a Tkinter widget used to create a list box that displays a collection of items. 
 It allows the user to view and select one or more items from the list
 
2. .insert()
-.insert() is a Tkinter method used to add (insert) an item into a Listbox at a specified position
-syntax
 listbox.insert(index, item)
 where,
 index → The position where the item will be inserted in the Listbox.
 item  → The text or value that you want to add to the Listbox '''