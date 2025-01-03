'''
TKINTER
'''

def add_digit(digit):
    val = calc.get() + str(digit)
    if val[0] == '0' and len(val) == 2:
        calc.delete(0, tk.END)
        calc.insert(0, str(digit))
    elif val[:5] == 'ERROR':
        calc.delete(0, tk.END)
        calc.insert(0, str(digit))
    else:
        calc.delete(0, tk.END)
        calc.insert(0, val)


def m_result_b(digit):
    val = calc.get()
    try:
        s = round(eval(val), 5)
    except:
        s = 'ERROR'

    calc.delete(0, tk.END)
    calc.insert(0, s)


def m_delete_b(oper):
    val = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, '0')


def add_operation(operation):
    val = calc.get()
    if len(val) > 0 and val[-1] in '-+/*':
        val = val[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, val + operation)


def operation_button(oper):
    return tk.Button(text=oper, bd=0,
                     command=lambda: add_operation(oper),
                     font=('Arial', 15),
                     fg='white',
                     bg='#302A2A'
                     )


def m_num_b(num):
    return tk.Button(text=num, bd=0,
                     bg='#3C3939',
                     command=lambda: add_digit(num),
                     font=('Arial', 15),
                     fg='white'
                     )


def m_o_b(oper):
    return tk.Button(text=oper, bd=0,
                     command=lambda: add_operation(oper),
                     font=('Arial', 15),
                     bg='#302A2A',
                     fg='white'
                     )


def m_del_b(oper):
    return tk.Button(text=oper, bd=0,
                     command=lambda: m_delete_b(oper),
                     font=('Arial', 15),
                     bg='#302A2A',
                     fg='white'
                     )


def m_res_b(oper):
    return tk.Button(text=oper, bd=0,
                     command=lambda: m_result_b(oper),
                     font=('Arial', 15),
                     bg='#302A2A',
                     fg='white'
                     )


import tkinter as tk

# create/config window
win = tk.Tk()
win.title('calculator')
win.geometry('245x295+100+100')
win.maxsize(245, 295)
win.minsize(245, 295)
win['bg'] = '#1E1F1F'
win['bd'] = 0
icon = tk.PhotoImage(file='icon2.png')
win.iconphoto(False, icon)

# entry
calc = tk.Entry(win, justify=tk.RIGHT,
                font=('Arial', 18),
                width=15,
                background='#3C3939',
                fg='white',
                bd=0
                )
calc.grid(row=0, column=0, columnspan=4, stick='wens', padx=5, pady=5)

# buttons: num
m_num_b('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
m_num_b('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
m_num_b('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
m_num_b('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
m_num_b('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
m_num_b('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
m_num_b('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
m_num_b('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
m_num_b('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
m_num_b('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

# buttons: operation
operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
operation_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
operation_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)

# button calculation
m_del_b('del').grid(row=4, column=1, stick='wens', padx=5, pady=5)
m_res_b('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)

# window config
win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)
win.grid_columnconfigure(4, minsize=60)

win.grid_rowconfigure(0, minsize=50)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

# ending
win.mainloop()


'''
palete

#3C5451 - bg
4E6967 - btn
4E6967 - title
'''
