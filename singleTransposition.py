from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import numpy as np
import math
import pandas as pd
class Application(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.button_clicks = 0
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
        #self.button4 = Button(self, text="Refresh")
        #self.button4.grid(row=7,column=1)
        #self.button4["command"] = self.refresh2

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
        plaintext = self.txt1.get()
        key_0 = self.txt2.get()
        key_0 = key_0.lower()
        column_names =[]

        for character in key_0:
            num = ord(character)-96
            column_names.append(num)

        key_0_len = len(key_0)
        j_ = key_0_len

        i_ = math.ceil(len(plaintext)/j_)

        m_ = np.zeros(shape=(i_,j_),dtype='object')
        ciphertext = m_

        s_ = ""
        h_ = 0


        for x_ in range(i_): 
            for y_ in range(j_): 
                if h_ in range(len(plaintext)):
                    m_[x_][y_] = plaintext[h_]
                    h_+=1
                else:
                    m_[x_][y_] = "_"

        w_ = 0
        df = pd.DataFrame(m_, columns=column_names)
        cols = df.columns.tolist()
        cols = sorted(cols, key=int)
        df = df[cols]
        df=df.values
        for w_ in range(j_):
            sb = "".join(df[:,w_])
            s_ += sb
            w_+=1
        self.txt3.insert(INSERT,s_)
        self.txt4.insert(INSERT,self.txt3.get())
        self.txt5.insert(INSERT,self.txt2.get())

    def decrypt(self):
        
        p = self.txt4.get()
        key_0 = self.txt5.get()
        key_0 = key_0.lower()
        column_names =[]

        for character in key_0:
            num = ord(character)-96
            column_names.append(num)
        key_0_len = len(key_0)
        j = key_0_len

        i = math.ceil(len(p)/j)

        m = np.zeros(shape=(i,j),dtype='object')

        ciphertext = m

        s = ""
        w=0
        n=0
        h = 0
        for x in range(j): 
            for y in range(i): 
                if h in range(len(p)):
                    m[y][x]= p[h]
                    h+=1
                else:
                    m[y][x]='_'


        col_nms = sorted(column_names, key =int)
        df = pd.DataFrame(m, columns=col_nms)
        cols = df.columns.tolist()
        cols = column_names
        df = df[cols]
        df=df.values
        for w in range(i):
            sb = "".join(df[w,:])
            s += sb
            w+=1  
        s = s.replace("_", "")
        self.txt6.insert(INSERT,s)
        
root = Tk()
root.title("Single Transposition")
root.geometry("368x352")

app = Application(root)




root.mainloop()