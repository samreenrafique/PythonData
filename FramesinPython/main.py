from tkinter import *
from PIL import ImageTk,Image
w = Tk()
w.geometry("500x500")
w.title("Frame Example")
frame1 = Frame(w, bg="black",width=200,height=100)
frame1.place(x=0,y=0)

imge = PhotoImage(file=""
photo = imge.subsample(1,2)
Button(frame1,image=photo).place(x = 40,y = 10)
Label(frame1,text="Pepsi", font=("times new roman",16,"bold"),fg="blue",bg="black").place(x=70,y=60)
Button(frame1,bg="white",text="Click").place(x=75,y= 100)

w.mainloop()
