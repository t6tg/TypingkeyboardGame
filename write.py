from tkinter import *
from tkinter import messagebox
gui = Tk()
gui.title("เพิ่มคำ")
gui.configure(bg="#801243")
#--variable--#
word = IntVar()
name = StringVar()
wo = StringVar()
#----#
def reset():
    global wo
    wo.set("")
def add():
    global name,word,wo
    n = name.get()
    w = word.get()
    w2 = wo.get()
    f = open('word.txt', 'a')
    if w2 == "":
        messagebox.showerror("Error", "ห้ามเป็นช่องว่าง")
    else :
        f.write("\n"+w2)
    f.close()
    reset()
def onclick(event=None):
    add()
gui.bind('<Return>', onclick)
l1 = Label(gui,text="เพิ่มคำ",fg="white",bg="#801243").place(x=230,y=30)
e = Entry(gui,textvariable=wo,width=20)
e.place(x=160,y=60)
e.focus()
b = Button(gui,text="เพิ่มคำ",width=21,height=2,command=onclick).place(x=160,y=120)
gui.minsize(500,300)
gui.maxsize(500,300)
gui.mainloop()
