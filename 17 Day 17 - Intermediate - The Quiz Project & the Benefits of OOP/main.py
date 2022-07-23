'''
#### NOTE ####
## 1-Class is blueprint of programming

## 2- There are three types of case using in Pyhton.
PascalCase > Capitalize each word
camelCase > Capitalize each word expect start once
snake_case > all small and _ used as sepretor
## 3 - Attributes are like variable eg car="Tesla"
#### Class Syntax ####
class <ClassName>:
eg:
class Car:
'''

#### Create attrubites in class###

class User:
    pass #to continue

user_1=User()
user_1.id="001"
user_1.name="Roshan"
print(user_1.name)

user_2=User()
user_2.id="002"
user_2.name="Jack"
print(user_2.name)

#### Constructor ####
# In python The way we would create the constructor using by special function.
Syntax :
class Car:
    def __init__(self):
    # initialize attributes

## Constructor with attributes ##
class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
user_1 = User("001", "Roshan")
user_2 = User("002","Jack")
print(user_1.username)

#### Adding methods to a Class ####
'''
Car     attributes:
            seats=5
        methods:
            def enter_race_mode():
                seats=2

# The full code is:
class Car:
    def enter_race_mode():
        self.seats=2

my_car.enter_race_mode() # to call function

'''
## user follow code ##
class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following =0

    def follow(self,user):
        user.followers +=1
        self.following +=1

user_1 = User("001", "Roshan")
user_2 = User("002","Jack")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

#### The Quiz Game####
## Creating a question Class##
'''
Question
    attributes
        text
        answer
    method
    
    
## QuizBrain ##
QuizBrain
    attributes
        question_number=0
        question_list 
    method
        next question
        
'''


