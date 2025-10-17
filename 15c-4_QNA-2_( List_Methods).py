#1 List sort ( sort = serial by serial)
X = [1,3,5,2,4,]
X.sort()
print(X)                                   # [1,2,3,4,5]


#2 List reverse 
X = [1,3,5,2,4,]
X.reverse()
print(X)                                   # [4,2,5,3,1]
   

#3 List append ( append = add more)
X = [1,3,5,2,4,]
X.append(66)
print(X)                                    # [1,3,5,2,4,66]


#4 List insert ( insert = shift in any position)
X = [1,3,5,2,4,]
X.insert(0,99)
X.insert(3,100)
X.insert(1,33)
print(X)                                   # [99, 33, 3, 100, 2, 4]


#5 List pop ( pop = delete)
X = [1,3,5,2,4,]
X.pop(0)
print(X)                                    # [3,5,2,4]  

X.pop(1)
print(X)                                    # [1,5,2,4]

X.pop(2)
print(X)                                    # [1,3,2,4]


#6 list remove
X = [1,3,5,2,4,]
X.remove(4)
print(X)                                    # [1,3,5,2]

X.remove(5)
print(X)                                    # [1,3,2,4] 

X.remove(1)
print(X)                                    # [3,5,2,4]                 