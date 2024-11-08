
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""
from turtle import turtles
import turtle


turtle.setup (width=300, height=300)    # Set the size of the window

tina = turtle.Turtle() 
tina.color("yellow")
tina.begin_fill()

window=turtle.Screen ()                # Create a turtle named tina
window.bgcolor('turquoise')

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(100000)                           # Make the turtle move as fast, but not too fast. 
tina.forward(150)                     # Move tina forward by the forward distance
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
tina.pendown()

tina.penup()
tina.begin_fill()
tina.fillcolor("white")
tina.right(90)
tina.forward(40) 

tina.forward(50)
tina.left(90)

tina.forward(20)
tina.left(90)

tina.forward(240)
tina.left(90)

tina.forward(20)
tina.left(90)
tina.forward(40) 
tina.forward(100)
tina.pendown()
tina.end_fill()


tina.penup()

tina.left(90)
tina.forward(40)
tina.begin_fill()
tina.fillcolor("white")
tina.left(90)
tina.forward(140)
tina.right(90)
tina.forward(20)
tina.right(90)
tina.forward(240)
tina.right(90)
tina.forward(20)
tina.right(90)
tina.forward(240) 
tina.end_fill()

turtle.exitonclick() 
... # Your code here

