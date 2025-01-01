'''
TKINTER
 '''
 def result():
    global res
    res['text'] = ''
    val = inp.get()
    if val.isdigit() and val:
        res = tk.Label(win, text=f'{round((int(val)*0.0022),4)} $',
                       font=('Arial', 16, 'bold'),
                       bg='#3C4255',
                       fg='white'
                       )
    else:
        res = tk.Label(win, text='ошибка',
                       font=('Arial', 16, 'bold'),
                       bg='#3C4255',
                       fg='white'
                       )
    res.grid(row=4, column=6, columnspan=4, stick='w')


def result2():
    global res2
    res2['text'] = ''
    val2 = inp2.get()
    if val2.isdigit() and val2:
        res2 = tk.Label(win, text=f'{round((int(val2)*462.81),4)} KZT',
                        font=('Arial', 14, 'bold'),
                        bg='#3C4254',
                        fg='white'
                        )
    else:
        res2 = tk.Label(win, text='ошибка',
                        font=('Arial', 16, 'bold'),
                        bg='#3C4254',
                        fg='white'
                        )

    res2.grid(row=10, column=6, columnspan=4, stick='w')


import tkinter as tk

# create window
win = tk.Tk()
win.title('converter')
win.geometry('400x350+100+100')
win.maxsize(400, 350)
win.minsize(400, 350)
win.config(bg='#3C4254')

# labels
text1 = tk.Label(win, text='конвертор USD/KZT',
                 font=('Arial', 20, 'bold'),
                 bg='#282F41',
                 fg='white'
                 )

text2 = tk.Label(win, text='введите сумму (теңге): ',
                 fg='white',
                 font=('Arial', 16, 'bold'),
                 bg='#3C4254'
                 )

text3 = tk.Label(win, text='результат: ',
                 font=('Arial', 16, 'bold'),
                 bg='#3C4254',
                 fg='white'
                 )
res = tk.Label(win, text=' 0 $',
               font=('Arial', 16, 'bold'),
               bg='#3C4254',
               fg='white'
               )

text4 = tk.Label(win, text='введите сумму (dollar): ',
                 font=('Arial', 16, 'bold'),
                 bg='#3C4254',
                 fg='white'
                 )

text5 = tk.Label(win, text='результат: ',
                 font=('Arial', 16, 'bold'),
                 bg='#3C4254',
                 fg='white'
                 )
res2 = tk.Label(win, text=' 0',
                font=('Arial', 16, 'bold'),
                bg='#3C4254',
                fg='white'
                )

# input
inp = tk.Entry(win)
inp2 = tk.Entry(win)

# buttons
bnt = tk.Button(win, text='oк',
                font=('Arial', 16, 'bold'),
                command=result,
                fg='white',
                bg='#282F41',
                relief=tk.RAISED,
                bd=0,
                activebackground='#212736',
                activeforeground='white'
                )
bnt2 = tk.Button(win, text='oк',
                 font=('Arial', 16, 'bold'),
                 command=result2,
                 fg='white',
                 bg='#282F41',
                 relief=tk.RAISED,
                 bd=0,
                 activebackground='#212736',
                 activeforeground='white'
                 )

# packing
text1.grid(row=0, column=2, stick='w', columnspan=10)
text2.grid(row=2, column=1, stick='we', columnspan=10)
inp.grid(row=3, column=2, stick='we', columnspan=5)
text3.grid(row=4, column=1, stick='we', columnspan=5)
bnt.grid(row=3, column=8, stick='we', columnspan=2)
res.grid(row=4, column=5, columnspan=2)

text5.grid(row=10, column=1, stick='we', columnspan=5)
inp2.grid(row=9, column=2, stick='we', columnspan=5)
text4.grid(row=8, column=1, stick='we', columnspan=10)
bnt2.grid(row=9, column=8, stick='we', columnspan=2)
res2.grid(row=10, column=5, columnspan=2)

# ending
win.grid_columnconfigure(0, minsize=40)
win.grid_rowconfigure(1, minsize=30)
win.grid_rowconfigure(3, minsize=20)
win.grid_rowconfigure(5, minsize=50)
win.mainloop()

# palete
'''
#3C4254 - background
#212736 - button on
#282F41 - buttons off
'white' - shift
'''
