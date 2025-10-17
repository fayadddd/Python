
# vector
class towDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class ThreeDVector(towDVector):
    def __init__(self,i,j,k):
        super(). __init__(i,j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = towDVector(1,2)
a.show()

b = ThreeDVector(9,11,5)
b.show()


# Dog bark

class Animal:
    pass

class pets(Animal):
    pass

class Dog(pets):
    @staticmethod
    def Bark():
        print("Bow Bow!")

X = Dog()
X.Bark() 


# Employe

class Employe:
    salary = 200
    increment = 20

    @property                 # for new adding value will be replace in here and calculate
    def SalaryAfterIncrement(self):
        return(self.salary + self.salary * (self.increment/100))

    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary) -1)*100


X = Employe()
print(X.SalaryAfterIncrement)
X.SalaryAfterIncrement = 250.9
print(X.increment)


# Complex number 

class Complex:
    def __init__(self, r,i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex (self.r + c2.r, self.i + c2.i)

    def __str__(self):
        return f"{self.r} + {self.i} i"

c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1 + c2)


# Vector implementation

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)  # Same dimension vector

print(v1 + v2)  # Output: Vector(5, 7, 9)
print(v1 * v2)  # Output: 32

print(v1 + v3)  # Output: Vector(8, 10, 12)
print(v1 * v3)  # Output: 50
