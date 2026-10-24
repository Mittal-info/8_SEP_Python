class student:
    def __init__(self,name,subject,score):

        self.name = name
        self.subject = subject
        self.score = score

    def display(self):
        print(self.name)
        print(self.subject)
        print(self.score)

name = input("Enter your name")
subject  = input("Enter your subject")
score = input("Enter your score")    

student = student(name,subject,score)

student.display()