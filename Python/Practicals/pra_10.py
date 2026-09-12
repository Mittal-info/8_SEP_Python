'''
control statements:

there are three types of control statements in python:
1. Conditional statements
2. Looping statements
3. Jump statements


1. Conditional statements:

i)if statement:

  syntax:
  if condition:
      statement(s)

ii)if-else statement:

  syntax:
  if condition:
      statement(s)
  else:
      statement(s)

iii)if-elif-else statement:

  syntax:
  if condition1:
      statement(s)
  elif condition2:
      statement(s)
  else:
      statement(s)

iv)nested if statement:

  syntax:
  if condition1:
      if condition2:
          statement(s)

iv)match statement:

  syntax:
  match value:
      case pattern1:
          statement(s)
      case pattern2:
          statement(s)
      case _:
          statement(s)

'''

age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")

'''------------------------------------------------------------'''
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")    
else:
    print("The number is odd.")

