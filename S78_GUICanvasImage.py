'16.3 Canvas Image'
'''
-Definition:
 Displays an image on the Canvas.

-Syntax:
 canvas.create_image(x, y, image=image_object)

 Parameters:
 x,y     -> Position of image
 image   -> Image object
 anchor  -> Image alignment position
'''
#Eg canvas image Example 

import  tkinter as tk 
from PIL import Image,ImageTk
root=tk.Tk()
root.title("Canvas Image Example")

canvas=tk.Canvas(root,height=500,width=800,bg="white")
canvas.pack()

image=Image.open("National_Flag.jpeg")



photo=ImageTk.PhotoImage(image)

canvas.create_image(100,100 ,anchor=tk.NW, image=photo)

root.mainloop()


'A.Explanation '
import tkinter as tk                 # Import the Tkinter library for creating GUI applications

from PIL import Image, ImageTk       # Import Pillow library classes to open and display images in Tkinter


root = tk.Tk()                       # Create the main application window

root.title("Canvas Image Example")   # Set the title of the window


# Create a Canvas widget
canvas = tk.Canvas(
    root,                            # Place the canvas inside the main window
    height=500,                      # Set the height of the canvas
    width=800,                       # Set the width of the canvas
    bg="white"                       # Set the background color of the canvas
)

canvas.pack()                        # Display the canvas in the window


# Open the image file
image = Image.open("National_Flag.jpeg")  
# Loads the image from the given file path using Pillow


# Convert the image into a format Tkinter can display
photo = ImageTk.PhotoImage(image)    
# Converts the Pillow image object into a Tkinter-compatible image object


# Display the image on the Canvas
canvas.create_image(
    100,                             # X-coordinate position of the image
    100,                             # Y-coordinate position of the image
    anchor=tk.NW,                    # Place the image starting from the top-left corner
    image=photo                      # Image object to display
)


root.mainloop()                      # Start the GUI event loop and keep the window running


'C.concepts'
'''
1. PIL 
-PIL stands for Python Imaging Library. It is a Python library used for opening, editing,
 processing, and saving images in different formats

-Common PIL Functions
| Function               | Definition                         | Syntax                         |
| ---------------------- | ---------------------------------- | ------------------------------ |
| `Image.open()`         | Opens an image file                | `Image.open("filename")`       |
| `Image.save()`         | Saves an image file                | `image.save("filename")`       |
| `Image.resize()`       | Changes image size                 | `image.resize((width,height))` |
| `Image.rotate()`       | Rotates an image                   | `image.rotate(angle)`          |
| `ImageTk.PhotoImage()` | Converts image for Tkinter display | `ImageTk.PhotoImage(image)`    |
'''
