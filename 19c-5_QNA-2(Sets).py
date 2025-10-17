# in  Sets  (value don't repeted)

s = {1, 5, 32, 54, 5, 5, 5, "fayad"}
print(s,type(s))

# Sets Methods

s1 = {1, 5, 32, 54, 5, 5, 5,}

# adding value
s1.add("hallo")
print(s1)

# Remove value
s1.remove(5)
print(s1)

# full clear the set
s1.clear()
print(s1)

# union all value
s2 = {1,45,6}
s3 = {7,8,1,78}
print(s2.union(s3))                # {1,6,7,8,45,78}
print(s3.union(s2))                # same

# intersection only common value
print(s2.intersection(s3))         # 1
print(s3.intersection(s2))         # 1