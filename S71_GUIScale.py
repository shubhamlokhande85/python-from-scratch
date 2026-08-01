'11.Scale'
'''
-A Scale is a GUI widget that lets the user select a value by moving a slider. 
 It is useful for choosing numbers such as volume, brightness, speed, or temperature
-Syntax
 scale = Scale(root, from_=0, to=100, orient=HORIZONTAL)
 where,
 root                 → The main window.
 from_                → The starting value of the scale.
 to                   → The ending value of the scale.
 orient=tk.HORIZONTAL → Displays the scale horizontally.
 orient=tk.VERTICAL   → Displays the scale vertically'''

#Eg Scale Example
import tkinter as tk

root=tk.Tk()
root.title("Scale Example")
root.geometry("500x500")

scale=tk.Scale(root,from_=0 , to=100,orient=tk.HORIZONTAL)
scale.pack(pady=20)

root.mainloop()


'A.Exaplanation'
import tkinter as tk          # Import the Tkinter library for creating GUI applications

root = tk.Tk()                # Create the main application window

root.title("Scale Example")   # Set the title of the window

root.geometry("500x500")      # Set the window size to 500 pixels wide and 500 pixels high

# Create a Scale (slider) widget
scale = tk.Scale(
    root,                     # Place the scale inside the main window
    from_=0,                  # Starting value of the scale
    to=100,                   # Ending value of the scale
    orient=tk.HORIZONTAL      # Display the scale horizontally
)

scale.pack(pady=20)           # Display the scale with 20 pixels of vertical padding

root.mainloop()               # Start the GUI event loop and keep the window open

'B.concepts'
'''
1.tk.Scale()
-tk.Scale() is a Tkinter widget used to create a slider that allows the user to select a 
 numeric value by moving a pointer between a minimum and maximum value'''

