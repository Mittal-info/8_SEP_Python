import random

print("NUMBER GUESSING GAME")
print("----------------------------------------")
print("Guess number between 1 to 100")

computer = random.randint(1,100)

status = True

while status:
    user_num = int(input("Enter a number:"))

    if user_num > computer:
        print("HINT: Guess below number")
    elif user_num < computer:
        print("HINT: Guess upper number")
    else:
        print("You won")  

        status =False