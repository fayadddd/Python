


Y = int(input("Enter your age:\n"))

if(Y>=18):
    print("[congratulation you are in a unresticted age]")

else:
    print("[Ops you are in a recticted age]")

# elif
X = int(input("Enter your age:\n"))

if(X>=18):
    print("[congratulation you are in a unresticted age]")

elif(X<0):
    print("{Why you are Entering unvalid age?}")

elif(X==0):                                                       # single (=) is not valid use duble (=)(=)
    print("{Why you are Entering unvalid age?}")

else:
    print("[Ops you are in a recticted age]") 

# 2/and more if thakle
X2 = int(input("Enter your age:\n"))

# if statement-1
if(X2/2==0):    
    print("X2 is even")  # close here

else:
    print("X2 is odd")


# if statement-2
if(X2>=18):
    print("[congratulation you are in a unresticted age]")

elif(X2<0):
    print("{Why you are Entering unvalid age?}")

elif(X2==0):                                                       
    print("{Why you are Entering unvalid age?}")

else:
    print("[Ops you are in a recticted age]")   # close here




# single line if operator

              # varible = (value-1) if {condition} else (value-2)      [1]

food = input("food: ")
eat = "yes" if food == "cake" else "no"
print (eat)

              # (value-1) if {condition} else (value-2)                [2]

food = input("food: ")
print ("sweet") if food == "cake" or food == "jalebi" else print("not sweet")


              # varible = (false , true) [condition]                   [3]  clever if

age = int(input("age: "))
vote = ("no", "yes")[age >= 18]
print(vote)


salary = float(input("selary: "))
tax = salary*(0.1 , 0.2) [salary <= 50000]
print(tax)


salary = float(input("selary: "))
tax = ((12/100)*salary , (6/100)*salary) [salary <= 50000]
print(tax)