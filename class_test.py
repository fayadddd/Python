
# c-2_QNA-3_(Typecasting)

''' #-1 What is the data type of the value returned by the input() function before any conversion? '''
    # ans-1: "string" 

''' #-2 Why does converting the input for a (name) to int or float result in an error? '''
    # ans-2: because the name is text. and it not be able to being int or float 

''' #-3 How does the data type of variable b change after converting it first to int and then to float? '''
    # ans-3: 
'''b= input("enter your input:")
print(type(b))
b = int(b)
print(type(b))
b = float(b)
print(type(b))'''




# c-3_QNA-1_(String_slicing_concatenation)

''' #-1 What will be the output of print(name + wish) when name = "azmain taosif fayad," and wish = "good morning"? '''

    # ans-1:
name = "azmain taosif fayad"
wish = "good morning"
print(name + wish)


''' #-2 How do you access the third character of the string name = "fayad" using indexing? '''

    # ans-2: 
name = "fayad"    
print(name[2])


''' #-3 What is the result of print(fullname[0:19]) if fullname = "azmain taosif fayad"? '''
    # ans-3: azmain taosif fayad


''' #-4 Explain the difference between name[0:5] and name[0:4] when name = "fayad" '''

    # ans-4:
name = "fayad"
print(name[0:5])   # it will show fayad  (because last word is not count like 5,it will be 5-1=4)
print(name[0:4])   # it will show faya   (because last word is not count like 4,it will be 4-1=3)


''' #-5 How can you use negative indexing to print the last character of the string name = "fayad"? '''

    # ans-5:
name = "fayad"
print(name[-1])




# c-3_QNA-2_(String_function)

''' #-1 What is the output of the str.upper() and str.lower() methods in your code when applied to the string 'PyThOn'? 
Show the specific lines of code that produce this result.'''  

    # ans-1:
story = "once upon a time there was a millioner name fayad who get 1 million in every month"
print(story.upper())      # ONCE UPON A TIME THERE WAS A MILLIONER NAME FAYAD WHO GET 1 MIILION IN EVERY MONTH
print(story.lower())      # once upon a time there was a millioner name fayad who get 1 miilion in every month
 

''' #-2 In your program, how did you use the str.find() or str.index() method to locate a substring? 
What is the key difference between these two methods that your code demonstrates (in their behavior when the substring is not found)? '''

    # ans-2:
story = "once upon a time there was a millioner name fayad who get 1 million in every month"
print(story.find("fayad"))  
print(story.find("azmain"))          # not find = -1
print(story.index("fayad"))
'''print(story.index("azmain"))         # not find = valueError'''

# The key difference is in their behavior when the substring is not found:

    #-1 str.find(): If the search fails, it returns the integer -1. This is a safe and silent failure.
     # The program can check for -1 to handle the "not found" case without crashing.

    #-2 str.index(): If the search fails, it raises a ValueError exception.
     # This will crash the program unless the call is placed inside a try...except block to handle the error gracefully,
     # as demonstrated in the code.


''' #-3 What is the purpose of the str.strip(), str.lstrip(), and str.rstrip() methods, 
and how do they handle different types of whitespace characters? '''

    # ans-3:
x = "  \t\n\n  Hello, World!  \n\t  "
print(f"Original: '{x}'")

# 1. str.strip() - Removes from both ends
y = x.strip()
print(f"After strip(): '{y}'")

# 2. str.lstrip() - Removes from the left (beginning) only
j = x.lstrip()
print(f"After lstrip(): '{j}'")

# 3. str.rstrip() - Removes from the right (end) only
k = x.rstrip()
print(f"After rstrip(): '{k}'")

#output:
''' Original: '  		Hello, World!  	  '
    After strip(): 'Hello, World!'
    After lstrip(): 'Hello, World!  	  '
    After rstrip(): '  		Hello, World!'
'''
#str.strip(): Removes characters from both the beginning and the end of the string.
#str.lstrip(): Removes characters only from the beginning (left side) of the string.
#str.rstrip(): Removes characters only from the end (right side) of the string.


''' #-4 How does your program use the len() function? What string did you apply it to, 
and what was the returned value? Does len() count spaces and punctuation? '''

    # ans-4:
story = "once upon a time there was a millioner name fayad who get 1 million in every month"
lenth = len(story)
print(lenth)

#Purpose	            -----   To determine the number of items in a sequence (e.g., characters in a string).
#Application	        -----   Used on your input, my internal data, and my generated output.
#Example	           	-----   	len(story) returns 81
#Spaces/Punctuation		-----   	Yes. It counts every single character, including spaces, commas, periods, and symbols.




# c-4_QNA-1,2_(List,List_Methods)

''' #-1 Write the Python code to create a list named fruits containing the elements "apple", "banana", and "cherry". 
Then, print the second item in the list. '''

    # ans-1:
fruits = ["apple","banana","cherry"]
print(fruits[1])

''' #-2 Given an empty list my_list = []
write the code to use these methods to make the list become ['python', 'is', 'fun', 'language']'''

    # ans-2:
'''my_list = []
list_1 = input("enter your frist input:")
list_2 = input("enter your second input:")
list_3 = input("enter your third input:")
list_4 = input("enter your fourth input:")
append_list = my_list.append(print([list_1,list_2,list_3,list_4]))
print(type(append_list)) '''

''' #-3 Explain the difference between the .pop(), .remove(), and del keyword when used on a list.
Provide a short code example for each that shows how it removes an element from the list numbers = [10, 20, 30, 40, 50]. '''

    # ans-3:
#    [pop]
numbers = [10, 20, 30, 40, 50]
numbers.pop(2)
print(numbers)

#    [remove]
numbers = [10, 20, 30, 40, 50]
numbers.remove(10)
print(numbers)
numbers.remove(20)
print(numbers)
numbers.remove(30)
print(numbers)
numbers.remove(40)
print(numbers)

#    [del]
numbers = [10,20,30,40,50]
del numbers[1]
print(numbers)
del numbers[0:3]
print(numbers)


#  Feature	                     .pop(index)	                 .remove(value)                              del 

# Argument	                  Index (optional)	                     Value	                             Index or Slice
# Returns Value?                	Yes                                No	                                   No
# Modifies List?	                Yes	                               Yes                                     Yes
# Use Case	            Remove by index & use the value	      Removeby known value	                Remove by index/slice, no need for value


''' #-4  Assuming your first program covers list operations, 
write a line of code that uses slicing on the list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] to create 
a new list containing only the elements [3, 4, 5, 6]. '''

    # ans-4:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = numbers[3:7]
print(new_list)
#  or
numbers_1 = [0,1,2,3,4,5,6,7,8,9]
del numbers_1[0:3]
print(numbers_1)
numbers_1.reverse()
print(numbers_1)
del numbers_1[0:3]
print(numbers_1)
numbers_1.reverse()
print(numbers_1)

''' #-5 Write a program that does the following:
Creates a list with the values [1, 2, 3].
Uses a method to add the value 4 to the end of the list.
Uses a method to add the value 0 to the beginning of the list.
Prints the final list and its length. '''

    # ans-5:
values = [1, 2, 3]
values.append(4)
print(values)
values.insert(0,0)
print(values)
print(len(values))