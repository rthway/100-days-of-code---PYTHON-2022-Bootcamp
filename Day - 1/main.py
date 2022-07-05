#Write your code below this line 👇
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")








'''Output
Q.2 - When you run your program, it should print the following:

Day 1 - String Manipulation
String Concatenation is done with the "+" sign.
e.g. print("Hello " + "world")
New lines can be created with a backslash and n.'''

#Fix the code below 👇

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Q.3 - Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.

#Fix the code below 👇
name = input("What is your name?")
print(len(name))

#another Method
print(len(input("What is your name?")))

''' Q.4 - Write a program that switches the values stored in the variables a and b.

Warning. Do not change the code on lines 1-4 and 12-18. Your program should work for different inputs. e.g. any value of a and b.

Example Input
a: 3
b: 5
Example Output
a: 5
b: 3
'''

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c=a
a=b
b=c 

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

Q.5
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

#Fix the code below 👇
two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number [0] ) + int(two_digit_number [1]))

