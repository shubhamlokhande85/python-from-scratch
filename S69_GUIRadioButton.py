'9.Radiobutton'
'''
-A Radiobutton is a GUI widget that allows the user to select only one 
 option from a group of choices
-synatx
 tk.Radiobutton(parent, text, variable, value, command)
 where,
  parent(root) → The window/frame where the RadioButton is placed.
  text         → Text displayed beside the button.
  variable     → A Tkinter variable (StringVar or IntVar) that stores the selected option.
  value        → The value assigned to that particular option(eg -"Male","Female").
  command      → Function that runs when the option is selected'''
  
#Eg RadioButton Example

import tkinter as  tk 

def show_gender():
    print("Selected Gender:", gender.get())

root=tk.Tk()
root.title("RadionButton Example")
root.geometry("500x500")
    
gender=tk.StringVar(value="Male")

tk.Radiobutton(root,
                text="Male",
                variable=gender,
                value="Male",
                command=show_gender
).pack(anchor="w")

tk.Radiobutton(root,
                text="Female",
                variable=gender,
                value="Female",
                command=show_gender
).pack(anchor="w")

root.mainloop()


'A.Explanation'
import tkinter as tk   # Import tkinter library and give it a short name "tk"


# Function that runs when a RadioButton is selected
def show_gender():

    # gender.get() reads the currently selected RadioButton value
    print("Selected Gender:", gender.get())


# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("RadioButton Example")

# Set the size of the window (width x height)
root.geometry("500x500")


# Create a StringVar to store the selected gender
# Default value is "Male", so Male button will be selected initially
gender = tk.StringVar(value="Male")


# Create first RadioButton
tk.Radiobutton(
    root,                    # Place RadioButton inside the main window

    text="Male",             # Text displayed next to the button

    variable=gender,         # Connect this button with the gender variable

    value="Male",            # Value stored when this button is selected

    command=show_gender      # Call show_gender function when clicked

).pack(anchor="w")           # Display button and align it to the left


# Create second RadioButton
tk.Radiobutton(
    root,                    # Place RadioButton inside the main window

    text="Female",           # Text displayed next to the button

    variable=gender,         # Use the same variable as Male button

    value="Female",          # Value stored when this button is selected

    command=show_gender      # Call show_gender function when clicked

).pack(anchor="w")           # Display button and align it to the left


# Start the GUI event loop
# Keeps the window open and waits for user actions
root.mainloop()

'B.Concepts'
'''
1.anchor=""
-In Python GUI (Tkinter), an anchor is a value that controls where a widget's
 content is positioned inside its available space
-anchor="" is parameter of pack() 
-anchor tells Python GUI where to place a widget or its content inside the
 available space (top, bottom, left, right, or center)

-Common anchor values 
| Anchor Value | Meaning    | Position            |
| ------------ | ---------- | ------------------- |
| `N`          | North      | Top center          |
| `NE`         | North-East | Top right corner    |
| `E`          | East       | Middle right        |
| `SE`         | South-East | Bottom right corner |
| `S`          | South      | Bottom center       |
| `SW`         | South-West | Bottom left corner  |
| `W`          | West       | Middle left         |
| `NW`         | North-West | Top left corner     |
| `CENTER`     | Center     | Middle center       |

-On Map(window)
          N
          |
     NW   |   NE
          |
W --------+-------- E
          |
     SW   |   SE
          |
          S

        CENTER
        
        

'''
