'8.Dropdown'
'''
-A Dropdown is a GUI widget that allows the user to select 
 one option from a list of available choices.
-It saves space by showing a list only when the user clicks it.
-In Tkinter,a dropdown is commonly created using the OptionMenu widget
-A dropdown is a selection box where users can choose one value
 from multiple options.
 
-syntax
 tk.OptionMenu(parent, variable, option1, option2, option3) 
 where,
 parent_name               → The window/frame where dropdown is placed (root)
 
 variable_name             → Variable that stores the selected value (StringVar)
 
 option1, option2..._names → Choices shown in the dropdown 
 
 OR
 
 *options            → we can create a list( options = [option1,...,optionN] ) 
                       then we can use *options as third parameter
'''

#Eg Dropdown Example 
import tkinter as tk 

def show_selection(*args):
    print("Selected:", choice.get())
    
root=tk.Tk()
root.title("Dropdown Example")
root.geometry("500x500")

choice=tk.StringVar(value="select a fruit")
options=["Apple","Strawberry","Orange","Mango"]
dropdown=tk.OptionMenu(root,choice,*options)
dropdown.pack(pady=40)

choice.trace_add("write",show_selection)
root.mainloop()    


'A.Explanation'
import tkinter as tk   # Import tkinter library and give it a short name "tk"


# Function that runs whenever the dropdown value changes
def show_selection(*args):

    # choice.get() reads the currently selected value from dropdown
    print("Selected:", choice.get())


# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Dropdown Example")

# Set the size of the window (width x height)
root.geometry("500x500")


# Create a StringVar to store the selected dropdown value
# Initial/default value is "select a fruit"
choice = tk.StringVar(value="select a fruit")


# Create a list of options that will appear in dropdown
options = ["Apple", "Strawberry", "Orange", "Mango"]


# Create a dropdown menu
# root → place dropdown inside the main window
# choice → variable that stores selected option
# *options → sends all list items as separate options
dropdown = tk.OptionMenu(root, choice, *options)


# Display the dropdown on the window
# pady=40 adds vertical space around the dropdown
dropdown.pack(pady=40)


# Monitor changes in the choice variable
# "write" means run function when the value is changed
# show_selection will be called automatically after selection
choice.trace_add("write", show_selection)


# Start the GUI event loop
# Keeps the window open and waits for user actions
root.mainloop() 
                  
'B.Concepts'
'''
1.*args
-*args is used in a function to accept any number of arguments (values)
 without knowing the exact number of inputs beforehand
-*args allows a function to take multiple values and stores them as a tuple


2.tk.StringVar(value)
-StringVar() is a Tkinter variable used to store and manage string (text)
 values in GUI widgets
-value - sets the initial text value

3.*options
-*options is used to unpack (expand) the items of a list, tuple, or other 
 iterable and pass them as separate values to a function
 
4. .trace_add()
 -trace_add() is a Tkinter method used to monitor changes in a Tkinter
  variable (StringVar, IntVar, etc.) and automatically call a function when
  the value changes
-syntax 
 variable.trace_add(mode, callback_function)
 where,
 -mode - specifies what type of change to watch ("write", "read", "unset"
 -callback_function specifies which function should run when that change 
  happens
  
4.1 .trace_add() 's modes 

4.1.A "write" 
-Runs the function when the variable value is changed.
-Use
 When you want to perform an action after a user changes something.
 Example:
  Dropdown selection change
  Text entry change
  Checkbox value change


4.2.B "read"
-Runs the function when the variable value is read using .get()
-Use
 To monitor when someone accesses the variable
   
   
4.3.C "unset"
-Runs the function when the variable is deleted or removed
-Use
 To detect when a variable is removed
 
'''


  