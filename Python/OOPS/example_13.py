""""class Vehicle:
    def vehicle_type(self):
        print("This is a vehicle")


class Specification(Vehicle):
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def show_specification(self):
        print("Color:", self.color)
        print("Wheels:", self.wheels)


class Bike(Specification):
    def __init__(self, color, wheels, brand):
        super().__init__(color, wheels)
        self.brand = brand

    def show_bike(self):
        self.vehicle_type()
        self.show_specification()
        print("Brand:", self.brand)


b1 = Bike("Black", 2, "Honda")
b1.show_bike()"""

"""-------------------------------------------------------"""


class A:
    def displayA(self):
        print("A class is here")

class B:
    def displayB(self):
        print("B class is here")
        
class C(A,B):
    def displayC(self):
        print("C class is here")

object = C()

object.displayA()
object.displayB()