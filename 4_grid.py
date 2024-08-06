#Grid system:

from tkinter import *

m_w=Tk()


my_label1=Label(m_w,text='Iam learning program ',font=('Arial',20),fg='red')#here fg means foregroung it's change the text color
my_label2=Label(m_w,text='from the youtube channel',font=('Arial',20),fg='blue')
my_label3=Label(m_w,text='so it is very heplful',font=('Arial',20),fg='green')

#Instead of using this pack() we can use the grid method:
#my_label1.pack()
#my_label2.pack(side=RIGHT)


#here iwant to create a button:

my_button=Button(m_w,text='click mee',font=('Arial',20),bg='#26C6DA')#we can keep Hex code color also

my_label1.grid(row=0,column=0)#so doing the positiong grid is so useful for us:
my_label2.grid(row=1,column=1)
my_label3.grid(row=2,column=2)

#my_button.pack()#e should not use the pack here use grid

my_button.grid(row=2,column=1,padx=10,pady=10)


m_w.mainloop()
