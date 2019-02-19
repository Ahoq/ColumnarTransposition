from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import numpy as np
import math
import pandas as pd
import string

class Application(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        style = ttk.Style()     # Create style
        style.configure("Blue.TFrame", background="blue") # Set bg color
        self.config(style='Blue.TFrame')    # Apply style to widget
      
        
    def create_widgets(self):
        label1 = Label(self, text="Enter Text:")
        label1.grid(row=0,column=0)
        self.txt1 = Entry(self,width=30)
        self.txt1.grid(row=1,column=0)
        label2 = Label(self, text="Enter a key:")
        label2.grid(row=2,column=0)
        self.txt2 = Entry(self,width=30)
        self.txt2.grid(row=3,column=0)
        label3 = Label(self, text="Result:")
        label3.grid(row=4,column=0)
        self.txt3 = Entry(self,width=30)
        self.txt3.grid(row=5,column=0)
        self.button1 = Button(self, text="Encrypt")
        self.button1.grid(row=6,column=0)
        self.button1["command"] = self.encrypt
        self.button2 = Button(self, text="Refresh")
        self.button2.grid(row=7,column=5)
        self.button2["command"] = self.refresh1
        
        label4 = Label(self, text="Text:")
        label4.grid(row=8,column=0)
        self.txt4 = Entry(self,width=30)
        self.txt4.grid(row=9,column=0)
        label5 = Label(self, text="Key:")
        label5.grid(row=10,column=0)
        self.txt5 = Entry(self,width=30)
        self.txt5.grid(row=11,column=0)
        label6 = Label(self, text="Result:")
        label6.grid(row=12,column=0)
        self.txt6 = Entry(self,width=30)
        self.txt6.grid(row=13,column=0)
        self.button3 = Button(self, text="Decrypt")
        self.button3.grid(row=14,column=0)
        self.button3["command"] = self.decrypt


    def refresh1(self):
        self.txt1.delete(0, "end")
        self.txt1.update()
        self.txt2.delete(0, "end")
        self.txt2.update()
        self.txt3.delete(0, "end")
        self.txt3.update()
        self.txt4.delete(0, "end")
        self.txt4.update()
        self.txt5.delete(0, "end")
        self.txt5.update()
        self.txt6.delete(0, "end")
        self.txt6.update()

    
    def encrypt(self):
        def caesar(text, step):
            alphabets = (string.ascii_lowercase, string.ascii_uppercase, string.digits)
            def shift(alphabet):
                return alphabet[step:] + alphabet[:step]

            shifted_alphabets = tuple(map(shift, alphabets))
            joined_aphabets = ''.join(alphabets)
            joined_shifted_alphabets = ''.join(shifted_alphabets)
            table = str.maketrans(joined_aphabets, joined_shifted_alphabets)
            return text.translate(table)
        ss = caesar(self.txt1.get(), int(self.txt2.get()))
        self.txt3.insert(INSERT,ss)
        self.txt4.insert(INSERT,self.txt3.get())
        self.txt5.insert(INSERT,self.txt2.get())

    def decrypt(self):
        def caesar1(text, step):
            alphabets = (string.ascii_lowercase, string.ascii_uppercase, string.digits)
            def shift(alphabet):
                return alphabet[step:] + alphabet[:step]

            shifted_alphabets = tuple(map(shift, alphabets))
            joined_aphabets = ''.join(alphabets)
            joined_shifted_alphabets = ''.join(shifted_alphabets)
            table = str.maketrans(joined_shifted_alphabets,joined_aphabets)
            return text.translate(table)
        ss1= caesar1(self.txt4.get(), int(self.txt5.get()))
        self.txt6.insert(INSERT,ss1)
        
root = Tk()
root.title("Caesar Cipher")
root.geometry("368x352")
app = Application(root)


root.mainloop()