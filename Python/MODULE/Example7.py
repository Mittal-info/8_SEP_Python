import os 

print("current working directory",os.getcwd())

os.chdir("C:\\Users\\rabar\\OneDrive\\Desktop\\18-june-2026")

print("change directory",os.getcwd())

print(os.listdir())

os.mkdir("Hello")