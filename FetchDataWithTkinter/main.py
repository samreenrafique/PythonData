from tkinter import *
import requests
from bs4 import BeautifulSoup
import pandas

class GUI:
    def __init__(self, root):
        self.root = root
        self.name = StringVar()
        self.root.geometry("300x300")
        Label(self.root, text = "Enter Name").pack()
        Entry(self.root,textvariable=self.name).pack(pady=15)
        Button(self.root, text="Fetch",command=self.wescrapping).pack(pady=15)

    def wescrapping(self):
        self.d = self.name.get()
        self.url = "https://www." + self.d + ".tv/"
        self.request = requests.get(self.url)
        if  self.request.status_code == 200:
            self.content = self.request.content
            self.khoobsurat = BeautifulSoup(self.content,"html.parser")
            self.findp = self.khoobsurat.find_all("p")
            self.text = []

            for self.b in self.findp:
                self.text.append(self.b.get_text())
            self.dict ={
                "news":self.text
            }
            self.tab = pandas
            self.file = open("myfile.txt","a+")
            self.file.write(str(self.text))
            self.file.close()


r = Tk()
a = GUI(r)
r.mainloop()

