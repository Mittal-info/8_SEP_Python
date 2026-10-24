import json

with open("myjsonfile.json","r") as file:
    data = json.load(file)

    print(data)
