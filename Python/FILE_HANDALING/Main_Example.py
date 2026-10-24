import datetime

f = open("vaccination_report.txt","a")

name = input("Enter your name:")
age = input("Enter your age:")
gender = input("Enter your gender:")
contact = input("Enter your contact:")
vaccination_report = input("Enter vaccination status: yes / no :")

current_time = datetime.datetime.now()

f.write("\n-------------------------")
f.write("\n"+str(current_time)+"\n")
f.write("\nName:"+name)
f.write("\nAge:"+age)
f.write("\nGender:"+gender)
f.write("\nContact:"+contact)
f.write("\nvaccination_status :"+vaccination_report)

print("Report saved !")

f.close()