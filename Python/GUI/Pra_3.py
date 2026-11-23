from tkinter import Label
from tkinter import *

screen = Tk()

screen.geometry("350x300") #wxh

lable = Label(screen,text="welcome to Tkinter",font=('arial',23,'bold'))

lable.pack()

screen.mainloop()