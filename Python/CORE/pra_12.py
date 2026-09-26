'''
Nested if statement:

syntax:

if condition1:

    if condition2:
        statement(s)
    else:
       if condition3:
        statement(s)
else:
    statement(s)
'''

email = "mittal@gmail.com"
password = "mittal123"

user_email = input("Enter your email: ")
user_password = input("Enter your password: ")

if user_email == email:

    if user_password == password:
        print("Login successful!")

    else:
        print("Incorrect password.")

else:
    print("Email not found.")

"""-----------------------------------------------------------------------"""

"""

for loop: sequence of statements is executed multiple 
          times and abbreviates the code that manages the loop variable.

          syntax:

          for variable in sequence:
              statement(s)

"""

for i in range(1, 6):
    print(i)