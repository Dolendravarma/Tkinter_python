from tkinter import *

mw = Tk()

mw.title('Calculator')

# Function to clear the display
def clear():
    dbox.delete(0, END)

# Function to handle button click and display
def btn_clk(num):
    cur_num = dbox.get()
    dbox.delete(0, END)
    dbox.insert(0, cur_num + num)

# Creating function for calculation based on math_type
def calc(math_type, ms):
    cur_num = dbox.get()
    if cur_num[-1] in '+-*/':
        cur_num = cur_num[:-1]
    dbox.delete(0, END)
    dbox.insert(0, cur_num + ms)

# Creating function for "=" button
def equal():
    expression = dbox.get()
    clear()
    try:
        result = eval(expression)  # Evaluate the full expression
        dbox.insert(0, str(result))
    except Exception as e:
        dbox.insert(0, 'Error')

# Creating the widgets
dbox = Entry(mw, width=14, font=('Arial', 28), justify=RIGHT)

btn_0 = Button(mw, text='0', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('0'))
btn_1 = Button(mw, text='1', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('1'))
btn_2 = Button(mw, text='2', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('2'))
btn_3 = Button(mw, text='3', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('3'))
btn_4 = Button(mw, text='4', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('4'))
btn_5 = Button(mw, text='5', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('5'))
btn_6 = Button(mw, text='6', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('6'))
btn_7 = Button(mw, text='7', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('7'))
btn_8 = Button(mw, text='8', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('8'))
btn_9 = Button(mw, text='9', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_clk('9'))
btn_clear = Button(mw, text='Clear', padx=74, pady=10, font=('Arial', 14), command=clear)
btn_div = Button(mw, text='/', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('div', '/'))
btn_mult = Button(mw, text='*', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('mult', '*'))
btn_sub = Button(mw, text='-', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('sub', '-'))
btn_add = Button(mw, text='+', padx=36, pady=10, font=('Arial', 14), command=lambda: calc('add', '+'))
btn_eq = Button(mw, text='=', padx=36, pady=40, font=('Arial', 14), command=equal)

# Showing the widgets
btn_sub.grid(row=6, column=0, padx=2, pady=2)
btn_add.grid(row=6, column=1, padx=2, pady=2)
btn_div.grid(row=5, column=0, padx=2, pady=2)
btn_mult.grid(row=5, column=1, padx=2, pady=2)
btn_eq.grid(row=5, column=2, rowspan=2, padx=2, pady=2)
btn_clear.grid(row=4, column=1, columnspan=2, padx=2, pady=2)
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
dbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

mw.mainloop()
