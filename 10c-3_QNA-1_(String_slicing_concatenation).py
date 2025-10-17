



# Concatenation two strings
name = "azmain taosif fayad,"
wish = "good morning"
print(name + wish)

  # OR
X = name + wish
print(X)



# Strings Slicing
name = "fayad"                 # f=0 , a=1 , y=2 , a=3 , d=4 (every first letter start with [0 to 1000....])
print(name[0])                 # f
print(name[1])                 # a
print(name[2])                 # y 
print(name[3])                 # a
print(name[4])                 # d
                
  # others
fullname ="azmain taosif fayad"  # a=0,z=1,m=2,a=3,i=4,n=5,gap=6,t=7,a=8,o=9,s=10,i=11,f=12,gap=13,f=14,a=15,y=16,a=17,d=18 
print(fullname[0:19])           # azmain taosif fayad


  # 0:5 means 0 to 4 {last number doesn't count like (5)}
print(name[0:5])               # fayad         
print(name[0:4])               # faya
print(name[0:3])               # fay
print(name[0:2])               # fa
print(name[0:1])               # f
print(name[0:0])               # not valued
print(name[:5])                # is same as name[0:5]
print(name[0:])                # is same as name[0:5]           
  

# Stirngs Length
name = "fayad"                 # every last letter is count by [-1] ( d=-1 , a=-2 , y=-3 , a=-4 , f=-5 )
print(name[-1])                # d
print(name[-2])                # a
print(name[-3])                # y
print(name[-4])                # a
print(name[-5])                # f


