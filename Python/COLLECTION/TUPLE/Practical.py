t = ()

print(t)
"""---------------------------------"""

t = 10,20,30,40
print(t)
print(type(t))

"""------------------------------"""
t = (100)  #INT

print(t)

print(type(t))
"""----------------------------------"""
t = (100,) 

print(t)

print(type(t))

"""----Tuple do not modify directly-----------------"""

"""t = (10,20,30)

t[0]=100

print(t)"""

"""____________modify through list_______"""


t = 10,20,30,40

l1 = list(t)

l1[0] = 100

t = (l1)

print(t)

"""-----------------------------------------"""

"""
there is no method like append,
extend,remove...

"""

t1 = 10,20,30,40

t2= 1,2,3,4,5

t3 = t1 + t2

print(t3)

"""-----------------------------------"""

"""Operations___________"""

t1 = 20,30,40,45

t2 = t1*3

print(t1)

print(t2)

print(max(t1))

print(min(t1))

print(sum(t1))

#print(sorted(t1)) #list

print(len(t1))

print(tuple(sorted(t1)))


"""________index and count________"""

t1 = 10,20,30,40,50,10

print(t1.index(20))#1

print(t1.count(10)) #2

"""______Membership operation_____"""

t_area = "CG ROAD","NIKOL","SG HIGHWAY"

if "NIKOL" in t_area:
    print("yes exits")
else:
    print("not exits")    

""""--------------------------"""

t = [10,20,30,40,50]

print(t[0])

print(t[1:3])

"""--------------------------------"""

#unpacking of tuple

t1 = ("Mittal","DA",89)

name,subject,score=t1

print(t1)
print(name)
print(subject)
print(score)

"""_______________________________________"""


