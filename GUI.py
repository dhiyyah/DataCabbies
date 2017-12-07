import sys
from tkinter import *

def first():
    pass
    return
root = Tk()
root.title("Data Cabbies")
root.geometry("400x200")
mlabel = Label(root,text='Enter Longitude').pack()
mEntry = Entry().pack()
mlabel = Label(root,text='Enter Lattitude').pack()
mEntry1 = Entry().pack()
mlabel = Label(root,text='choose location').pack()
mbutton = Button(root,text ='OK',command = first).pack()
root.mainloop()
