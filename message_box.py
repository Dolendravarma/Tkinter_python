#How to Create Message Box - Tkinter::..

from tkinter import *
from tkinter import messagebox

mw = Tk()

mw.title('Message Box')
mw.geometry('400x300')

def show_msg():
    # messagebox.showinfo('This is a message Box','Naresh is genius')
    # showinfo will give you a sound when you click
    
    # messagebox.showwarning('This is a message Box','Naresh is genius')
    # showwarning will give you the warning symbol.
    
  #  res = messagebox.showerror('This is a message Box', 'Naresh is genius')
  #  Label(mw, text=res, font=('', 16)).pack(pady=(20, 0))
    # showerror will give you the error symbol X


   # res = messagebox.askyesno('This is a message Box', 'Naresh is genius')   
   # Label(mw,text=res,font=('',16)).pack(pady=(20,0))
    #this askyesno will show you a message with yes no options which you want to click


  #  res = messagebox.askokcancel('This is a message Box', 'Naresh is genius')   
  #  Label(mw,text=res,font=('',16)).pack(pady=(20,0))

    res = messagebox.askquestion('This is a message Box', 'Do you want to save this file?')   
    if res=='yes':
    
        Label(mw,text='File has been saved!',font=('',16)).pack(pady=(20,0))
    
    else:
        messagebox.showwarning('This is a Message Box','Your File is trashed!')
    
    
mybutton = Button(mw, text='Show Message', font=('', 16), command=show_msg)
mybutton.pack(pady=(50, 0))

mw.mainloop()
