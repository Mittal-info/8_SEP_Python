f = open("UserDetails.txt","w")

name = input("Enter your name")

age = int(input("Enter your age:"))


f.write("Name: " + name + "\n") #f.write(name)
f.write("Age: " + str(age)) #f.write(str(age))

f.close()



