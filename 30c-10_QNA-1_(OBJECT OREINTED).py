
class Employe:
    name = "Ballon"
    language = "German"
    salary = 1300000
X = Employe()
print(X.name,X.language,X.salary)



# changing name
class Employe:
    language = "German"                                  # class Attribute
    salary = 1300000.
    X = Employe()
    X.name = "Ballon DFJ"                               # instance Attribute
print(X.name,X.salary,X.language)

amir = Employe()
amir.name = "amir Roro"
print(amir.name, amir.language, amir.salary)



# changing language
class Employe:
    language = "German"                                  # class Attribute
    salary = 1300000
    X = Employe()
    X.language = "English"                               # instance Attribute
print(X.salary,X.language)



# getinfo and self method
class Employe:
    language = "German"                                  # class Attribute
    salary = 1300000
    def getinfo(self):
           print(f"The language is {self.language}. The selary is {self.salary}")

X = Employe()                             
X.language = "English"
X.getinfo()                              # or Employe.getinfo



# Constructor
#type-1
class Employe:
    language = "German"                                  # class Attribute
    salary = 1300000
    
    def __init__(self):                                   # __int__ is a dunder mathod which is called by automatically
        print("iam adding new text")
    
    def getinfo(self):
           print(f"The language is {self.language}. The selary is {self.salary}")
          
X = Employe() 
X.getinfo()
                          
#type-2
class Employe:

    def __init__(self,language,salary):                   ## __int__ is a dunder mathod which is called by automatically
        self.language = language
        self.salary = salary                                        
        print("iam adding new text")
    
    def getinfo(self):
           print(f"The language is {self.language}. The selary is {self.salary}")
                                 
X = Employe("Bnagla",120330)
Y = Employe("English",195040)
z = Employe("German",130500)
X.getinfo()

 

# [final form to use]

class Employe:

    def __init__(self,name,salary,language):
        print("Adding the Employe's details...")
        self.name = name
        self.salary = salary
        self.language = language

X = Employe("Fayad",1500000,"Italy")                             
print(X.name,X.salary,X.language)

Y = Employe("Ronaldo",140000,"German")
print(Y.name,Y.salary,Y.language)



# [Abstraction] = hiding the process
class Car:
    def __init__(self):
        self.accelaretion = False
        self.brake = False
        self.clutch = False
    
    def car_start(self):
        self.clutch = True
        self.accelaretion = True
        print("The Car is Started...")
        

    def car_stop(self):
        self.brake = True
        print("The Car is stoped...")
        

car_1 = Car()
car_1.car_start()

car_2 = Car()
car_2.car_stop()


# Private programe
#type-1
class Person:
    def __hello(self):
        print("Helooooo")

x1 = Person()
print(x1.__hello())


#type-2
class  Bank_Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass                # in   [(__)acc_pass]  the   __(duble underscor) use to private the value

ac1= Bank_Account("0001223","12$3^55#lTWf")
print(ac1.acc_no)
print(ac1.__acc_pass)


#Print Privte programe
class Person:
    def __hello(self):
        print("Helooooo")
    
    def welcome(self):
        self. __hello()
    
p1 = Person()
print(p1.welcome())