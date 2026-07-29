'GUI - Graphical User Interface'
'''
-GUI
-Graphical User Interface is a user-friendly interface 
 that allows users to interact with a computer program through
 graphical elements such as buttons, icons, menus, and window

-Tkinter
 Tkinter is the standard GUI library in Python that is used to create graphical applications using windows,
 buttons, labels, and other GUI elements
 
 -Widget 
  -A widget is a graphical element used to create the user interface of an application.
  -It allows users to interact with the program through elements like buttons, labels, text boxes, and menus

-Common GUI Elements in Python Tkinter

| No. | Graphical Element | Syntax                                  | What it does                                                       |
| --- | ----------------- | --------------------------------------- | ------------------------------------------------------------------ |
| 1   | **Window (Tk)**   | `window = tk.Tk()`                      | Creates the main application window.                               |
| 2   | **Label**         | `tk.Label(window, text="Hello")`        | Displays text or information on the window.                        |
| 3   | **Button**        | `tk.Button(window, text="Click")`       | Creates a clickable button to perform an action.                   |
| 4   | **Entry**         | `tk.Entry(window)`                      | Creates a single-line text input box.                              |
| 5   | **Text Box**      | `tk.Text(window)`                       | Allows users to enter multiple lines of text.                      |
| 6   | **Checkbutton**   | `tk.Checkbutton(window, text="Option")` | Creates a checkbox to select or deselect an option.                |
| 7   | **Radiobutton**   | `tk.Radiobutton(window, text="Male")`   | Allows users to select one option from multiple choices.           |
| 8   | **Listbox**       | `tk.Listbox(window)`                    | Displays a list of items from which users can choose.              |
| 9   | **Combobox**      | `ttk.Combobox(window)`                  | Creates a drop-down list of options.                               |
| 10  | **Frame**         | `tk.Frame(window)`                      | Groups and organizes other GUI elements.                           |
| 11  | **Menu**          | `tk.Menu(window)`                       | Creates menus like File, Edit, Help, etc.                          |
| 12  | **Canvas**        | `tk.Canvas(window)`                     | Used for drawing shapes, images, and graphics.                     |
| 13  | **Scale**         | `tk.Scale(window)`                      | Creates a slider to select a value.                                |
| 14  | **Spinbox**       | `tk.Spinbox(window)`                    | Allows users to select values by increasing or decreasing numbers. |
| 15  | **Message**       | `tk.Message(window, text="Info")`       | Displays longer text messages.                                     |
| 16  | **Scrollbar**     | `tk.Scrollbar(window)`                  | Adds scrolling ability to widgets like Text and Listbox.           |
'''

'1.Window(Tk())'
'''
-Tk is the main window or root window of a Tkinter GUI application. It creates the basic application window 
where all other GUI elements like buttons, labels, text boxes, and menus are placed
-syntax
window = tk.Tk()
where,

| Part     | Meaning                              |
| -------- | ------------------------------------ |
| `window` | Stores the main GUI window.(root)    +|
| `=`      | Assigns a value.                     |
| `tk`     | Tkinter module name (alias).         |
| `Tk()`   | Creates the main application window. |
'''

#Eg 01 Window Example
import tkinter as tk

root =tk.Tk()
root.title("First Window")
root.geometry("500x500")
root.mainloop()

'A.Explanation'
'''

| Code                         | Explanation                                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `root = tk.Tk()`             | Creates the **main GUI window**. `Tk()` is a Tkinter function that starts the application window. `root` stores this window so we can control it. |
| `root.title("First Window")` | Sets the **title of the window**. The text `"First Window"` appears on the top title bar.                                                         |
| `root.geometry("500x500")`   | Sets the **size of the window**. Here, the window width is **500 pixels** and height is **500 pixels**.                                           |
| `root.mainloop()`            | Keeps the window **open and running**. It waits for user actions like clicks and keyboard input.                                                  |

'''

'B.Concepts '
'1.root'
'''
-root is a variable name that stores the main GUI window created by tk.Tk()
-When we create a GUI window using tk.Tk(), we need a name to refer to that 
 window later. The variable root is commonly used for this purpose.'''


'2.tk.Tk()'
'''
-tk.Tk() is the function used to create the main/root window of a Tkinter GUI application
-In a GUI program, everything needs a main window (the base screen) where all other graphical
 elements like buttons, labels, text boxes, menus, and images are placed. The tk.Tk() function
 creates this main window and starts the connection between Python and the computer's 
 graphical system'''

'3.root.title()'
'''
-root.title(" ") is a Tkinter method used to set or change the title of the main GUI window
-In a GUI application, the title bar is the top area of the window that tells the user the name
 or purpose of the application. The title() method allows the programmer to give a meaningful name to the window.
-The text inside root.title() is written in double quotes (" ") because it is a string (text value'''

'4.root.geometry()'
'''
-root.geometry("width x height") is a Tkinter method used to set the size of the main GUI window
-In a GUI application, every window has a specific width and height. The geometry() method controls 
 how big or small the application window appears on the screen
-The size value is written inside double quotes (" ") because geometry() expects a string format,
 not separate integer values
-Format is always width × height (in pixels)
-small x denotes as by (width by height )
-Why not use integers?
 Because geometry() does not take two separate numbers. It expects one string that describes the
 complete window size
'''

'5.root.mainloop()'
'''
-root.mainloop() is a Tkinter method used to start and keep the GUI application running until the user 
 closes the window.
-In a GUI application, the program must continuously listen for user actions like button clicks, 
 keyboard input, and mouse movements. The mainloop() method creates this continuous waiting process'''


