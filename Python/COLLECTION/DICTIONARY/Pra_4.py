student ={

    "name":"Mittal",
    "subject" :"python",
    "score":89,
    "city":"Ahmedabad"
}

print(student)

print(student.get("city"))

print(student.clear())
print(student)


student.update({

    "department" : "It",
    "state" : "Gujrat"
})

print(student)