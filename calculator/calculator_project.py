from tkinter import *
from numpy import *

def button_press(num):
    global equation_text
    equation_text= equation_text + str(num)
    eqaution_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        eqaution_label.set(total)
        equation_text = total

    except ZeroDivisionError:
        eqaution_label.set("arithmetic error")
        equation_text = ""

    except SyntaxError:
        eqaution_label.set("Syntax error")
        equation_text = ""

def clear():
    global equation_text
    eqaution_label.set("")
    equation_text = ""

window = Tk()
window.title("Calcualtor")
window.geometry("280x440")
window.resizable(0,0)
equation_text = ""
eqaution_label = StringVar()

label = Label(window, textvariable= eqaution_label, text =('Arial',50, 'bold'), bg = 'white', width =36, height = 2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=6,font=35,
command= lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=6,font=35,
command= lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=6,font=35,
command= lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=6,font=35,
command= lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=6,font=35,
command= lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=6,font=35,
command= lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=6,font=35,
command= lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=6,font=35,
command= lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=6, height=4, width=6,font=35,
command= lambda: button_press(6))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=6,font=35,
command= lambda: button_press(0))
button0.grid(row=3, column=1)

plus = Button(frame, text='+', height=4, width=6,font=35,
command= lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=6,font=35,
command= lambda: button_press('-'))
minus.grid(row=1, column=3)

mul = Button(frame, text='*', height=4, width=6,font=35,
command= lambda: button_press('*'))
mul.grid(row=2, column=3)

div = Button(frame, text='/', height=4, width=6,font=35,
command= lambda: button_press('/'))
div.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=6,font=35,
command= lambda: equals())
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=6,font=35,
command= lambda: button_press('.'))
decimal.grid(row=3, column=0)

clr = Button(window, text='C', height=2, width=9,font=35,
command= lambda: clear())
# clr.grid(row=4, column=1)
clr.pack()


window.mainloop()