# problem-1

try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)


print("Thank You!")




# proble-2

l = [1, 2, 3, 4, 5, 6 ,7 , 8]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)




# problem-3

n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
print(table)




# problem-4

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")




# problem-5

n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
with open("tables.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")

