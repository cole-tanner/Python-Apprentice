"""
Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section " Click on the Turtle"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and when you click on it, it moves to a random location on the screen.

Use this code to get a random x and y location


    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

""" 
                         # Tell Python we want to work with the turtle
from turtle import turtles
import turtle


turtle.setup (width=300, height=300)    # Set the size of the window

tina = turtle.Turtle() 
tina.color("yellow")
tina.begin_fill()                 # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(1)                           # Make the turtle move as fast, but not too fast. 

tina.forward(150)                       # Move tina forward by the forward distance
tina.left(90)                           # Turn tina left by the left turn

tina.forward(150)                       # Continue the last two steps three more times
tina.left(90)  
tina.forward(90)                         # to draw a square

tina.forward(150)
tina.left(90)

tina.forward(150)
tina.left(90)
tina.left(90)
tina.right(90)
tina.forward(90)
tina.color("red")
tina.penup()
tina.end_fill()


tina.color("blue")
tina.begin_fill()     
tina.left(90)
tina.forward(90)
tina.pendown()
tina.color("blue")
tina.left(90)
tina.forward(90)
tina.right(90)
tina.forward(60)
tina.right(90)
tina.forward(90)
tina.right(90)
tina.forward(60)


tina.end_fill()

tina.right(180)
tina.forward(30)

tina.penup()

tina.begin_fill()
tina.right(90)
tina.forward(150)
tina.fillcolor("white")
tina.right(90)
tina.forward(20)

tina.right(90)
tina.forward(150)
tina.end_fill()
tina.pendown()

tina.penup()
tina.left(90)
tina.forward(20)

tina.right(90)
tina.forward(20)

turtle.exitonclick()                    # Close the window when we click on it
