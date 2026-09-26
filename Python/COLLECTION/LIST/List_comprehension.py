"""

List comprehension: is a most powerfull topic of list
  concept which is mainly use to convert list into sorter way

  syntax:

   list = [Element loop condition]     

"""
#without list comprehension

l1 = []

for i in range(1,6):
    l1.append(i)

print(l1)
"""-----------------------------------------"""

l1 = []

for i in range(1,6):
    value = i+10
    l1.append(value)

print(l1)

# With list comprehension

l1 = [i for i in range(1,6)]
print(l1)

"""---------------------------------------"""

l1 = [i+10 for i in range(1,6)]
print(l1)