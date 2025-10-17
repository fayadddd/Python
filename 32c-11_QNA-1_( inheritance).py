
'''
class X:
    company = "NASA"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Y:
    company = "Google" 
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

a = X()
b = Y()
print(a.company,b.company)



# shortcut

class X:
    company = "NASA"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Y(X):
    company = "Google" 
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

a = X()
b = Y()
print(a.company,b.company)


# Multiple inheritance

class X:
    company = "NASA"
    name = "issac"
    salary = 120000
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Z:
    language = "python"
    def show1(self):
        print(f"the language is : {self.language}")

class Y(X,Z):
    company = "Google" 
    def show2(self):
        print(f"The company name is {self.company} and the salary is {self.salary}")

b = Y()
#b.show()
#b.show1()
b.show2()


# Multilevel ineritance

class Employee:
    a = 1 

class Programmer(Employee):
    b = 2 

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # Shows an error as there is no b attribute in Employee class

o = Programmer()
print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)


# super mathod 
class Gari:
    def __init__(self, model):  # Corrected: __init__ instead of __int__
        self.model = model
    
    @staticmethod                #Decorator
    def start():
        print("car start...")

    @staticmethod                #Decorator
    def stop():
        print("car stop...")

class ToyotaCar(Gari):
    def __init__(self, name, model):  # Corrected: __init__ instead of __int__
        super().__init__(model)  # Initialize the parent class (Gari)
        self.name = name  # Initialize the name attribute

# Create an instance of ToyotaCar
gari1 = ToyotaCar("MARK", "2")
print(gari1.model)  # Output: 2
print(gari1.name)   # Output: MARK
'''
# Dander Function
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def ShowNumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2):
        NewReal = self.real + num2.real
        Newimg = self.img + num2.img
        return Complex(NewReal,Newimg)

num1 = Complex(1,3)
num1.ShowNumber()

num2 = Complex(4,6)
num2.ShowNumber()

num = num1 + num2
num.ShowNumber()