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