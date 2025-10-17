import random
n = random.randint(1,100)
a = -1
attempts = 1
while(a != n):
    a = int(input("Guess The Number: "))
    if(a > n):
        print("Lower number plz,")
        attempts += 1
    elif(a < n):
        print("Higher number plz,")
        attempts += 1

print(f"You have guessed the currect number {[n]} in {attempts} attemps")