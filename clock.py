#How to Create Digital Clock - Python in Tkinter::..

from tkinter import *
from time import strftime


mw=Tk()
mw.title('Digital-clock')
mw.geometry('630x135')#when we want to keep this size only permenetly then use this down line
mw.minsize(630,135)
mw.maxsize(630,135)
mw.config(bg='black')


def time():
    cur_time=strftime('%I:%M:%S %p')
    clock_label.config(text=cur_time)
    clock_label.after(1000,time)#what this line do is onece this line was executed  again it will call this function it's like recurssion..

clock_label=Label(mw,text='Digital-clock',font=('Arial',80),bg='black',fg='#03fc3d',padx=5,pady=5)
clock_label.pack()

time()

mw.mainloop()
