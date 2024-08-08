#How to Create Windows ::....
#how to create multiple windows

from tkinter import *
from PIL import Image, ImageTk

# Initialize the main window
mw = Tk()
mw.title('Main window')
mw.geometry('400x300')

# Global variable to store the image
img = None

def open_window():
    global img
    # Create a second window (Toplevel widget)
    second = Toplevel()
    second.title('Second window')
    second.geometry('400x350')

    # Load the image and place it in a label
    img = ImageTk.PhotoImage(Image.open('C:/Users/nares/OneDrive/Desktop/images/nature.jpg'))
    img_label = Label(second, image=img)
    img_label.pack(padx=10, pady=10)

    # Create an "Exit window" button that closes the second window
    exit_btn = Button(second,text='Exit window', font=('', 50), command=second.destroy)
    exit_btn.pack(padx=20, pady=20)

# Create a button in the main window to open the second window
ow_btn = Button(mw, text='Open second window', font=('', 16), command=open_window)
ow_btn.pack(pady=(60, 0))

# Start the Tkinter event loop
mw.mainloop()



