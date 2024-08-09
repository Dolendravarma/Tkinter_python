#How to Open File Dialog - Python:::...

from tkinter import *
from tkinter import filedialog
#To display image in another window we want to import PIL

from PIL import Image,ImageTk

mw=Tk()

mw.title('Main window')
#mw.iconbitmap('C:/Users/nares/OneDrive/Desktop/images/nature.jpg')
mw.geometry('300x200')


img=''

def open_file():
    global img
    filename=filedialog.askopenfilename(initialdir='C:/Users/nares/OneDrive/Desktop/images',title='select a file',
                                    filetypes=(('JPG Files','*.jpg'),('All Files','*.*')))


    sw=Toplevel()
    sw.title('Image window')
    sw.geometry('800x500')

    
    
    img=ImageTk.PhotoImage(Image.open(filename))
    img_label=Label(sw,image=img)
    img_label.pack(padx=10,pady=10)
        

btn=Button(mw,text='open file',font=('',16),command=open_file)
btn.pack(pady=(60,0))



mw.mainloop()
