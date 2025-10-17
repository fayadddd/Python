
# dictonary Bangla to English
words ={
    "shahajjo" : "help",                                    # remamber about  (,)coma using in last
    "bichana"  : "bed",
      "biral"  :  "cat"
}

X1 = input("Enter the word you want to meaning of:")
print(words[X1])                                         # use [] third bracet because of it's a "dict"

# make a user display sets
s = set()

X = input("Enter number: ")
s.add(int(X))
X = input("Enter number: ")
s.add(int(X))
X = input("Enter number: ")
s.add(int(X))
X = input("Enter number: ")
s.add(int(X))
X = input("Enter number: ")
s.add(int(X))
X = input("Enter number: ")
s.add(int(X))
X = input("Enter number: ")
s.add(int(X))
X = input("Enter number: ")
s.add(int(X))
X = input("Enter number: ")
s.add(int(X))
X = input("Enter number: ")
s.add(int(X))

print(s)



# int and str and flot in sets
X2 = set()
X2.add(33)                         # int
X2.add("33")                       # str
X2.add(3.3)
print(X2,type(X2))                  # set {33,"33",3.3}
print(len(X2))                     # leanth 3                                        

# type-2
X3 = set()
X3.add(33)                        
X3.add("33")
X3.add(33.0)
print(X3)                          # {33,"33"} because    33 and 33.0 same thing and value don't repeted
print(len(X3))                     # 2

# QNA
s = {}
s1 = ()
s2 = []
print(type(s))                     # dict
print(type(s1))                    # tuple
print(type(s2))                    # list

# Make a dictonary
X = {}
name = input("Enter your name:")
language = input("Enter your language:")
name2 = input("Enter your name:")
language2 = input("Enter your language:")
X.update({name : language})
X.update({name2 : language2})

print(X)