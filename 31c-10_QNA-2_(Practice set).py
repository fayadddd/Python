
# company programer details
class programer:
    company = "Microsoft"
    
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
    
X = programer("Fayad",1500000,2345)                             
print(X.name, X.salary, X.pincode, programer.company)

X1 = programer("Yamal",1300000,23456)                             
print(X1.name, X1.salary, X1.pincode, programer.company)


# class calculator
class calculator:
    def __init__(self,n):
        self.n = n
    
    def square(self):
        print(f"The square is {self.n* self.n}")

    def cube(self):
        print(f"The cube is {self.n* self.n* self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n* self.n* 1/2}")

X = calculator(5)
X.square()
X.cube()
X.squareroot()


#
class Demo:
    a = 4
X = Demo()
print(X.a)            # prints the class attribute because instance attribute is not present       
X.a = 0               # instance attribute is set
print(X.a)            # prints the instance attribute becasue instance attribute is present
print(Demo.a)         # prints the class attribute


# train details
import random

class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo
    
    def booked(self,frome,to):
        print(f"Ticket is booked in tarin number:{self.trainNo} from {frome} to {to}")
    def getStatus(self):
        print(f"Train number:{self.trainNo} is running on time ")
    def getFare(self,frome,to):
        print(f"Ticket fare in tarin number:{self.trainNo} from {frome} to {to} is {random.randint(111,555)}")

X = Train(2001)
X.booked("DHAKA" , "COX")
X.getStatus()
X.getFare("DHAKA" , "COX")


# Students Exm Marks

class Students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("Hi", self.name, "Your average score is:",sum/3)

student_1 = Students("fAYAD",[88,92,90])
student_1.average()


# Bank credit and debit
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("BDT.", amount , "was debited")
        print("total balance =", self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("BDT.", amount, "was creadited")
        print("total balance =",self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000,12352)
acc1.debit(10000)
acc1.credit(5500)


