
# Read the File
X = open("c-9 demo file.txt","r")
Y = X.read()
print(Y)
print(type(Y))
X.close()

# or       # without use cloose funtion
with open("c-9 demo file.txt","r") as X:
     data = X.read()
     print(data)


# Write the file
with open("c-9 demo file", "w") as X1:
    X1.write("Hehe surprice\nI creat a new line")

#read
X2 = open("c-9 demo file.txt","r")
Y2 = X2.readlines()
print(Y2,(type(Y2)))
X2.close()

# Read line
f = open("c-9 demo file.txt","r")

line1 = f.readline()
print(line1,(type(line1)))

line2 = f.readline()
print(line2,(type(line2)))

line3 = f.readline()
print(line3,(type(line3)))

line4 = f.readline()
print(line4 =="")


f.close()

# a = append means (file.txt ar last a add hobe)
X3 = "\niam adding a new line"
Y3 = open("c-9 My file.txt","a")
Y3.write(X3)
Y3.close()

# rb = Binary mode
X = open("c-9 demo file.txt","rb")
Y = X.read()
print(Y)
print(type(Y))
X.close()



