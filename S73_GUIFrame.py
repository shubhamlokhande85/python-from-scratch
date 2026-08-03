'13.Frame'
'''
-A Frame is a Tkinter widget used to group and organize other widgets (such as buttons, labels, 
 entry boxes, etc.) inside a window. It helps arrange the GUI into different section
-Syntax 
tk.Frame(
    parent,
    bg="color",
    width=value,
    height=value,
    bd=value,
    relief="style"
)


where,
| Parameter | Description                                                                     |
| --------- | ------------------------------------------------------------------------------- |
| `parent`  | The window or frame where the Frame is placed.                                  |
| `bg`      | Sets the background color of the Frame.                                         |
| `width`   | Sets the width of the Frame.                                                    |
| `height`  | Sets the height of the Frame.                                                   |
| `bd`      | Sets the border thickness.                                                      |
| `relief`  | Sets the border style (`FLAT`, `RAISED`, `SUNKEN`, `RIDGE`, `GROOVE`, `SOLID`). |
'''
#Eg Frame Example 

import tkinter as tk 

root=tk.Tk()
root.title("Frmae")
root.geometry("500x500")

frame=tk.Frame(root,bg="lightblue",width=250, height=250)
frame.pack_propagate(False)
frame.pack(pady=20,padx=20)

label=tk.Label(frame,text="We are now inside the frame")
label.pack(pady=10)

button=tk.Button(frame,text="Click Me")
button.pack(pady=10)

root.mainloop()

'A.Expalnation'
import tkinter as tk              # Import the Tkinter library and give it the short name 'tk'

root = tk.Tk()                    # Create the main application window

root.title("Frame")               # Set the title of the window

root.geometry("500x500")          # Set the size of the window to 500x500 pixels


# Create a Frame inside the main window
frame = tk.Frame(
    root,                         # Place the frame inside the root window
    bg="lightblue",               # Set the background color of the frame
    width=250,                    # Set the width of the frame
    height=250                    # Set the height of the frame
)

frame.pack_propagate(False)       # Prevent the frame from shrinking to fit its contents

frame.pack(
    pady=20,                      # Add 20 pixels of vertical space around the frame
    padx=20                       # Add 20 pixels of horizontal space around the frame
)


# Create a Label inside the frame
label = tk.Label(
    frame,                        # Place the label inside the frame
    text="We are now inside the frame"  # Text displayed on the label
)

label.pack(pady=10)               # Display the label with 10 pixels of vertical padding


# Create a Button inside the frame
button = tk.Button(
    frame,                        # Place the button inside the frame
    text="Click Me"               # Text displayed on the button
)

button.pack(pady=10)              # Display the button with 10 pixels of vertical padding

root.mainloop()                   # Start the GUI event loop and keep the window running
 
'B.concepts'
'''
1.tk.Frame()
-tk.Frame() is a Tkinter widget used to create a container or section inside a GUI window.
 It is used to group and organize other widgets like labels, buttons, entry boxes, and other  
 frames. A Frame helps in creating a well-structured and organized GUI layout
 
 
 2.widget.pack_propagate()
-pack_propagate(value) is a Tkinter method used to control whether a widget (usually a Frame) 
 should automatically adjust its size according to the size of its child widgets.
-If propagation is enabled (True), the Frame size changes automatically to fit its contents.
-If propagation is disabled (False), the Frame keeps the width and height specified by the 
 programmer
-Syntax
 widget.pack_propagate(value)
 where,
 widget → The widget on which the method is applied (usually a Frame).
 value  → A Boolean value:
                      True → Allow automatic resizing (default behavior).
                      False → Keep the fixed size of the widget'''
