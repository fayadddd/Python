

# we can create a list with items of diffrent types
X = [ 67, "fayad",True, 8.9 ]
print(X[1])                      # fayad
print(X[0])                      # 67
print[1] = "FFAAYYAADD"
print(x[1])                      # FFAAYYAADD
print(x)                         # 67, "fayad", True, 8.9



# create a List using []
a = [ 1, 2, 9, 13, 15 ]
print(a)                          # [ 1, 2, 9, 13, 15, ]
print(a[0])                       # 1
print(a[1])                       # 2
print(a[2])                       # 9
print(a[3])                       # 13
print(a[4])                       # 15

print(a[-1])                      # 15
print(a[-2])                      # 13
print(a[-3])                      # 9
print(a[-4])                      # 2
print(a[-5])                      # 1


# changing list
a = [ 1, 2, 9, 13, 15, ]
a[0] = 88
a[1] = 99
a[2] = 66
a[3] = 77
a[4] = 55
a[5] = 44
a[6] = 00
print(a)                         # [88, 99, 66, 77, 55, 44, 00]


# List slicing
friends = ["fayad", "shadow", "halk", "aquaman"]
print(friends[0:3])                                             # ["fayad", "shadow", "halk"]