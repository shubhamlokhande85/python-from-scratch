'16.2 Canvas circle'
'''
1. canvas.create_oval()

-Definition:
  Creates a circle or oval shape on the Canvas.

-Syntax:
 canvas.create_oval(x1, y1, x2, y2, options)

Parameters:
x1, y1  -> Top-left boundary coordinates of the oval
x2, y2  -> Bottom-right boundary coordinates of the oval
fill    -> Oval fill color (inside color)
outline -> Border color of the oval
width   -> Border thickness
dash    -> Creates a dashed border style for the oval
start   -> Starting angle of the arc portion (in degrees)
extent  -> Amount of arc to draw (in degrees)  '''
 
 #Eg 
import tkinter as tk 
root=tk.Tk()

root.title("Canvas Circle Example")
root.geometry("500x500")

canvas=tk.Canvas(root,height=300, width=300,bg="white")
canvas.pack(pady=20)

canvas.create_oval(50,25,150,125,fill="orange",outline="lightblue",width=2)
root.mainloop()




'A.Explanation'


import tkinter as tk                  # Import the Tkinter library for creating GUI applications

root = tk.Tk()                        # Create the main application window


root.title("Canvas Circle Example")    # Set the title of the window

root.geometry("500x500")               # Set the window size to 500x500 pixels


# Create a Canvas widget
canvas = tk.Canvas(
    root,                              # Place the canvas inside the main window
    height=300,                        # Set the height of the canvas
    width=300,                         # Set the width of the canvas
    bg="white"                         # Set the background color of the canvas
)

canvas.pack(pady=20)                   # Display the canvas with 20 pixels of vertical padding


# Draw an oval/circle on the Canvas
canvas.create_oval(
    50,                                # X-coordinate of the top-left corner
    25,                                # Y-coordinate of the top-left corner
    150,                               # X-coordinate of the bottom-right corner
    125,                               # Y-coordinate of the bottom-right corner
    fill="orange",                     # Fill the oval with orange color
    outline="lightblue",               # Set the border color of the oval
    width=2                            # Set the border thickness to 2 pixels
)


root.mainloop()                        # Start the GUI event loop and keep the window open


