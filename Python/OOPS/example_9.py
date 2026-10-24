"""
encapsulation provides data hiding using of encapsulation we can prevent records from 
outside direct access

in pyhton using of __(double underscore)
we can prevent record and make it private member

encapsulation in python does not provide fully private but yes using of
__(double underscore) we can make private member and prevent from outside the world


"""

class student:
    def __init__(self):
        self.subject = "python"
        #self.marks = 89
        self.__marks = 89

s1 = student()

print(s1.subject)
print(s1.__marks)