
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# First Class
# def btnclick():
#     messagebox.showinfo("Title","LALALALALA")
#
# w = Tk()
# w.title("First Window")
# w.iconbitmap("icon.ico")
# w.configure(background="#000000")
# w.geometry("400x400")
# w.resizable(False,False)
#
# # pack
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="red",activebackground="pink",foreground="pink",activeforeground="red",width=20,command=btnclick).pack(pady = 20)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="red",activebackground="pink",foreground="pink",activeforeground="red",width=20,command=btnclick).pack(pady = 20)
# w.mainloop()

# 2nd Class

w = Tk()
w.title("First Window")
w.iconbitmap("icon.ico")
w.configure(background="#000000")
w.geometry("500x400")
w.resizable(False,False)

# Pack
#
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="red",activebackground="pink",foreground="pink",activeforeground="red",width=20).pack(side=TOP)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="red",activebackground="pink",foreground="pink",activeforeground="red",width=20).pack(side=BOTTOM)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="red",activebackground="pink",foreground="pink",activeforeground="red",width=20).pack(side=LEFT)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="red",activebackground="pink",foreground="pink",activeforeground="red",width=20).pack(side=RIGHT)

# Grid

# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).grid(row=0,column=0)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).grid(row=1,column=1)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).grid(row=0,column=2)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).grid(row=1,column=3)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).grid(row=0,column=4)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).grid(row=2,column=0)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).grid(row=2,column=2)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).grid(row=3,column=3)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).grid(row=2,column=4)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).grid(row=3,column=1)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).grid(row=4,column=0)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).grid(row=4,column=2)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).grid(row=4,column=4)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).grid(row=5,column=1)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).grid(row=5,column=3)

# place
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).place(x= 100, y = 0)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).place(x= 200, y = 0)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).place(x= 300, y = 0)
#
#
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).place(x= 100, y = 50)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).place(x= 200, y = 50)
# Button(w,text = "Click ME",font= ("Times new roman" ,  12 ,"italic"),background="white",activebackground="pink",foreground="pink",activeforeground="white",width=10).place(x= 300, y = 50)

# Label(w,text="This is Text",fg = "red",bg="black",font=("", 18)).place(x = 0, y = 0)
# Entry(w,borderwidth=2,width=30).place(x = 150, y = 3)

# Get Textbox Value
# def myfunc():
#     fnam = fname.get()
#     lnam = lname.get()
#     gen = gender.get()
#     cont = con.get()
#     contww = contt.get()
#     fullname = fnam + lnam
#     fulname.set(fullname+" " + gen + " " + cont + " " + contww)
#
# fname = StringVar()
# lname = StringVar()
# fulname = StringVar()
# gender = StringVar()
# con = StringVar()
# contt = StringVar()
# contt.set(value="Select Country")
# gender.set(value= " ")
# con.set(value= "Select Country")
#
#
# Label(w, text="Enter First Name",bg = "black", fg = "white", font = ("", 18)).grid(row = 0 , column= 0)
# Entry(w, textvariable=fname).grid(row=0, column=1)
#
# Label(w, text="Enter Last Name",bg = "black", fg = "white", font = ("", 18)).grid(row = 1 , column= 0)
# Entry(w, textvariable=lname).grid(row=1, column=1)
#
# Button(w, text = "Click",width=30, command = myfunc).grid(row = 2, column = 0, columnspan=2,pady=10)
#
# Label(w, text="Result" ,bg = "black", fg = "white", font = ("", 18)).grid(row = 3 , column= 0)
# Entry(w,  textvariable=fulname, state=DISABLED,width=40).grid(row=3, column=1)
#
# Label(w, text="Select Gender" ,bg = "black", fg = "white", font = ("", 18)).grid(row = 4 , column= 0)
# col = 1
#
# # Radio Button
# gender_define = [
#     ("Male","M"),
#     ("Female","F"),
#     ("Rather Not to Say","No")
# ]
#
# for a in gender_define:
#     Radiobutton(w,
#                 text=a[0],
#                 value=a[1],
#                 variable=gender).grid(row = 4, column = col)
#     col = col + 1
#
# country = ["Pakistan", "India", "Bangladesh"]
# # DropDown
# OptionMenu(w, con, *country).grid(row = 5 , column= 0)
#
# # ComboBox
# ttk.Combobox(w,values=country , textvariable=contt).grid(row = 6 , column= 0)
import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="",
    database = "Arts"
)

m = db.cursor()
def click():
    a = name.get()
    b = num.get()
    if a == "" or b == 0.0:
        messagebox.showerror("Error","All Fields are Required")
    else:
        i = "INSERT INTO `user`( `Name`, `Age`) VALUES(%s,%s)";
        v = [a,b]
        m.execute(i ,v)
        db.commit()
        messagebox.showinfo("Save","Data Saved")


name = StringVar()
num = DoubleVar()

Label(w, text = "Enter Name", font=("times new roman", 15), bg = "black", fg = "white").pack()
Entry(w, textvariable=name).pack()

Label(w, text = "Enter Number", font=("times new roman", 15), bg = "black", fg = "white").pack()
Entry(w, textvariable=num).pack()

Button(w,text = "Click", command= click).pack(pady= 10)
w.mainloop()

