from tkinter import *
from tkinter import ttk,messagebox
import string
import random
import pyperclip

def generate_password():
    try:
        length = int(pswd_length.get())
        level = option.get()
        pswd = []
        characterlist = []
        if length >= 8:
            if  level == "Select Level":
                messagebox.showerror("Error","Kindly Select any Level")
            elif level == "Easy":
                characterlist = list(string.ascii_uppercase + string.ascii_lowercase)
            elif level == "Medium":
                characterlist = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
            elif level == "Hard":
                characterlist = list(string.ascii_uppercase + string.ascii_lowercase +string.digits + string.whitespace + "!@#$%^&*()")

            for a in range(length):
                pswd.append(random.choice(characterlist))

            passwordgen = "".join(pswd)
            gen_pswd.set(passwordgen)
        else:
            messagebox.showerror("Error", "Length Must be Greater than 7")
    except Exception as e:
        messagebox.showerror("Error", e )
def copy_text():
    pswd = gen_pswd.get()
    if len(pswd) != 0:
        pyperclip.copy(pswd)
    else:
        messagebox.showerror("Error", "There is nothing to Copy")

root = Tk()
pswd_length = StringVar()
gen_pswd  = StringVar()
option = StringVar()
options = ["Easy", "Medium" , "Hard"]
option.set(value="Select Level")
Label(root,text="Enter Password Length").grid(row = 0 , column=0)
Entry(root,textvariable=pswd_length).grid(row=0, column = 1)
Label(root,text="Select Option").grid(row=1 , column=0,pady=10)
ttk.Combobox(root, textvariable= option, values= options).grid(row=1 , column=1,pady=10)
Button(root,text="Generate",bg="white",command=generate_password).grid(row=2 , column=0,pady=10)
Button(root,text="Copy",bg="white",command=copy_text).grid(row=2 , column=1,pady=10)
Label(root,text="Generated Password").grid(row = 3 , column=0)
Entry(root,textvariable=gen_pswd).grid(row=3, column = 1)


root.mainloop()
