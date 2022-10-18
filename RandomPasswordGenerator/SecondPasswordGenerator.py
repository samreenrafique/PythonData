from tkinter import *
from tkinter import ttk,messagebox
import string
import random
import pyperclip

def generate_pswd():
    ab = uletter.get()
    b = lletter.get()
    c = specialcharac.get()
    d = number.get()

    uppercasecharacter,lowercasecharacter,specialcharacter, gennumber = [],[],[],[]

    upperletter = list(string.ascii_uppercase)
    lowerletter = list(string.ascii_lowercase)
    special_character = list("!@#$%^&*(),<>?/")
    digits = list(string.digits)

    for a in range(ab):
        uppercasecharacter.append(random.choice(upperletter))

    for a in range(b):
        lowercasecharacter.append(random.choice(lowerletter))

    for a in range(c):
        specialcharacter.append(random.choice(special_character))

    for a in range(d):
        gennumber.append(random.choice(digits))

    generated_pswd = uppercasecharacter + lowercasecharacter + specialcharacter + gennumber
    update = "".join(generated_pswd)
    gen_pswd.set(update)

root = Tk()
gen_pswd  = StringVar()

uletter = IntVar()
lletter = IntVar()
specialcharac = IntVar()
number = IntVar()

Label(root,text="Enter Upper Case Count").grid(row = 0 , column=0)
Entry(root,textvariable=uletter).grid(row=0, column = 1)

Label(root,text="Enter Lower Case Count").grid(row = 1 , column=0)
Entry(root,textvariable=lletter).grid(row=1, column = 1)

Label(root,text="Enter Special Character Count").grid(row = 2 , column=0)
Entry(root,textvariable=specialcharac).grid(row=2, column = 1)

Label(root,text="Enter Number Count").grid(row = 3 , column=0)
Entry(root,textvariable=number).grid(row=3, column = 1)

Label(root,text="Generated Password").grid(row = 4 , column=0)
Entry(root,textvariable=gen_pswd).grid(row=4, column = 1)

Button(root,text="Generate",bg="white",command=generate_pswd).grid(row=5, column=0,pady=10)
Button(root,text="Copy",bg="white").grid(row=5, column=1,pady=10)

root.mainloop()
