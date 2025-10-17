


# user inter the name and i need to add GOOD MORNING using input() function
name = input("Enter your name\n")              # fayad
print("GOOD MORNING," + name)                  # GOOD MORNING,fayad   ''' 


# write a program to fill in a (letter template) given below with name and date
letter = ''' Dear |NAME|,
Gresting from XYZ cording house. Iam happy to tell you about your sellection.
You are selected!
Have a Great Day Ahead.
Thanks and regards,
Date: |DATE|'''
name = input("Enter your Name:\n")
date = input("Enter date:\n")
letter = letter.replace("|NAME|", name)
letter = letter.replace("|DATE|", date)
print(letter)


# Double space detacted
a = "this is a string with double  spaces"
doubleSpaces = a.find("  ")
print(doubleSpaces)                           # 28  position


# Double spaces replace into single spaces
a = "this is a string with double  spaces"
a = a.replace("  ", ' ')                      # convert double spaces into single spaces
print(a) 
# moultiple double spaces
b = "this is a string with double  spaces  ok"
b = b.replace("  ", ''' ''')
print(b)


# Reformate the letter
letter = "Dear fayad, You will millioner too soon! Yes you are!"
reformate_the_letter = "Dear fayad,\n\t You will millioner too soon!\nYes you are!"
print(reformate_the_letter)