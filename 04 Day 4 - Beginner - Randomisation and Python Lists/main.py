# Q.1 Write a program to haad and tail randomize using random module.
import random
ramdom_integer =random.randint(0,1)
if ramdom_integer == 1:
    print("Heads")
else:
    print("Tails")

''' Q.2 You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.
Example Output
Michael is going to buy the meal today!
Hint
You might need the help of the len() function.
'''
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# to get the total number of list
x= len(names)
random_choice = random.randint(0,x-1) # because indexing start from 0 and len start from 1
person_who_will_pay=names[random_choice]
print(person_who_will_pay + " is going to buy the meal today!")


'''
First, your program must take the user input and convert it to a usable format.
Next, you need to use it to update your nested list with an "x".

Example Input 1
column 2, row 3 would be entered as:
23
Example Output 1
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
Example Input 2
column 3, row 1 would be entered as:
31
Example Output 2
['⬜️', '⬜️', 'X']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
e.g. When you hit run, this is what should happen:
'''
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizonal=int(position[0])
vertical=int(position[1])
selected_row=map[vertical -1 ]
selected_row[horizonal -1 ]= "X"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

# Q. 3 WAP for a game Rock, paper, Scissors
import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")