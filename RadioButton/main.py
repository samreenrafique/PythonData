#  1st Method


# from tkinter import *
#
# def selection():
#     data = "You Selected: " + selectvalue.get()
#     Label(root,text=data).place(x = 150,  y= 130)
#
# root = Tk()
# root.geometry("300x300")
#
# selectvalue = StringVar(value= " ")
#
# Label(text="Select Food").place(x = 50, y = 50)
# Radiobutton(root,text="Biryani",variable=selectvalue,value="biryani",command=selection).place(x = 150,y = 50)
# Radiobutton(root,text="Burger",variable=selectvalue,value="burger" ,command=selection).place(x = 150,y = 80)
# Radiobutton(root,text="Pizza",variable=selectvalue,value="pizza",command=selection).place(x = 150,y = 110)
#
# root.mainloop()

# from tkinter import *
#
#
# def selection():
#     selection = "You selected the option " + str(radio.get())
#     label.config(text=selection)
#
#
# top = Tk()
# top.geometry("300x150")
# radio = IntVar()
# lbl = Label(text="Favourite programming language:")
# lbl.pack()
# R1 = Radiobutton(top, text="C", variable=radio, value=1,
#                  command=selection)
# R1.pack(anchor=W)
#
# R2 = Radiobutton(top, text="C++", variable=radio, value=2,
#                  command=selection)
# R2.pack(anchor=W)
#
# R3 = Radiobutton(top, text="Java", variable=radio, value=3,
#                  command=selection)
# R3.pack(anchor=W)
#
# label = Label(top)
# label.pack()
# top.mainloop()


# 2nd Method

from tkinter import *
root = Tk()
root.geometry("300x300")

selectvalue = StringVar(value= " ")
dish = (
    ("Biryani","Pakistani"),
    ("Burger","Fast Food"),
    ("Pizza","Italian"),
    ("Spaghetti","Italian")
)

Label(root,text="Select").pack()

for s in dish:
    Radiobutton(root, text=s[0], value=s[0],variable=selectvalue).pack()

root.mainloop()