import random

print("random between 0-1")
print(random.random())

print("random between 1-10")
print(random.randint(1,10))

print("now generate 4 digit random")
print(random.randint(1111,9999))

print("random choice from string")
s1 = "PYTHON"
print(random.choice(s1))