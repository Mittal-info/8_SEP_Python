"""
json file:
     
   json stands for javascript object notation

"""

import  json

user ={

    'name' : 'mittal',
    'sub'  :'python',
    'score': 89
}

with open("myjsonfile.json","w") as f:
    json.dump(user,f,indent=4)

print("successfully file created !")