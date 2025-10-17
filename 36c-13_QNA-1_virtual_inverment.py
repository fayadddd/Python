# to see the download packegas
'''  pip freeze  '''

# to transfer packegas into txt file
'''     pip freeze > requirements.txt    '''

# install those packegas in any inverment
'''     pip install -r .\requirements.txt     '''





# Lambda function
square = lambda X : X*X
print(square(6))

sum = lambda a,b,c : a+b-c
print(sum(2,6,8))



# Join mathod
a = ["fayad", "azzmain", "taosif"]
X = " 0-_-0 " .join(a)
print(X)



# Formet method
a = "{1} is a good boy {0}" .format("Azmain", "Fayad")                    # azmain = 0      fayad = 1
print(a)



# Map function
l = [1,2,3,4,5,]
square = lambda x : x*x
Y = map(square, l)
print(list(Y))



# Filter function
lis = [1,2,3,4,5,]
def X(n):
    if (n%2 == 0):
        return True
    return False

Y = filter(X, lis)                                    # filter ---- find  only numbers those are devided by 2 
print(list(Y))



# Reduse
from functools import reduce
lis = [1,2,3,4,5,]
def sum(a,b):
    return a+b

print(reduce(sum, lis))
