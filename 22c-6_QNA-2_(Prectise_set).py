
# QNA-1 find the greatest number
a1 = int(input("Enter your number1: "))            #3
a2 = int(input("Enter your number2: "))            #2
a3 = int(input("Enter your number3: "))            #4
a4 = int(input("Enter your number4: "))            #1

if ( a1>a2 and a1>a3 and a1>a4 ):                  # t f t
    print("The greatest number is a1: ",a1)
elif ( a2>a1 and a2>a3 and a2>a4 ):                # f f t
    print("The greatest number is a2: ",a2)
elif ( a3>a2 and a3>a1 and a1>a4 ):                # t t t   
    print("The greatest number is a3: ",a3)
elif ( a4>a2 and a4>a3 and a4>a1 ):                # f f f
    print("The greatest number is a4: ",a4)




# QNA-2 student pass and fail mark's percentage
mark1 = int(input("Enter Marks1: "))
mark2 = int(input("Enter Marks2: "))
mark3 = int(input("Enter Marks3: "))

total_percentage = (100*(mark1 + mark2 + mark3)/300)
if(total_percentage>30 and mark1>33 and mark2>33 and mark3>33):
    print("congratulation you are pass ",total_percentage)
else:
    print("unfortunatly you are fail",total_percentage)




# spam filter
p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe now"
p4 = "click now"

massage = input("Enter your comment:")
if((p1 in massage) or (p2 in massage) or (p3 in massage) or(p4 in massage)):
    print("!!!{This comment is a sapm}!!!")
else:
    print("{ This comment is not a spam }")




# QNA-3 name list
X = ["fayad","azmain","taosif"]
name = input("Enter your name: ")
if(name in X):
    print("Your is in the list")
else:
    print("you name is not in the list")




# QNA-4 Mark Grade
marks = int(input("Enter your marks: "))
if(marks<=100 and marks>=90):
    grade = "GoldanA+"
elif(marks<90 and marks>=80):
    grade = "A+"
elif(marks<80 and marks>=70):
    grade = "A"
elif(marks<70 and marks>=60):
    grade = "A-"
elif(marks<60 and marks>=50):
    grade = "B"
elif(marks<50):
    grade = "F"

print("your grade is:", grade)