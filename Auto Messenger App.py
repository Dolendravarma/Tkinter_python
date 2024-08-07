#How to Create Auto Messenger App using Python Tkinter::


from tkinter import *
import pyautogui as pag
from threading import *
import time




        

m_w=Tk()

m_w.title('Auto Messenger')
img=PhotoImage(file='C:\\Users\\nares\\PycharmProjects\\socket_prog\\butter.png')
m_w.iconphoto(False,img)


def justcheck(check):
    if check:
        send_button.config(text='Running....',state='disabled')
        
    else:
        send_button.config(text='start Running....',state='normal')
        
    
        

 
class AutoMessenger(Thread):
    hmt_c=5
    wt_c=3
    msg_c='Running'

    
    def run(self):
        justcheck(True)
        i=1
        while True:
    
            time.sleep(self.wt_c) 
            pag.typewrite(self.msg_c)
            pag.press('Enter')
            if self.hmt_c==i:
                justcheck(False)
                break
            i=i+1
        


#createing the function:
def messenger(hmt,wt,msg):
    print(hmt,'times')
    print(wt,'seconds')
    print(msg)
    
    send=AutoMessenger()
    send.hmt_c=int(hmt)
    send.wt_c=float(wt)
    send.msg_c=msg
    send.daemon=True #daemon is used when we close the app then automatically it will close at the background
    send.start()

    



#creating the widgets:

hmt_label=Label(m_w,text='How many times :',font=('Arial',14),fg='red')
hmt_e=Entry(m_w,width=5,font=('Arial',18))
hmt_times=Label(m_w,text='times(0 to infinite times):',font=('Arial',12))
            
wt_e=Entry(m_w,width=5,font=('Arial',18))
wt_label=Label(m_w,text='waiting time:',font=('Arial',14),fg='green')           
wt_sec=Label(m_w,text='seconds:',font=('Arial',12))
           
msg_label=Label(m_w,text='Message:',font=('Arial',14),fg='blue')
msg_e=Entry(m_w,width=30,font=('Arial',18))

send_button=Button(m_w,text='Start Sending',font=('Arial',14),command=lambda:messenger(hmt_e.get(),wt_e.get(),msg_e.get()),bg='orange')

           
#showing widgets
hmt_label.grid(row=0,column=0,padx=10,pady=15,sticky=E)
hmt_e.grid(row=0,column=1,padx=10,pady=15,sticky=W)
hmt_times.grid(row=0,column=1,padx=130,pady=15,sticky=W)

wt_label.grid(row=1,column=0,padx=10,pady=15,sticky=E)
wt_e.grid(row=1,column=1,padx=10,pady=15,sticky=W)
wt_sec.grid(row=1,column=1,padx=130,pady=15,sticky=W)


msg_label.grid(row=2,column=0,padx=10,pady=15,sticky=E)#sticky means like directions E,W,N,S
msg_e.grid(row=2,column=1,padx=10,pady=15,sticky=W)


send_button.grid(row=3,column=1,pady=20)

m_w.mainloop()

