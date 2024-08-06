#Create Buttons and Input Fields in GUI - Python Advanced Tutorials in Telugu - Tkinter Tutorial 2::

from tkinter import *


m_w=Tk()

def clicked():
    mylabel=Label(m_w,text='Ilove Python',font=('Arial',13))
    mylabel.pack(pady=10)


#createing userinput:
user_input=Entry(m_w,width=20,font=('Arial',15))#entry is used to create a box like.. method
user_input.pack(pady=10)



#creating buttons:
my_button=Button(m_w,text='click mee!',padx=20,pady=10,font=('Arial',14),command=clicked)#here command is used to call the function

my_button.pack(padx=50,pady=30)



m_w.mainloop()
