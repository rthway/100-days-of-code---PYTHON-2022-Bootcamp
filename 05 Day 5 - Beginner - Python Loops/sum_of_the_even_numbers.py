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