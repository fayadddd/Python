# Greatest number

def X(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c

a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))
print(X(a,b,c))



# calcius to farhenhit
f = int(input("Enter temperature in F: "))
c = 5*(f-32)/9
print(f"{round (c), 2}°F")

# type - 2
def X(f):
    return 5*(f-32)/9
f = int(input("Enter temperature in F: ") )
print(f"{round (X(f), 2)}°F")


# gap
print("a")
print("b")
print("c", end="")
print("d", end="")                    #  a , b , cd


# recurtion
'''
Y(5) = 1 + 2 + 3 + 4 + 5
Y(4) = 1 + 2 + 3 + 4 
Y(3) = 1 + 2 + 3 
Y(2) = 1 + 2
Y(1) = 1

Y(n) = 1 + 2 + 3 + 4 +.....n+1
Y(n) = Y(n-1) + n '''


def X(n):
    if(n==1 or n==0):
        return 1
    return X(n-1) + n
print(X(4))


# Star pettern
def pettern(n):
    if(n==0):
        return # or print("nothing")
    print("*" * n )
    pettern(n-1)

pettern(5)   


# inch to cm
def inch_to_cm(inch):
    return inch * 2.54
X = int(input("Enter value in inches: "))
print(f"The value in cm is {inch_to_cm(X)}cm")


# multification
def multiply(n):
    for i in range(1,11):
        print(f"{n} x {i} {n*i}")

multiply(5)


# USD to Tk
def convertion(USD_value):
    TK_value = USD_value * 106
    print(USD_value, "USD =", TK_value, "TK")
convertion(100)