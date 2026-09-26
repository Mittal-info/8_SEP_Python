'''

list : list is a collection of data type 
      which is contain similer dis-similer data element.

    list is a orderable,indexable,mutable data types.

    mutable: means we can change element after creation.

    list which is represent by [] braces.  

'''

l1 = []
print(l1)

"""--------------------------------------------"""

l1 = ["fruit","milk","bread"]
print(l1)

"""---------------------------------------------"""

for item in l1:
    print(item)

"""---------------------------------------------""" 
"""
  find the length of list
"""   
shopping_list = ["fruit","milk","bread"]

print(len(shopping_list))

"""---------------------------------------------"""

count = 0

for item in shopping_list:
    count+=1
    print(count)

"""---------------------------------------------"""

""" Access list or list indexing"""

l1 = [10,52,89,63,32,27]

print(l1[0]) # 0th index

"""
 0   1   2   3   4   5  (+) positive indexing
10, 52, 89, 63, 32, 27
-6  -5  -4  -3   -2  -1 (-) nagative  indexing
"""
print(l1[3]) 

print(l1[-4])

print(l1[-1])

"""
list slicing::

l1 = [10,52,89,63,32,27]

 0   1   2   3   4   5  (+) positive indexing
10, 52, 89, 63, 32, 27
-6  -5  -4  -3   -2  -1 (-) nagative  indexing
"""
l1 = [10,52,89,63,32,27]

print(l1[0:2])

print(l1[4:6])

print(l1[-6:-4])

print(l1[2:])

print(l1[4::])


