# methods , instance variables, class variables, constructor 
# Class name start with Capital Case.
class Calculator:
    num = 100   #Class variable accessible withn any method in the Class and constant across object
                # and needs to be called within the class using class name eg. Calculator.num or self.num
                # Fields: Data attached to an object


    def __init__(self, a, b): # Constructor is called first and the name is __init__
        self.firstNumber = a   # instance variable differs for every object 
        self.secondNumber = b  # instance variable differs for every object
        print("I am called automatically when object is created")

    def getData(self): # Method
        print('I am now executing as method in class')

    def Summation(self):
        return self.firstNumber + self.secondNumber  + Calculator.num 




obj1 = Calculator(3, 4) #syntax to create an object from the class, an instance of the class
obj1.getData()
print(obj1.Summation())


obj2 = Calculator(4, 6) #syntax to create an object from the class
obj2.getData()
print(obj2.Summation())