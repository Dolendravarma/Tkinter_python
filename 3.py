#Create Say Hello GUI App with Tkinter - Python Advanced Tutorials in Telugu - Tkinter Tutorial 3

from tkinter import *

m_w=Tk()


def say_hello():
    name=user_input.get()
    greeting='Hello ' + name +'!'
    if name!='':
        
        text.config(text=greeting)
        user_input.delete(0,END)#Name enter chesinna tharavatha empty avalili antey use this
    else:
        text.config(text='Enter you Name')

user_input=Entry(m_w,width=20,font=('Arial',10))
user_input.pack(padx=10,pady=10)

text=Label(m_w,text='Enter your Name:',font=('Arial',14))
text.pack(pady=6)

button=Button(m_w,text='say Hello!',font=('Arial',12),command=say_hello)

button.pack(pady=20)





m_w=mainloop()


#Use this command to convert to like a app pyinstaller **name of file**.py --noconsole --onefile
#use in pycham terminal and see this in in folder of pycham projects..
