# [While] Loops
X = 1

while(X<6):                          # [while] means until give me the numbers when X<6 is false
    print(X)
    X += 1                           # X = (X<6) = [1,2,3,4,5]               # X+=1 / X=X+1


# [list] using [while]
X1 = [1,"fayad",False,34]
Y = 0

while(Y<len(X1)):                    # len = leanth of X1 is (1,2,3,4)   # X1=4 # Y=0 # Y<4 = 1,2,3
    print(X1[Y])   
    Y += 1                           # 1,fayad,False,34


# [for] Loops
for X2 in range(10):                 # range = 0 to 9   
    print(X2)

#type-2
for X3 in range(0,20,2):             # (start=0,stop=20,step/gap=2)
    print(X3)


# [for] [list] and [tuple] and [string]
Li = [1,24,3,56,778,8]
for Xi in Li:
    print(Li)                        # 1,24,3,56,778,8

Tu = (3,66,3345,22,7,99)
for Xj in Tu:
    print(Xj)                        # 3,66,3345,22,7,99

St = "fayad"
for Xp in St:
    print(Xp)                        # f  a  y  a  d


# [for] Loops with [else]
X4 = [1,45,26,77]
for item in X4:
    print(item)
else:                                
    print("done")                   # when the loops end it show     # 1,45,26,77,done


# Loops [break]
for X5 in range(30):
    if( X5 == 20):
        break                       # break = exit the loop
    print(X5)                       # 0.....20        


# Loops [continue]
for X6 in range(30):
    if( X6 == 20):
        continue                    # 
    print(X6)                       # 0.....18,19,21,22......30


    
# Loops [pass]
for X6 in range(30):
    pass                            # Loops pouse/stop