from tkinter import Button
from tkinter import *


screen = Tk()

screen.geometry("350x300")

btn1 = Button(screen,text="btn1",font=('arial',26,'bold'))
btn1.pack()

btn2 = Button(screen,text="btn2",font=('arial',26,'bold'))
btn2.pack(side=LEFT)

btn3 = Button(screen,text="btn3",font=('arial',26,'bold'))
btn3.pack(side=RIGHT)

btn4 = Button(screen,text="btn4",font=('arial',26,'bold'))
btn4.pack(side=BOTTOM)

screen.mainloop()