#Graphical User Interface App in Python | Python Advanced Tutorials| Tkinter Tutorial 1::..

from tkinter import *

#creating a window:

main_window=Tk()

mylabel=Label(main_window,text='Welcome to Tkinter..',font=('Arial',20),padx=30,pady=30)#so here fon t will generate the size of the text. and padx is known as the padding will give the space of the text from left and right of the text and another one is pady it also known as the padding and it is of space bteween top and bottom of the text

mylabel.pack(side=RIGHT)#so this pack method will add our text into a screen or window so pack antey mana text entha varaku undh anthavaraku compress iyipodhi anamata
#so in pack there is FOUR types LEFT,RIGHT,TOP,BOTTOM AND TOP is default.)
#DEFAULT IT IS IN THE TOP


main_window.mainloop()






from tkinter import *

main_window = Tk()

mylabel = Label(main_window, text='Hello Naresh', bg='pink', font=('Helvetica', 20), padx=20, pady=25)

mylabel.pack()

main_window.mainloop()


