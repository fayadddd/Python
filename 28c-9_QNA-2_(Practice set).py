
# the word is present or not in your file
X = open("c-9 parctice set.txt")
Y = X.read()
if("Cristiano" in Y ):
    print("the word Cristinao is present in the here")

else:
    print("the word Cristinao is not present in the here")


if("Neymar" in Y ):
    print("the word Neymar is present in the here")

else:
    print("the word Neymar is not present in the here")

X.close()


# which line the word is preasent in your file
word = "positions"
data = True
line_no = 1
with open("c-9 log.txt", "r") as f:
     while data:
        data = f.readline()
        if(word in data):
            print(line_no)
        line_no +=1


# finding the odd number in your file
count = 0
with open("c-9 My file.txt", "r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)


# Game high score
import random

def game():
    print("You are playing the game...")
    X = random.randint(1,100)                       # randint means continution 1 to 100 or 1,2,3......100
    with open("c-9 game.txt") as Z:
        Y = Z.read()
        if(Y !=""):
            Y = int(Y)
        else:
            Y = 0
    
    print(f"Your Score: {X}")
    with open("c-9 game.txt", "w") as Z:
            Z.write(str(X))
    if(X>Y):
            return X
        
game()


# monkey to ######
word = "Monkeys"
with open("c-9 Monkey.txt","r") as f:
    X = f.read()
Y = X.replace(word,"#######")
with open("c-9 Monkey.txt","w") as f:
    f.write(Y)

# word = is more then 1 word, then use Y = X.replace(word,"#" * len(word))


# line
with open("log.txt") as f:
    lines = f.readlines()

X = 1
for line in lines:
    if("python" in line):
        print(f"yes python is present.Line no:{X}")
        break
    X += 1

else:
    print("No Python is not present")