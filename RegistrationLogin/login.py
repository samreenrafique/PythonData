from tkinter import *
from tkinter import messagebox
import mysql.connector

class Login:
    def __init__(self,b):
        self.c = b;
        self.c.geometry("500x500")
        self.c.title("Registration")
        self.c.config(bg="#b6c4c4")
        Button(self.c, text="Go to Registration", bg="#3e7e7d", command=self.go_to_register).place(x=150, y=190)

    def go_to_register(self):
        self.c.destroy()
        import main

root = Tk()
b = Login(root)
root.mainloop()