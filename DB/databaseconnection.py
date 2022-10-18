from tkinter import *
from tkinter import ttk
import pymysql

def datajao():
    name = username.get()
    email = useremail.get()
    pswd = userpswd.get()
    gender = usergender.get()
    country = usercountry.get()
    
    


root = Tk()
root.geometry("300x250")
root.title("Database Connection")

Label(root,text="Enter Name").grid(row = 0,column = 0)

username = StringVar()
Entry(root,textvariable=username).grid(row=0,column=1)

Label(root,text="Enter Email").grid(row = 1,column = 0)
useremail = StringVar()
Entry(root,textvariable=useremail).grid(row=1,column=1)

Label(root,text="Enter Password").grid(row = 2,column = 0)
userpswd = StringVar()
Entry(root,textvariable=userpswd).grid(row=2,column=1)


Label(root,text="Select Gender").grid(row = 3,column = 0)
usergender = StringVar(value=" ")
Radiobutton(root,text="Male",value="Male",variable=usergender).grid(row=3,column=1)
Radiobutton(root,text="Female",value="Female",variable=usergender).grid(row=3,column=2)

Label(root,text="Select Country").grid(row = 4,column = 0)
country = ["Pakistan","Bangladesh","India","Srilanka","Iran"]
usercountry = StringVar(value="Country")
ttk.Combobox(root,values = country,textvariable=usercountry).grid(row=4,column = 1)

Button(root,text="Save Data").grid(row = 6,column = 1)
root.mainloop()
