#Exception : is a parent class which we can import or inherite in our own exception class

class AgeNotValid(Exception):# here,AgeNotValid is an userdefined exception
  pass

age =int(input("Enter your age:"))

if age < 18:
    raise AgeNotValid("You are below 18:")     
             