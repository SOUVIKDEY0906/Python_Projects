from tkinter.ttk import *
from tkinter import *
from time import *
from tkinter.font import BOLD
import pyglet

pyglet.font.add_file('D:\\python\\projects\\clock_widget\\DigitalNumbers-Regular.ttf')


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text = time_string)

    day_string = strftime("%A")

    date_string = strftime("%B %d, %Y")
    date_label.config(text = date_string+','+str(day_string))

    window.after(1000, update)

window  = Tk()
window.title("Digital_Clock")
window.configure(background="#2F2926")
window.resizable(0,0)
# window.overrideredirect(1)

time_label = Label(window, font =("DigitalNumbers-Regular", 40, 'bold'),fg ="#2F2927", bg ="#2F2926")
time_label.master.wm_attributes('-transparentcolor','#2F2926')
time_label.master.geometry('+1200+0')
time_label.pack(anchor='c')

date_label = Label(window, font =("DigitalNumbers-Regular.", 15, BOLD),bg ='#2F2926',fg ='#2F2927')
date_label.pack(anchor='c')


update()

window.mainloop()