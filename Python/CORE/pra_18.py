even_count = 0
odd_count = 0

for i in range(1,6):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)#print(f"Even numbers: {even_count}")
print("Odd numbers:", odd_count)

