student ={

    "name":"Mittal",
    "subject" :"python",
    "score":89,
    "city":"Ahmedabad"

}

for key in student.keys():
    print(key)


print("------------------------")

for value in student.values():
    print(value)

print("----------------------------")

for key,value in student.items():
    print(f"{key} = {value}")