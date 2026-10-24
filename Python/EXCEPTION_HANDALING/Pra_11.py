try:
    num1 =int(input("Enter number 1:"))
    num2 =int(input("Enter number 2:"))
    ans = num1 / num2
except ZeroDivisionError:
    print("Not devide by zero")
except ValueError:
    print("invalid input")
else:
    print(ans)
finally:
    print("Thank you for using this application !")                
