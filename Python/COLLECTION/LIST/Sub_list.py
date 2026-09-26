subject_list = []

status = True

while status:
    subject = input("Enter subject :")

    if subject not in subject_list:

     subject_list.append(subject)

     print(f"'{subject}' Added !!")

    else:
       print(f"'{subject}' Already Exits !!")

    choice = input("Do you want to add more sub : press n for no and y for yes:" )

    if choice== 'n' or choice == 'no':   

       status=False

print(subject_list)

