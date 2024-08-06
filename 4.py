#Positioning with Grid System - Title Icon | Python Advanced Tutorials in Telugu | Tkinter Tutorial 4
#How to add title and icon

from tkinter import *


m_w = Tk()

#we can change the title icon like this:
img=PhotoImage(file='C:\\Users\\nares\\OneDrive\\Desktop\\th.jpeg')
m_w.iconphoto(False,img)
m_w.title('say hello!')


m_w=mainloop()

