#Create Frames, Radio Button, Check Box, Dropdown, Slider | Tkinter :::..


from tkinter import *

mw=Tk()
mw.title('Naresh')

#creating the geomentry to adjust the window function:.
mw.geometry('600x620')#in geometry we can ajust the size of the window

#creating the frames:
frame1=LabelFrame(mw,text='This is frame 1',width=400,padx=10,pady=10,font='14')
frame1.grid(row=0,column=0,padx=20,pady=10)


exit_btn=Button(frame1,text='Exit',padx=60,pady=12,font=('',14),command=mw.quit)
exit_btn.pack()


#creating the radio buttons:

def rv_res():
    rv_lbl.config(text=rv.get())

rv=StringVar()#definig the tkinter variable rv we can use this as string and int as per the situation
rv.set('chicken biriyani')
Radiobutton(frame1,text='option 1',value='chicken biriyani',variable=rv,font=('',14),command=rv_res).pack(pady=(30,10))
Radiobutton(frame1,text='option 2',value='veg biriyani',variable=rv,font=('',14),command=rv_res).pack(pady=(0,20))

rv_lbl=Label(frame1,text=rv.get(),font=('',14))
rv_lbl.pack()


#creating check Buttons/Boxes:.

def cv_res():
    cv_lbl.config(text=cv.get())

cv=StringVar()
cb=Checkbutton(frame1,text='Do want this house ?',variable=cv,font=('',14),command=cv_res,onvalue='Yes',offvalue='No')
cb.deselect()#if we don't keep this it will automatically be filled the box
cb.pack(pady=(30,10))

cv1=StringVar()
cb1=Checkbutton(frame1,text='Do want this house ?',variable=cv1,font=('',14),command=cv_res,onvalue='Yes',offvalue='No')
cb1.deselect()#if we don't keep this it will automatically be filled the box
cb1.pack(pady=(30,10))

cv_lbl=Label(frame1,text=cv.get(),font=('',14))

cv_lbl.pack(pady=(0,30))


#creating the Drop down menus:


months=['Januray','Febuary','March','April','May','June','July','August','September','October','November','December']
selected=StringVar()
selected.set('March')
opts=OptionMenu(frame1,selected,*months)
opts.config(font=('',14))
opts.pack(pady=(0,30))

#so we handle the menu like this remember this one
opts_menu=frame1.nametowidget(opts.menuname)
opts_menu.config(font=('',12))


#creating the sliders:

def box_ver(num_v):
    box_lbl.config(pady=num_v)

def box_hor(num_v):
    box_lbl.config(padx=num_v,pady=num_v)
    
#creating the flame2

frame2=LabelFrame(mw,text='This is frame 2',width=200,padx=10,pady=10,font='14')
frame2.grid(row=0,column=1,padx=20,pady=10)

#there are two types of sliders vertical and horizontal

ver=Scale(frame2,from_=0,to=200,command=box_ver)
ver.grid(row=0,column=0,pady=(0,20))


hor=Scale(frame2,from_=0,to=300,orient=HORIZONTAL,command=box_hor)
hor.grid(row=0,column=1,pady=(0,20))


frame3=LabelFrame(mw,text='This is frame 3',width=300,padx=10,pady=10,font='14')
frame3.grid(row=0,column=3,padx=20,pady=10)

box_lbl=Label(frame3,text='',bg='blue')
box_lbl.pack(pady=(0,20))


mw.mainloop()















