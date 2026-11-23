from tkinter import *

screen = Tk()

screen.geometry("500x500")
screen.config(background="blue")

counter_var = IntVar()
counter_var.set(0)

counter = 0

# Increment function
def increment():
    global counter
    counter += 1
    counter_var.set(counter)

# Decrement function
def decrement():
    global counter
    counter -= 1
    counter_var.set(counter)

# Increment button

btn1 = Button(
    screen,
    text="+ INCREMENT",
    font=('arial', 26, 'bold'),
    command=increment
)
btn1.place(x=50, y=50)

# Counter label
label = Label(
    screen,
    textvariable=counter_var,
    font=('arial', 26, 'bold')
)
label.place(x=50, y=180)

# Decrement button
btn2 = Button(
    screen,
    text="- DECREMENT",
    font=('arial', 26, 'bold'),
    command=decrement
)
btn2.place(x=50, y=270)

screen.mainloop()