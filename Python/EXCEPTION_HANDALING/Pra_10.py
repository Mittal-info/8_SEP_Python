ACCOUNT_BALANCE = 5000

class InsuffiecentBalance(Exception):
 pass



menu = """
        Menu:

        1)DEPOSITE
        2)WITHDRAW
"""
status = True

while status:
     print(menu)

     choice = int(input("Enter your choice:"))
     if choice ==1:
        amount =int(input("Enter deposite amount:"))
        ACCOUNT_BALANCE += amount
        print("TOTAL AMOUNT :",ACCOUNT_BALANCE)
     elif choice == 2:
        amount = int(input("Enter deposite amount:"))
        try:
           if amount > ACCOUNT_BALANCE:
              raise InsuffiecentBalance("Insuffiecent Balance")
        except InsuffiecentBalance as e:
           print(e)
        else:
           ACCOUNT_BALANCE -= amount
           print("TOTAL AMOUNT :",ACCOUNT_BALANCE)
     else:
        pass

     exit_choice = input("Are you sure you want to exit ? press y for yes and n for no:")
     if exit_choice == "y":
        status = False              