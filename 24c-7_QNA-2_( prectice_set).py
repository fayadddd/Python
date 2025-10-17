# make a multiplication table with [for] Loops
X = int(input("Enter a number: "))

for Y in range(1,11):
    print(f"{X} x {Y} = {X*Y}")                        # or print(f"{X} * {Y} = {X*Y}")      


# make a multiplication table with [while] Loops
X1 = int(input("Enter a number: "))
Y1 = 1

while(Y<11):
    print(f"{X1} x {Y} = {X1*Y}")
    Y1 += 1




# about name
X2 = ["Fayad","Azmain","Asif","sakib"]

for name in X2:
    if(name.startswith("A")):
        print(f"HELLO {name}")                       # HELLO Azmain , HELLO Asif



# prime number and not prime number     # prime number = jor shonkha      # not prime number = bijor shonkha
X3 = int(input("Enter your number: "))

for Y2 in range(2,X3):
    if(X3 % Y2) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")



# [factorial (!)]  is  Y! = 1 x 2 x 3 x 4 x 5 x ....... Y

X4 = int(input("Enter the number: "))
product = 1
for Y in range(1, X4+1):
    product = product * Y
print(f" The factorial of {X4} is {product}")



# making the start with [for] Loops
# type-1
n = int(input("Enter The number: "))
for Y in range(1, n+1):
    print(" "* (n-Y), end ="")
    print("*"* (2*Y-1), end ="")
    print("")
    
# type-2
n = int(input("Enter The number: "))
for Y in range(1, n+1):
    print("*" * Y, end ="")
    print("")

# type-3
n = int(input("Enter The number: "))
for Y in range(1, n+1):
    if( Y == 1 or Y == n):
        print("*" * n, end ="")
    else:
         print("*", end ="")
         print(" " * (n-2), end ="")
         print("*", end ="")
    print("")



# revers multification
Z = int(input("Enter The number: "))
for Y in range(1, 11):
    print(f"{Z} x {11 - Y} = {Z*(11-Y)}")