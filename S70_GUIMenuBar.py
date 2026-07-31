'10.MenuBar'
'''
-A menu bar is a horizontal bar at the top of a GUI window that
 contains menus with different commands or options for the user to select
-Syntax
import tkinter as tk

root = tk.Tk()

menubar = tk.Menu(root)

root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")

menubar.add_cascade(label="File", menu=file_menu)

root.mainloop()


where, 
1. menubar = tk.Menu(root)   - Creates a menu bar

2. root.config(menu=menubar) - Displays the menu bar in the window

3. file_menu = tk.Menu(menubar, tearoff=0) - Creates a dropdown menu (like File menu) inside the menu bar

4.file_menu.add_command(label="Open") - Adds commands/options inside a menu

5.menu.add_cascade(label="File", menu=file_menu) - Adds a menu item (like File) to the menu bar.


'''

#Eg ManuBar Example

import tkinter as tk 
from tkinter import messagebox 

def new_file():
    messagebox.showinfo("New_file","New file selected")
def open_file():
    messagebox.showinfo("Open_file","Open file selected")
def show_about():
    messagebox.showinfo("About","Tkinter Menubar widget Example")
    
root = tk.Tk()
root.title("MenuBar Example ")
root.geometry("500x500")

menu_bar=tk.Menu(root)

file_menu=tk.Menu(menu_bar,tearoff=0)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

menu_bar.add_cascade(label="File",menu=file_menu)


help_menu=tk.Menu(menu_bar,tearoff=0)
help_menu.add_command(label="About",command=show_about)

menu_bar.add_cascade(label="Help",menu=help_menu)

root.config(menu=menu_bar)
root.mainloop()


'A.Explanation'
# Import tkinter library and give it a short name 'tk'
import tkinter as tk

# Import messagebox module to show popup messages
from tkinter import messagebox


# Function that runs when "New" option is clicked
def new_file():
    # Display an information popup box
    messagebox.showinfo("New_file", "New file selected")


# Function that runs when "Open" option is clicked
def open_file():
    # Display an information popup box
    messagebox.showinfo("Open_file", "Open file selected")


# Function that runs when "About" option is clicked
def show_about():
    # Display information about the application
    messagebox.showinfo("About", "Tkinter Menubar widget Example")


# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("MenuBar Example")

# Set the size of the window (width x height)
root.geometry("500x500")


# Create the main menu bar that will appear at the top of the window
menu_bar = tk.Menu(root)


# Create a dropdown menu named File inside the menu bar
# tearoff=0 prevents the menu from being separated into another window
file_menu = tk.Menu(menu_bar, tearoff=0)


# Add "New" option inside File menu
# When clicked, it calls the new_file() function
file_menu.add_command(label="New", command=new_file)


# Add "Open" option inside File menu
# When clicked, it calls the open_file() function
file_menu.add_command(label="Open", command=open_file)


# Add a horizontal line separator between menu options
file_menu.add_separator()


# Add "Exit" option inside File menu
# root.quit closes the application window
file_menu.add_command(label="Exit", command=root.quit)


# Attach File dropdown menu to the main menu bar
# It creates a "File" option on the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)


# Create another dropdown menu named Help
help_menu = tk.Menu(menu_bar, tearoff=0)


# Add "About" option inside Help menu
# When clicked, it calls show_about() function
help_menu.add_command(label="About", command=show_about)


# Attach Help dropdown menu to the main menu bar
menu_bar.add_cascade(label="Help", menu=help_menu)


# Display the menu bar at the top of the application window
root.config(menu=menu_bar)


# Start the GUI event loop and keep the window running
root.mainloop()

'B.Concepts'
'''
1. tk.Menu()
-tk.Menu() is a Tkinter widget used to create a menu or menu bar that 
 contains commands/options for the user
-syntax 
 menu_name = tk.Menu(parent)
 parent - root (window)
 
 
2. tearoff=0
-tearoff=0 disables the detachable menu feature, so the dropdown menu 
 cannot be separated into a new window
-syntax 
 tk.Menu(parent, tearoff=0)
 
 
3.add_command()
-add_command() adds an option/item inside a menu. When the user clicks it,
 a specific function runs
-syntax
 menu_name.add_command(label="Option Name", command=function_name)
 
 
4. add_cascade()
-add_cascade() attaches a submenu to a menu bar or another menu. It creates
 menu headings like File, Edit, Help
-syntax
 menu_bar.add_cascade(label="Menu Name", menu=sub_menu)
 
5. add_separator()
-add_separator() adds a horizontal dividing line between menu options to
 group related items
-syntax
 menu_name.add_separator()
 
 
6. .config()
-.config() is used to change or update the properties/settings of a Tkinter
 widget after creating it
-syntax
 widget_name.config(property=value)
-eg
 root.config(menu=menu_bar)
 -Displays the created menu bar on the main window
 
 7. .quit()
 -.quit() is a Tkinter method used to stop the application's main event loop
  and close the GUI window
-syntax
 root.quit()


'''
