# repeted for multiple time uses
# [Function] [Definition]

def calculate_pluse(a,b):
    pluse = a + b
    return pluse
print(calculate_pluse(2,4))
print(calculate_pluse(45,4))
print(calculate_pluse(9,5))
print(calculate_pluse(22,34))


def calculate_avarage():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    average = (a + b + c)/3
    return average
print(calculate_avarage())
print("Thank you!")


# [Funtion] [argumnet]
# type-1
def X(name,ending):
    print(" good morning," + name)
    return ending   
a = X("Fayad","Thank you")
print(a)

# type-2
def X(name,ending="Thank you"):
    print(f"good morning, {name}")
    print(ending)
    
X("Fayad")


# [Recursion]
#type-1
def  show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(6)

'''
| factorial(n) = n-1 x ..... 3 x 2 x 1       |  
| factorial(5) = 5 x 4 x 3 x 2 x 1           |
| factorial(4) = 4 x 3 x 2 x 1               |
| factorial(3) = 3 x 2 x 1                   |
| factorial(2) = 2 x 1                       |
| factorial(1) =  1                          |
|                                            |
| factorial(n) = n * factorial(n-1)          |'''


#type-2
n = int(input("Enter your number: "))
def factorial(n):
    if( n==1 or n==0):
        return 1
    return n * factorial(n-1)

print(f"The factorial of ths number is:{factorial(n)}")

#Loops
#type-3
def cal_fact(n):
    fact = 1
    for X in range(1,n+1):
        fact *= X
    print(fact)
cal_fact(5)