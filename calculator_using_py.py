#How to Create Calculator in Python - Tkinter ::..

from tkinter import *

mw=Tk()

mw.title('calculator')

#creating the function for celar button:

def clear():
    dbox.delete(0,END)

#ceating the button for button click display
def btn_clk(num):
    cur_num=dbox.get()
    clear()
    f_num=cur_num + num
    #dispaly box
    dbox.insert(0,f_num)#insert is used to insert the number


#certaing function for add symbol
first_num=0
math=''

def calc(math_type):#insted of writing all the functions like add,sub,mult,div we can write a function called as calc in that we can keep all the add,sub,mult,div
    global first_num,math
    math=math_type
    first_num=dbox.get()#get anadhi manam ee number ithey first theskunatomoo dhanini first lo padesidhii
    clear()

#Creating function for =

def equal():
    result=''
    global first_num
    second_num=dbox.get()
    clear()#after taking the second number clear the display
    if math=='add':
        result=int(first_num) + int(second_num) #if we don't keep the int it will consider it as the string 

    elif math=='sub':
         result=int(first_num)-int(second_num)

    elif math=='mult':
         result=int(first_num)*int(second_num)         

    elif math=='div':
         result=int(first_num)/int(second_num)
         result=round(result,4)
                  
    dbox.insert(0,str(result))
    
    



#creating the widgets
dbox=Entry(mw,width=14,font=('Arial',28),justify=RIGHT)#so in calculator numbers will come from right t left so that we want to use the justify



btn_0=Button(mw, text='0',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('0'))
btn_1=Button(mw, text='1',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('1'))
btn_2=Button(mw, text='2',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('2'))
btn_3=Button(mw, text='3',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('3'))
btn_4=Button(mw, text='4',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('4'))
btn_5=Button(mw, text='5',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('5'))
btn_6=Button(mw, text='6',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('6'))
btn_7=Button(mw, text='7',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('7'))
btn_8=Button(mw, text='8',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('8'))
btn_9=Button(mw, text='9',padx=36,pady=10,font=('Arial',14),command=lambda:btn_clk('9'))
btn_clear=Button(mw,text='Clear',padx=74,pady=10,font=('Arial',14),command=clear)
btn_div=Button(mw,text='/',padx=38,pady=10,font=('Arial',14),command=lambda:calc('div'))
btn_mult=Button(mw,text='*',padx=38,pady=10,font=('Arial',14),command=lambda:calc('mult'))
btn_sub=Button(mw,text='-',padx=38,pady=10,font=('Arial',14),command=lambda:calc('sub'))
btn_add=Button(mw,text='+',padx=36,pady=10,font=('Arial',14),command=lambda:calc('add'))
btn_eq=Button(mw,text='=',padx=36,pady=40,font=('Arial',14),command=equal)





#showing the widgets

#if we see the calculator we get first 7,8,9, numbers so that we want to write like that only

btn_sub.grid(row=6,column=0,padx=2,pady=2)
btn_add.grid(row=6,column=1,padx=2,pady=2)



btn_div.grid(row=5,column=0,padx=2,pady=2)
btn_mult.grid(row=5,column=1,padx=2,pady=2)
btn_eq.grid(row=5,column=2,rowspan=2,padx=2,pady=2)

btn_clear.grid(row=4,column=1,columnspan=2,padx=2,pady=2,)
btn_0.grid(row=4, column=0, padx=2, pady=2)


btn_1.grid(row=3, column=0, padx=2, pady=2)
btn_2.grid(row=3, column=1, padx=2, pady=2)
btn_3.grid(row=3, column=2, padx=2, pady=2)


btn_4.grid(row=2, column=0, padx=2, pady=2)
btn_5.grid(row=2, column=1, padx=2, pady=2)
btn_6.grid(row=2, column=2, padx=2, pady=2)


btn_7.grid(row=1, column=0, padx=2, pady=2)
btn_8.grid(row=1, column=1, padx=2, pady=2)
btn_9.grid(row=1, column=2, padx=2, pady=2)

#we get zero at the last so keep here
dbox.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

mw.mainloop()
