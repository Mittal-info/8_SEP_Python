
"""1)append():: 

  syntax:

    list.append()
    variable.append(new value)
"""

l1 = [12,30,50,45]
print(l1)
l1.append(63)
print(l1)


"""----------------------------------------------------------------------"""

# ACCEPT 3 VALUES FROM USER:

subject_list = [] # blank list

for i in range(1,4):

    subject = input("enter subject name:")
    subject_list.append(subject)

    print(subject_list)



    """_________________________________________________________________"""

    fruit_list = []

status = True

while status:

    fruit_name = input("Enter fruit name:")
    fruit_list.append(fruit_name)

    choice = input("do you want to add fruit so press Y another N::").lower()

    if choice == 'N' or choice == 'No':
          status = False

    else:
         status = True

print(fruit_list)      