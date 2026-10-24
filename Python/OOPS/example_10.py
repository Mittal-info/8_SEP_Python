class student:
    def __init__(self):
        self.subject = "python"
        #self.marks = 89
        self.__marks = 89

    def getMarks(self):
        return self.__marks
s1 = student()

print(s1.subject)
print(s1.getMarks())