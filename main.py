import tkinter
from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry('490x490+100+100')
root.resizable(False, False)
root.configure(bg='#17161b')

equ = ''


def show(value):
    global equ
    equ += value
    label_result.config(text=equ)


def clear():
    global equ
    equ = ''
    label_result.config(text=equ)


def calculate():
    global equ
    result = ''
    if equ != '':
        try:
            result = eval(equ)
        except:
            result = 'Error'
            equ = ''
    label_result.config(text=result)


label_result = Label(root, text='', width=40,
                     height=3, font='timesnewroman 20')
label_result.pack()

butn_c = Button(text='C', width=5, height=1,
                font='arial 22 bold', bd=1, fg='#fff', bg='#36975f', command=lambda: clear(), cursor='hand2')
butn_c.place(x=15, y=110)

btn_divide = Button(text='/', width=5, height=1,
                    font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('/'))
btn_divide.place(x=135, y=110)

btn_mode = Button(text='%', width=5, height=1,
                  font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('%'))
btn_mode.place(x=255, y=110)

btn_multi = Button(text='*', width=5, height=1,
                   font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('*'))
btn_multi.place(x=375, y=110)

# Row 2
butn_7 = Button(text='7', width=5, height=1,
                font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('7'))
butn_7.place(x=15, y=185)

btn_8 = Button(text='8', width=5, height=1,
                    font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('8'))
btn_8.place(x=135, y=185)

btn_9 = Button(text='9', width=5, height=1,
               font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('9'))
btn_9.place(x=255, y=185)

btn_minus = Button(text='-', width=5, height=1,
                   font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('-'))
btn_minus.place(x=375, y=185)

# Row 3
butn_4 = Button(text='4', width=5, height=1,
                font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('4'))
butn_4.place(x=15, y=260)

btn_5 = Button(text='5', width=5, height=1,
                    font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('5'))
btn_5.place(x=135, y=260)

btn_6 = Button(text='6', width=5, height=1,
               font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('6'))
btn_6.place(x=255, y=260)

btn_plus = Button(text='+', width=5, height=1,
                  font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('+'))
btn_plus.place(x=375, y=260)

# Row 4
butn_1 = Button(text='1', width=5, height=1,
                font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('1'))
butn_1.place(x=15, y=335)

btn_2 = Button(text='2', width=5, height=1,
                    font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('2'))
btn_2.place(x=135, y=335)

btn_3 = Button(text='3', width=5, height=1,
               font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('3'))
btn_3.place(x=255, y=335)

# Zero Button
btn_0 = Button(text='0', width=12, height=1,
               font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('0'))
btn_0.place(x=15, y=410)

# dot button
btn_dot = Button(text='.', width=5, height=1,
                 font='arial 22 bold', bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('.'))
btn_dot.place(x=255, y=410)

# Equal button
btn_dot = Button(text='=', width=5, height=3,
                 font='arial 22 bold', bd=1, fg='#fff', bg='#fe903f', command=lambda: calculate())
btn_dot.place(x=375, y=340)


root.mainloop()
