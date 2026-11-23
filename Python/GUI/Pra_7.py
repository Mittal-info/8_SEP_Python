from tkinter import Label
from tkinter import Button
from tkinter import *
import random

screen = Tk()

screen.geometry("500x500")
screen.config(bg="teal")

user_choice = ""
computer_choice = ""

user_choice_var = StringVar()
computer_choice_var = StringVar()

user_choice_var.set("PENDING")
computer_choice_var.set("PENDING")

def userChoiceGame(user_choice):
    print(user_choice)

    user_choice_var.set(user_choice)
    game_choice_list = ["ROCK", "PAPER", "SCISSORS"]
    computer_choice = random.choice(game_choice_list)   
    computer_choice_var.set(computer_choice)

label1 = Label(screen, text="ROCK PAPER SCISSORS", font=("Arial", 20, 'bold'), bg="teal")
label1.pack()

rock_button = Button(screen, text="ROCK", font=("Arial", 15, 'bold'), bg="white", fg="black",command=lambda: userChoiceGame("ROCK"))
rock_button.place(x=10, y=60)

paper_button = Button(screen, text="PAPER", font=("Arial", 15, 'bold'), bg="white", fg="black",command=lambda: userChoiceGame("PAPER"))
paper_button.place(x=150, y=60)

scissors_button = Button(screen, text="SCISSORS", font=("Arial", 15, 'bold'), bg="white", fg="black",command=lambda: userChoiceGame("SCISSORS"))
scissors_button.place(x=300, y=60)


userbutton = Button(screen, text="USER CHOICE", font=("Arial", 15, 'bold'), bg="white", fg="black",command=lambda: userChoiceGame("SCISSORS"))
userbutton.place(x=10, y=120)

Computerbutton = Button(screen, text="COMPUTER CHOICE", font=("Arial", 15, 'bold'), bg="white", fg="black",command=lambda: userChoiceGame("SCISSORS"))
Computerbutton.place(x=10, y=180)

userbutton = Button(screen, textvariable=user_choice_var, font=("Arial", 15, 'bold'), bg="white", fg="black",command=lambda: userChoiceGame("SCISSORS"))
userbutton.place(x=10, y=240)

computerbutton = Button(screen, textvariable=computer_choice_var, font=("Arial", 15, 'bold'), bg="white", fg="black",command=lambda: userChoiceGame("SCISSORS"))
computerbutton.place(x=10, y=300)

screen.mainloop()
