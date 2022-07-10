'''
dictionaries : 
key         Value
bug         An error in a progrram that prevents  the program from running expected.
function    A piece of code that you can easily call over and over Again
loop        The action of doinf something over and over again.
'''

# simple syntax
programming_dictionary={
    "bug":"An error in a progrram that prevents  the program from running expected.",
"function":"A piece of code that you can easily call over and over Again"
}


#Retrieving item from dictionary 
print(programming_dictionary[function])
print(programming_dictionary[bug])


# add new item on dictonary
programming_dictionary["loop"]="The action of doing something over and over again."


# create an empty dictionary
empty_dictionary={}

# wipe exiting dictionaty
programming_dictionary={}

# Edit an item in a dictionary
programming_dictionary[bug]="A moth in your computer"

# loop through a dictionary
programming_dictionary={
    "bug":"An error in a progrram that prevents  the program from running expected.",
  "function":"A piece of code that you can easily call over and over Again"
}

for thing in programming_dictionary:
  print(thing)

'''
Result: 
bug
function 
loop
note : this function can print out key only
'''
programming_dictionary={
    "bug":"An error in a progrram that prevents  the program from running expected.",
  "function":"A piece of code that you can easily call over and over Again"
}

for thing in programming_dictionary:
  print(thing)
  print(programming_dictionary[thing])

'''
Result: 
bug
An error in a progrram that prevents  the program from running expected.
function
A piece of code that you can easily call over and over Again
note : this function can print out key only
'''

'''
Exercise 1 - Grading Program
Instructions
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

This is the scoring criteria:
Scores 91 - 100: Grade = "Outstanding"
Scores 81 - 90: Grade = "Exceeds Expectations"
Scores 71 - 80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Fail"

Expected Output
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
'''
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
  score=student_scores[student]
  if score > 90:
    student_grades[student]="Outstanding"
  elif score > 80:
    student_grades[student]="Exceeds Expectations"
  elif score > 70:
    student_grades[student]="Acceptable"
  else:
    student_grades[student]="Fail"

# 🚨 Don't change the code below 👇
print(student_grades)


# Nasting list on dictionary
'''
Syntax:
{
    key:[list],
    key2:{dict},
}
'''
travel_log={
    "France":"city_visited":["Paris","Lille","dijon"],
    "Germany":"city_visited":["Berlin","Hamburg","Stuttgart"],
}

# Nasting Dictionary in a Dictionary
'''
Syntax:

'''

travel_log={
    "France":{"city_visited":["Paris","Lille","dijon"],"total_visited":12},
    "Germany":{"city_visited":["Berlin","Hamburg","Stuttgart"],"total_visited": 5},
}


# Nasting a dictionary inside of List.
travel_log=[{
    "country":"France",
    "city_visited" : ["Paris", "Lille","dijon"],
    "total_visited":12
    },
    {
    "country":"Germany",
    "city_visited":["Berlin","Hamburg","Stuttgart"],
    "total_visited": 5
}]

'''
You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.
Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
You've visited Russia 2 times.
You've been to Moscow and Saint Petersburg.

DO NOT modify the travel_log directly. You need to create a function that modifies it.
'''
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(name, visit_count, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = visit_count
  new_country["cities"] = cities_visited
  travel_log.append(new_country)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
