##--Assignment-Typingkeyboard--##
#--import/display--##
from tkinter import *
from random import *
import time, threading
import sys
from tkinter import messagebox
labelfont = ('times', 40, 'bold')
gui = Tk()
gui.title("พิมพ์ดีด | 6104062630301")
gui.configure(bg="pink")
##--end import--#
##--function--#
def word():
    global w,v,s
    lines = open('word.txt').read().splitlines()
    myline = choice(lines)
    w.set(myline)
    m = w
def process():
    global v,x1,time,i
    t = v.get()
    h = w.get()
    if h == t :
        s.set(int(s.get()+1))
        v.set("")
    else:
        s.set(int(s.get()+0))
        v.set("")
    print()
    word()
def alert():
    messagebox.showinfo("หมดเวลา", "หมดเวลาสนุกแล้วสิ")
    restart()
def timeout():
        process()
##--variable--#
s = IntVar()
s.set(0)
w = StringVar()
v = StringVar()
##--time--##
x1 = IntVar()
x1.set(60)
def onclick(event=None):
    timeout()

gui.bind('<Return>', onclick)

def restart():
    global x1,s
    x1.set(60)
    s.set(0)
def counter():
    x1.set((int(x1.get())-1))
    threading.Timer(1,counter).start()
counter()
l1 = Label(gui,textvariable=x1,bg="pink").place(x=760,y=20)
ltime = Label(gui,text="เวลา : ",bg="pink").place(x=710,y=19)
#--end time--#
#--score--#
ls = Label(gui,textvariable=s,bg="pink").place(x=70,y=20)
ls_socre = Label(gui,text="คะแนน : ",bg="pink").place(x=10,y=19)
#--main--#
word()
ml = Label(gui,textvariable=w,bg="pink",font=labelfont).place(x=360,y=200)
e = Entry(gui,textvariable=v,width=50)
e.place(x=200,y=300)
e.focus()
b = Button(gui,text="ส่งคำตอบ",width=20,height=2,command=onclick).place(x=320,y=400)
b2=Button(text="เริ่มเกมส์ใหม่",width=20,height=2,command=restart)
b2.place(x=320,y=550)
##--Size--#
gui.minsize(800,600)
gui.maxsize(800,600)
gui.after(60000, lambda: alert())
gui.mainloop()

