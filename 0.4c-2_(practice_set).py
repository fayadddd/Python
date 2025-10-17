

# write a python prgrm to add 2 numbers
a = 10
b = 5
print("the sum of a and b is", a*b)       # 50



# write a python prgrm to find (remainders) when a number is divided by Z
a = 45
b = 5
print("the remainder when a is divided by b is", a%b)      # (0) because 45/5 = 9 
# and
A = 46
B = 5
print("the remainders when A is divided by B is", A%B)     # (1) because 46/5 = float



# compare bettwen a and b
a = 334
b = 222
print(a>b)    # ture
print(b>a)    # false



# (a+b)/2
a = input("enter first number:")
b = input("enter second numbber:")
X = (a+b)/2
print("the average of a and b is", X)    # not valued because "str" can't be an number so convert (str) into (int)
# solution
a = input("enter first number:")        # 34
b = input("enter second number:")       # 23
b = int(b)
a = int(a)
X = int(a+b)/2
print("the average of a and b is", X)    # 28.5 and also a float number
print(type(X))                              
                                
                        

