'''
Q.1 -
You are going to write a program that calculates the average student height from a List of heights.
The average height can be calculated by adding all the heights together and dividing by the total number of heights.
Average height rounded to the nearest whole number = 164
Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

Example Input
156 178 165 171 187
In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

Example Output
171
'''

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height =0
for height in student_heights:
    total_height +=height
#print (total_height)

total_student = 0
for student in student_heights:
    total_student+=1
#print(total_student)

Avrage_height=round(total_height/total_student)
print(Avrage_height)

''' 
Q.2 You are going to write a program that calculates the highest score from a List of scores.
Important you are not allowed to use the max or min functions. The output words must match the example. i.e
The highest score in the class is: x
Example Input
78 65 89 86 55 91 64 89
Example Output
The highest score in the class is: 91
'''
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

heighest_score=0
for score in student_scores:
    if score > heighest_score:
        heighest_score=score
print(f"The highest score in the class is: {heighest_score}")


#Q.3 WAP to dispaly sum of all number 1-100.
total=0
for number in range(1,101):
  total += number
print(total)


# Q-4 You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
#Write your code below this row 👇
total=0
for number in range(2,101,2):
    total+=number
   # print(number)
print(total)

#another method 
total=0
for number in range(2,101):
  if number % 2==0:
    total+=number
    
   # print(number)
print(total)

'''Q.5  
You are going to write a program that automatically prints the solution to the FizzBuzz game.
Your program should print each number from 1 to 100 in turn.
When the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
  And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
'''
#Write your code below this row 👇
for number in range(1,101):
  if number % 3==0 and number%5==0:
    print("FizzBuzz")
  elif number % 3==0:
    print("Fizz")
  elif number % 5==0:
    print("Buzz")
  else:
    print(number)

# Q.6 WAP to random generate password in python 
# Easy_level
import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','*']
nr_letters=int(input("how many letters would you like your password \n"))
nr_numbers=int(input("how many number would you like your password \n"))
nr_symbols=int(input("how many symbols would you like your password \n"))
password=""
for char in range (1,nr_letters+1):
  password += random.choice(letters)
for char in range (1,nr_numbers+1):
  password += random.choice(numbers)
for char in range (1,nr_symbols+1):
  password += random.choice(symbols)
print(f"Your password would be {password}")


#Hard level
import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','*']
nr_letters=int(input("how many letters would you like your password \n"))
nr_numbers=int(input("how many number would you like your password \n"))
nr_symbols=int(input("how many symbols would you like your password \n"))
password_list=[]
for char in range (1,nr_letters+1):
  password_list.append(random.choice(letters))
for char in range (1,nr_numbers+1):
  password_list.append(random.choice(numbers))
for char in range (1,nr_symbols+1):
  password_list.append(random.choice(symbols))

random.shuffle(password_list)

password=""
for char in password_list:
  password+=char
print(f"Your password would be {password}")




