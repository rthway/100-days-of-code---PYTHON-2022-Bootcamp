# Q.1 - Input two digit number and output sum of the digits

two_digit_number=input("Enter your 2 digit number: ")

first_digit= two_digit_number[0]
second_digit=two_digit_number[1]
result=int(first_digit) + int(second_digit)
print(result)

# Q.2 - BMI Calc (BMI=Weight/(height*height))
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
result=float(weight)/(float(height)*float(height))
print(int(result))

# or 
BMI=float(weight)/float(height)**2
BMI_as_int=(int(BMI))
print(BMI_as_int)

'''
Q.3 - Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input
56
Example Output
You have 12410 days, 1768 weeks, and 408 months left.
'''

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int=int(age)
age_remaining = 90-age_int
days_remaining = age_remaining*365
weeks_remaining = age_remaining*52
months_remaining = age_remaining*12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")

Project 2 - Tip Calulator
print("Welcome to the tip calculator!")
bill =float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give ? 10,12, or 15?"))
people = int(input("How many people to split the bill?"))
bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)
