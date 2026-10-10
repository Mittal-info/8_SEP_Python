import os

#os.mkdir("HELLO")  folder created

if os.path.exists("HELLO"):
    print("ALREADY EXITS !")
else:
    os.mkdir("HELLO")
    print("Folder created !")    