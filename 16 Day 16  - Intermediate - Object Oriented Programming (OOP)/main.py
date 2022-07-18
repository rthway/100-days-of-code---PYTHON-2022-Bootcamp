
##### EX-1####
## Create a main.py file inside a new project 
main.py
import another_module
print(another_module.another_variable)
## create a another_module inside a same project 
another_module.py
another_variable=12
# output
output is : 12

#### EX-2 ####
import turtle 
timmy = turtle.Turtle()
# same as 
from turtle import Turtle
timmy=Turtle()
print(timmy)

#### EX-3 ####

from turtle import Turtle,Screen #Turtle,Screen are class inside the turtle files 
timmy=Turtle()
print(Turtle)

my_screen=Screen()
print(Screen.canvheight)
# Where Screen is object and canvleight is attribute
my_screen.exitonclick()
# Where exitonclick() is function 

#### Python Packages ####
# we can add many python package from pypi.org (pypi stand for python package index)

#### Ex- 4 ####
# Install PrettyTable and store pokemon name and type inside a table 
'''
## Install package PrettyTable
> Goto pycharm 
> python package
> Search PrettyTable
> install it
'''
from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("type",["Electric","Water","Fire"])
print(table)

# output 
'''
+--------------+----------+
| Pokemon Name |   type   |
+--------------+----------+
|   Pikachu    | Electric |
|   Squirtle   |  Water   |
|  Charmander  |   Fire   |
+--------------+----------+
'''

#### Ex- 5 ####
# in the previous code change set the align of text is left
from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("type",["Electric","Water","Fire"])
table.align="l"
print(table)


# output 
'''
+--------------+----------+
| Pokemon Name | type     |
+--------------+----------+
| Pikachu      | Electric |
| Squirtle     | Water    |
| Charmander   | Fire     |
+--------------+----------+
'''






