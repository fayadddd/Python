
X = {
       "fayad" : 100,
       "azmain" : 88,
       "taosif" : 77, 
       
        100 : "fayad",
        88 : "azmain",
        77 : "taosif",  }

print(X,type(X))
print(X["fayad"])
print(X["azmain"])
print(X["taosif"])
print(X[100])
print(X[88])
print(X[77])


X2 = {
        "name" : "Fayad",
        "subject": {
                "physics": 98,
                "Chmeistry":97,
                "ICT":100
        }
}

# Nested dictionary
print(X2["subject"]["ICT"])



# dict Method

X1 =   {
       "fayad" : 100,
       "azmain" : 88,
       "taosif" : 77, 
       
        100 : "fayad",
        88 : "azmain",
        77 : "taosif",  }
1.
print(X1.items())                   # X1 a ja ja ase shob show korbe 

2.
print(X1.keys())                    # X1 a left side all things

3.
print(X1.values())                  # X1 a right side all things

4.
X1.update({})                       # exchance and ADD
X1.update({"fayad":99,})            # fayad : 99
X1.update({"spider Man":00})        # new adding
print(X1)

#OR
X1.update({"fayad":99,"spider Man":00})
print(X1)

5.
print(X1.get("fayad"))              # 100
print(X1.get("DJ BOY"))             # None