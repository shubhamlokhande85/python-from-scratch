'7.CheckBox'
'''
-A CheckBox is a GUI control that allows the user to select or deselect an
 option. It is used when the user can choose one or more options from a list.
 A checkbox has two states:
   Checked (Selected) 
   Unchecked (Not selected) 
   
-Syntax
Checkbutton(parent, 
            text="label",
            variable=variable_name, 
            command=function_name)
            
where,
| Parameter  | Description                                                     |
| ---------- | --------------------------------------------------------------- |
| `parent`   | The parent window where the checkbox is placed.                 |
| `text`     | The text displayed next to the checkbox.                        |
| `variable` | Stores the checkbox state (`1` for checked, `0` for unchecked). |
| `command`  | Function that runs when the checkbox state changes.             |

'''

#Eg CheckButton Example

import tkinter as tk 

def show_status():
    if agree_var.get()== 1 :
        result_label.config(text="You Agreed On Terms And Conditions")
    else:
        result_label.config(text="You Have Not Agrred Yet Terms And Conditions")      
root=tk.Tk()
root.title("Checkbutton Example")
root.geometry("500x500")       
agree_var=tk.IntVar() 
checkbox=tk.Checkbutton( root,
                        text="I Agree On This T & C ",
                        variable=agree_var,
                        command=show_status
                        )
checkbox.pack(pady=20)
result_label=tk.Label(root,text="You Have Not Agreed Yet")
result_label.pack(pady=20)
root.mainloop()  


'A.Expalnation Of Each Steps '

import tkinter as tk   # Import tkinter library and give it a short name "tk"

# This function runs when the checkbox is clicked
def show_status():

    # Check the current value of agree_var
    # get() reads the value stored in IntVar
    # 1 means checkbox is checked
    # 0 means checkbox is unchecked
    if agree_var.get() == 1:
        # Change the text of the label if user agreed
        result_label.config(text="You Agreed On Terms And Conditions" )
        
    else:
        # Change the text of the label if user did not agree
        result_label.config(text="You Have Not Agreed Yet Terms And Conditions")


# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Checkbutton Example")

# Set the size of the window (width x height)
root.geometry("500x500")


# Create an integer variable for the checkbox
# Default value is 0 (unchecked)
agree_var = tk.IntVar()


# Create a Checkbutton (checkbox)
checkbox = tk.Checkbutton(
    root,                         # Put checkbox inside the main window

    text="I Agree On This T & C",  # Text shown beside checkbox

    variable=agree_var,            # Connect checkbox with IntVar

    command=show_status            # Call show_status function when clicked
)


# Display the checkbox on the window
checkbox.pack(pady=20)


# Create a label to show the result message
result_label = tk.Label(
    root,
    text="You Have Not Agreed Yet"
)


# Display the label on the window
result_label.pack(pady=20)


# Start the GUI event loop
# Keeps the window open and waits for user actions
root.mainloop()



'B.Concepts'
'''
1. .get()
-.get() is a method used to retrieve (get) the current value of a widget(agree_var)
-agree_var=tk.IntVar() it stores the status of checkbutton 
-from agree_var=tk.IntVar() it gets the current status of the Checkbutton.
 Returns 1 → checkbox is checked
 Returns 0 → checkbox is unchecked.
 
2. .config()
-.config() is a Tkinter method used to change or update the properties 
(settings) of a widget(result_label) after it has been created
-.config() is used to modify an existing widget(result_label
-In case of this example it is changing the text displayed on the label
 it updates the text inside the label dynamically based on whether the check
 button is checked or not
 
 3.tk.IntVar()
 -IntVar() is a Tkinter variable used to store and manage integer values 
  in GUI widgets
-IntVar() creates an integer variable that Tkinter widgets can use to store 
 values like 0 or 1
-here,
 Default value = 0
 Checked Checkbutton → value becomes 1
 Unchecked Checkbutton → value becomes 0
'''
