import random
'''  1 = snake
    -1 = water
     0 = gun   '''
computer = random.choice([-1, 0, 1])
yourinput = input("Enter your choise (s/w/g) : ")
X = {"s" : 1, "w" : -1, "g" : 0 }
reverse_X = { 1:"Snake", -1:"Water", 0:"Gun"}

you = X[yourinput]

print(f"You chose {reverse_X[you]}\nComputer chose {reverse_X[computer]}")

if(computer == you):
    print("It's a Draw")

else:
    if(computer ==-1 and you ==1):
        print("You WIN")
        
    elif(computer ==-1 and you ==0):
        print("You LOSE")
        
    elif(computer ==1 and you ==-1):
        print("You LOSE")
        
    elif(computer ==1 and you ==0):
        print("You WIN")
        
    elif(computer ==0 and you ==1):
        print("You LOSE")
        
    elif(computer ==0 and you ==-1):
        print("You WIN")


    

   