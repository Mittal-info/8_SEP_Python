import os

#os.remove("Hello.txt")  for remove the file

if os.path.exists("HELLO"):
    os.rmdir("HELLO")
else:
    print("FOLDER DOES NOT EXISTS")    