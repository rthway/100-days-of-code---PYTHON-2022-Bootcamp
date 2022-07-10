# Simple function
def greet():
  print("hello")
  print("How are you")
  print("Isn't the weather nice today?")
greet()

#function that allow input
def greet_with_name(name):
  print(f"hello {name}")
  print(f"How are you {name}")
  print(f"Isn't the weather nice today?")
greet_with_name("Roshan")
# note: where name is parameter and Roshan Argument



# function that allows with more then 1 inputs 
def greet_with(name,location):
  print(f"hello {name}")
  print(f"what is it like in {location}")
greet_with("Roshan","KTM")

''' # positional Agruments vs Keyword Arguments #
# Positionnal Agruments
def my_function(a,b,c):
  do this with a
  then do this with b
  finally do this with c
my_function(1,2,3)
result are : a=1 , b=2, c=3

# Keyword agruments 
def my_function(a,b,c):
  do this with a
  then do this with b
  finally do this with c
my_function(a=3 , b=1, c=2)
result are : a=3 , b=1, c=2
'''
'''
Q. 1 - Paint Area Calculator 
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
number of cans = (wall height ✖️ wall width) ÷ coverage per can.
e.g. Height = 2, Width = 4, Coverage = 5
number of cans = (2 ✖️ 4) ÷ 5

                     = 1.6

Example Input: 
test_h = 3
test_w = 9
Example Output:
You'll need 6 cans of paint.
'''
#Write your code below this line 👇
def paint_calc(height,width,cover):
  area=(height * width) / cover
  area_cans=round(area)
  print(f"You'll need {area_cans} cans of paint.")


# Q-2 - WAP to display input value is prime number or not.
# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Check input number is Prime or not
#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


#caeser_cipher (Encrypt and Discrypt any massage.)

alphabet= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input ("Type 'encode' to encrypt, Type decode to 'decrypt'\n")
text=input("Type your massage: \n")
shift=int(input("type the shift number: \n"))

def caeser(start_text,shift_amount,cipher_direction):
  end_text=""
  if cipher_direction == "decode":
     shift_amount *= -1
  for letter in start_text:
    position=alphabet.index(letter)
    new_position=position+shift_amount
    new_letter=alphabet[new_position]
    end_text += new_letter
  print(f"Here the {direction}d. The encoded text is {end_text}")

caeser(start_text=text, shift_amount=shift, cipher_direction=direction)








