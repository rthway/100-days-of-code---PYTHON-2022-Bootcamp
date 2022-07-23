#### Turtle Lession ####
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)

screen= Screen()
screen.exitonclick()


### Turtle Challanges ####
# Draw a Square
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)

screen= Screen()
screen.exitonclick()

## Esy way ##
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


#### Import in Turtle module ####
## basic Import ##
import turtle # import is keyword turtle is module name
tim=turtle.Turtle()

## from .. import ...##
from turtle import Turtle # from : keyword , turtle: module name , import: keyword and Turtle thing in module
tim =Turtle() # in this method we don't need to write turtle.Turtle()

## from .. import *
#note : avoid the code writing like this


##  Aliasing Modules
import turtle as t
tim=t.Turtle()

## Installing Module ##
# > goto pypi.org > search package then install it using pip install

## Turtle Challenge : 2 ##
# Draw a dashed line
import turtle as t
tim=t.Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

#### Turtle Challenge 3 - Drawing Different Shapes ####
# Draw a tringle, Squre, Pentagon, Hexagon, Heptagon, Octagon, nonagon and decagon with different color
import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

#### Challenge 4 - Random Walk ####
import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))

#### Challenge 5 - Spirograph #####
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

