from tkinter import *
from tkinter import messagebox

import mysql.connector


class main:
    def __init__(self,b):
        self.a = b
        self.a.geometry("500x500")
        self.a.title("Registration")
        self.a.config(bg="#b6c4c4")
        self.uname = StringVar()
        self.email = StringVar()
        self.pswd = StringVar()

        Label(self.a, text="Enter Username", font=("times new roman", 15, "bold"), bg="#b6c4c4",
                         fg="#3e7e7d").place(x=0, y=10)
        Entry(self.a ,textvariable=self.uname ).place(x=150, y=15)

        Label(self.a, text="Enter Email", font=("times new roman", 15, "bold"), bg="#b6c4c4",
                         fg="#3e7e7d").place(x=0, y=80)
        Entry(self.a ,textvariable=self.email ).place(x=150, y=85)

        Label(self.a, text="Enter Password", font=("times new roman", 15, "bold"), bg="#b6c4c4",
      fg="#3e7e7d").place(x=0, y=160)
        Entry(self.a, textvariable=self.pswd).place(x=150, y=165)

        Button(self.a , text="Save Data",bg="#3e7e7d",command=self.register_login).place(x = 150, y= 190)
        Button(self.a , text="Go to Login Page",bg="#3e7e7d",command=self.go_to_login).place(x = 150, y= 220)

    def register_login(self):
        name = self.uname.get()
        mail = self.email.get()
        pswd = self.pswd.get()

        dbcon = mysql.connector.connect(host="localhost",username="root",password="",database="demodb")
        fetch = dbcon.cursor()
        q = "INSERT INTO `user`(`Name`, `Email`, `Password`) VALUES (%s,%s,%s)"
        v = [name,mail,pswd]

        loginquery = "select * from user where Email = %s"
        log_val = [mail]

        fetch.execute(loginquery,log_val)
        row = fetch.fetchone()
        if row == None:
            fetch.execute(q, v)
            dbcon.commit()
            messagebox.showinfo("Success", "Register Successfully", parent=self.a)
        else:
            messagebox.showerror("Error", "Email Already Exist",parent = self.a)

    def go_to_login(self):
        self.a.destroy()
        import login


root = Tk()
a = main(root)

root.mainloop()