from turtle import *
screen = Screen()
screen.bgcolor("teal")
screen.setup(400, 400)

# def regular_polygon(turtle, sides):
#     turtle.begin_fill()
#     for i in range(sides):
#         turtle.forward(100/sides)
#         turtle.right(360/sides)
#     turtle.end_fill()

# # def draw():
# #     sides = int(input("How many sides does your shape have?"))


pen = Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()

# regular_polygon(pen, 3)

# while True:
#     sides = int(input("How many sides does the polygon have? "))
#     pen.clear()
#     if sides == 3:
#         regular_polygon(pen, sides)
#         name.write("TRIANGLE", font = ("Times New Roman", 20))


# screen.exitonclick()


# import turtle

# # Setup the screen and turtle
# screen = Turtle.Screen()
# t = turtle.Turtle()
# t.speed(3)

def draw_regular_polygon(sides, length):
    
    angle = 360 / sides
    for _ in range(sides):
        pen.forward(length)
        pen.left(angle)

def draw_rectangle(width, height):
    
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)

def draw_parallelogram(side1, side2, angle):
    for _ in range(2):
        pen.forward(side1)
        pen.right(angle)
        pen.forward(side2)
        pen.right(180 - angle)

def draw_trapezoid():
    
    pen.forward(150) 
    pen.left(120)
    pen.forward(60)
    pen.left(60)
    pen.forward(90)  
    pen.left(60)
    pen.forward(60)
    pen.setheading(0)

def draw_irregular_quad():
    pen.forward(100)
    pen.right(110)
    pen.forward(80)
    pen.right(100)
    pen.forward(110)
    pen.goto(0, 0) 
    pen.setheading(0)
