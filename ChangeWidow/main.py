# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

# creates a Tk() object
master = Tk()

# sets the geometry of main
# root window
master.geometry("200x200")


# function to open a new window
# on a button click
def openNewWindow():
    # Toplevel object which will
    # be treated as a new window

    master2 = Tk()

    # sets the geometry of main
    # root window
    master2.geometry("200x200")

    # A Label widget to show in toplevel
    Label(master2,
          text="This is a new window").pack()
    master.destroy()

label = Label(master,
              text="This is the main window")

label.pack(pady=10)

# a button widget which will open a
# new window on button click
btn = Button(master,
             text="Click to open a new window",
             command=openNewWindow)
btn.pack(pady=10)

# mainloop, runs infinitely
mainloop()