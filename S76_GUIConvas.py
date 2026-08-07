'16.Canvas'
'''
-Canvas is a Tkinter widget used to draw shapes, lines, text, images, and graphics inside a GUI 
 window. It provides a drawing area where you can create custom designs and visual elements
-Syntax 
 tk.Canvas(
    parent,
    width=value,
    height=value,
    bg="color"
 )

 where,
| Parameter | Description                                    |
| --------- | ---------------------------------------------- |
| `parent`  | The window or frame where the Canvas is placed |
| `width`   | Sets the width of the Canvas                   |
| `height`  | Sets the height of the Canvas                  |
| `bg`      | Sets the background color of the Canvas        |

'''

'16.1. Canvas rectangle'
'''
-Definition:
 Creates a rectangle shape on the Canvas.

-Syntax:
canvas.create_rectangle(x1, y1, x2, y2, options)

where,
 x1, y1  -> Top-left corner coordinates
 x2, y2  -> Bottom-right corner coordinates
 fill    -> Rectangle fill color
 outline -> Border color
 width   -> Border thickness

'''
#Eg Canvas rectangle Example

import tkinter as tk 
root=tk.Tk()
root.title("Canvas Example")
root.geometry("500x800")

canvas=tk.Canvas(root,height=300, width=300 , bg="white")
canvas.pack(pady=20)

canvas.create_rectangle(70,50,200,130, fill="red")

root.mainloop()


'A.Explanation'

import tkinter as tk                  # Import the Tkinter library for creating GUI applications

root = tk.Tk()                        # Create the main application window

root.title("Canvas Example")           # Set the title of the window

root.geometry("500x800")               # Set the window size to 500 pixels wide and 800 pixels high


# Create a Canvas widget
canvas = tk.Canvas(
    root,                              # Place the canvas inside the main window
    height=300,                        # Set the height of the canvas
    width=300,                         # Set the width of the canvas
    bg="white"                         # Set the background color of the canvas
)

canvas.pack(pady=20)                   # Display the canvas with 20 pixels of vertical padding


# Draw a rectangle on the canvas
canvas.create_rectangle(
    70,                                # X-coordinate of the top-left corner
    50,                                # Y-coordinate of the top-left corner
    200,                               # X-coordinate of the bottom-right corner
    130,                               # Y-coordinate of the bottom-right corner
    fill="red"                         # Fill the rectangle with red color
)


root.mainloop()                        # Start the GUI event loop and keep the window open

'B.Concepts'
'''
B.1.tk.Canvas()
-tk.Canvas() is a Tkinter widget used to create a drawing area in a GUI application.
 It allows you to draw shapes, lines, text, images, and graphics on the screen
 
B.2.Most Important Canvas Methods
| Method               | Use                    |
| -------------------- | ---------------------- |
| `create_rectangle()` | Draw rectangle         |
| `create_oval()`      | Draw circle/oval       |
| `create_line()`      | Draw line              |
| `create_text()`      | Add text               |
| `create_arc()`       | Draw arc               |
| `create_polygon()`   | Draw polygon           |
| `create_image()`     | Add image              |
| `delete()`           | Remove objects         |
| `move()`             | Move objects           |
| `coords()`           | Change/get coordinates |



# 2. canvas.create_oval()

# Definition:
# Creates a circle or oval shape on the Canvas.

# Syntax:
canvas.create_oval(x1, y1, x2, y2, options)

Parameters:
x1, y1  -> Top-left boundary coordinates of the oval
x2, y2  -> Bottom-right boundary coordinates of the oval
fill    -> Oval fill color (inside color)
outline -> Border color of the oval
width   -> Border thickness
dash    -> Creates a dashed border style for the oval
start   -> Starting angle of the arc portion (in degrees)
extent  -> Amount of arc to draw (in degrees)

# Example:
canvas.create_oval(50, 50, 150, 150, fill="blue")




# 3. canvas.create_line()

# Definition:
# Creates a line between two or more points.

# Syntax:
canvas.create_line(x1, y1, x2, y2, options)

# Parameters:
# x1, y1  -> Starting point
# x2, y2  -> Ending point
# fill    -> Line color
# width   -> Line thickness
# dash    -> Creates dashed line

# Example:
canvas.create_line(20, 20, 200, 100, fill="black", width=3)




# 4. canvas.create_text()

# Definition:
# Displays text on the Canvas.

# Syntax:
canvas.create_text(x, y, options)

# Parameters:
# x, y    -> Position of text
# text    -> Text to display
# fill    -> Text color
# font    -> Font style and size

# Example:
canvas.create_text(150, 100, text="Hello", fill="green")




# 5. canvas.create_arc()

# Definition:
# Creates a part of a circle (arc) on the Canvas.

# Syntax:
canvas.create_arc(x1, y1, x2, y2, options)

# Parameters:
# x1, y1  -> Top-left boundary
# x2, y2  -> Bottom-right boundary
# start   -> Starting angle
# extent  -> Arc angle size
# fill    -> Arc fill color

# Example:
canvas.create_arc(50, 50, 200, 200, start=0, extent=180, fill="yellow")




# 6. canvas.create_polygon()

# Definition:
# Creates a polygon shape using multiple points.

# Syntax:
canvas.create_polygon(x1,y1,x2,y2,x3,y3, options)

# Parameters:
# x,y points -> Coordinates of polygon corners
# fill       -> Polygon fill color
# outline    -> Border color

# Example:
canvas.create_polygon(100,50,200,150,50,150,fill="orange")




# 7. canvas.create_image()

# Definition:
# Displays an image on the Canvas.

# Syntax:
canvas.create_image(x, y, image=image_object)

# Parameters:
# x,y     -> Position of image
# image   -> Image object
# anchor  -> Image alignment position

# Example:
canvas.create_image(100,100,image=my_image)



# 8. canvas.delete()

# Definition:
# Deletes objects from the Canvas.

# Syntax:
canvas.delete(item)

# Parameters:
# item -> Object ID or "all"

# Example:
canvas.delete("all")




# 9. canvas.move()

# Definition:
# Moves a Canvas object from one position to another.

# Syntax:
canvas.move(item, x_amount, y_amount)

# Parameters:
# item       -> Object ID
# x_amount   -> Horizontal movement
# y_amount   -> Vertical movement

# Example:
canvas.move(rectangle, 20, 10)




# 10. canvas.coords()

# Definition:
# Gets or changes the coordinates of a Canvas object.

# Syntax:
canvas.coords(item, coordinates)

# Parameters:
# item        -> Object ID
# coordinates -> New position values

# Example:
canvas.coords(rectangle, 100,100,200,200)
'''