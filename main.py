import random
from turtle import Turtle, Screen
from random import choice

# Setting up turtle and screen objects.
my_turtle = Turtle()
my_turtle.speed(0)
screen = Screen()
screen.colormode(255)
screen.setup(width=1000, height=1000)

# Orientation list and Movement
orinet_list = [0, 90, 180, 270]
movement = [0, 10, 5 ,15, 1, 20]


# Glorious for loop
for i in range(1000):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    my_turtle.forward(choice(movement))
    my_turtle.setheading(choice(orinet_list))
    my_turtle.pencolor(r, g, b)





screen.exitonclick()
