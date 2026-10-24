class student:
    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

obj = student()
obj.setId(101)
print(obj.getId())        