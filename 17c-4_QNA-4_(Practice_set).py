
# name of fruits
fruits = []
 
f1 = input ("Enter fruits name:")
fruits.append(f1)
f2 = input ("Enter fruits name:")
fruits.append(f2)
f3 = input ("Enter fruits name:")
fruits.append(f3)
f4 = input ("Enter fruits name:")
fruits.append(f4)
f5 = input ("Enter fruits name:")
fruits.append(f5) 
print(fruits)

# examination mark
marks = []
 
f1 = input ("Enter marks name:")          # shortcut :      f1 = int(input ("Enter marks name:"))   
f1 = int(f1)
marks.append(f1)
f2 = input ("Enter marks name:")
f2 = int(f2)
marks.append(f2)
f3 = input ("Enter marks name:")
f3 = int(f3)
marks.append(f3)
f4 = input ("Enter marks name:")
f4 = int(f4)
marks.append(f4)
f5 = input ("Enter marks name:")
f5 = int(f5)
marks.append(f5) 
print(marks)



# Palindrome

list1 = [1, 2, 1]
list2 = [1, 2, 3]
list3 = ["m","a","m"]
list4 = ["m","a","l"]
 
copy_list1 = list1.copy()
copy_list1.reverse()

copy_list2 = list2.copy()
copy_list2.reverse()

copy_list3 = list3.copy()
copy_list3.reverse()

copy_list4 = list4.copy()
copy_list4.reverse()

if(copy_list1 == list1):
    print("Palindorme")
else:
    print("NOT Palindrome")

if(copy_list2 == list2):
    print("Palindorme")
else:
    print("NOT Palindrome")

if(copy_list3 == list3):
    print("Palindorme")
else:
    print("NOT Palindrome")

if(copy_list4 == list4):
    print("Palindorme")
else:
    print("NOT Palindrome")