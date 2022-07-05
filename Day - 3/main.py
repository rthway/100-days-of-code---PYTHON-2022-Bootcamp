# Q.1 WAP to ride rollercoster if your height more then 120 cm 
print ("Welcome to the Rollercoster!")
height = int(input("your height on cm : "))
if height > 120:
  print("you can ride Rollercoster!")
else:
  print("You can not ride Rollercoster!")



# Q.2 WAP to check input number is odd and even.
number = int(input("Enter your number: "))
if number%2==0:
  print("The number is even")
else:
  print("The number is odd")




# Q.3 WAP to Ride rollercoster if your height > 120. and charge is more then 18 years $12 or <=18 then $7
# This is a example of Nasted if/else 
print ("Welcome to the Rollercoster!")
height = int(input("Enter your height on cm : "))
if height > 120:
  print("you can ride Rollercoster!")
  age=int(input("Enter your age: "))
  if age > 18:
    print("your charge is $12")
  else:
    print("your charge is $7")
else:
  print("You can not ride Rollercoster!")

# Q.4 WAP to Ride rollercoster if your height > 120. and charge is more then 18 years $12 or <=18 then $7
# This is a example of Nasted if/else with elif
print ("Welcome to the Rollercoster!")
height = int(input("Enter your height on cm : "))
if height > 120:
  print("you can ride Rollercoster!")
  age=int(input("Enter your age: "))
  if age < 12:
    print("your charge is $5")
  elif age <= 18:
    print("your charge is $7")
  else:
    print("your charge is $12")
else:
  print("You can not ride Rollercoster!")

# Q.5 WAP to calculate and corresponding interpretation.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi=round(weight/height**2)
if bmi<18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
  

# Q.6 WAP to Ride rollercoster if your height > 120. and charge is more then 18 years $12 or <=18 then $7 and add additial $3 if they want to click photos.
# This is a example of Nasted if/else with elif
print ("Welcome to the Rollercoster!")
height = int(input("Enter your height on cm : "))
if height > 120:
  print("you can ride Rollercoster!")
  age=int(input("Enter your age: "))
  if age < 12:
    bill=5
    print("your charge is $5")
  elif age <= 18:
    bill=7
    print("your charge is $7")
  else:
    bill=12
    print("your charge is $12")
  wants_photo=input("Do you want to photo Taken? Y or N. ")
  if wants_photo=="Y":
    bill+=3
  print(f"Your final bill ammount = {bill}")
    
else:
  print("You can not ride Rollercoster!")

'''
Q.7 Instructions
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

This is how you work out whether if a particular year is a leap year.
on every year that is evenly divisible by 4 
**except** every year that is evenly divisible by 100 
**unless** the year is also evenly divisible by 400
e.g. The year 2000:
2000 ÷ 4 = 500 (Leap)
2000 ÷ 100 = 20 (Not Leap)
2000 ÷ 400 = 5 (Leap!)
So the year 2000 is a leap year.
But the year 2100 is not a leap year because:
2100 ÷ 4 = 525 (Leap)
2100 ÷ 100 = 21 (Not Leap)
2100 ÷ 400 = 5.25 (Not Leap)
''' 


# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 ==0:
    if year % 100==0:
        if year % 400==0:
            print("leap year")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")




'''
Q.8 Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1 
'''
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill+=25

if add_pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_cheese=="Y":
    bill+=1
print(f"Your final bill is ${bill}")



'''
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."

e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times

Total = 3
Love Score = 53
Print: "Your score is 53."
'''
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string = name1 + name2 
lower_case_string=combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love= l + o + v + e

score = str(true) + str(love)
love_score=int(score)
if (love_score <10) or (love_score >90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")













