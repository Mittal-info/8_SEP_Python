from tkinter import Label
from tkinter import Button
from tkinter import *

screen = Tk()

screen.geometry("500x500")
screen.config(background="blue")


btn1 = Button(screen,text="+ INCREMENT",font=('arial',26,'bold'))
btn1.place(x = 50 ,y =50)

lable = Label(screen,text="1",font=('arial',26,'bold'))
lable.place(x = 50 ,y =180)

btn2 = Button(screen,text="- DECREMENT",font=('arial',26,'bold'))
btn2.place(x = 50 ,y =270)

screen.mainloop()