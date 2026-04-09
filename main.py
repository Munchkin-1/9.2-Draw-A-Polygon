from turtle import *
screen = Screen()
screen.bgcolor("teal")
screen.setup(400, 400)

def regular_polygon(turtle, sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(100/sides)
        turtle.right(360/sides)
    turtle.end_fill()

# def draw():
#     sides = int(input("How many sides does your shape have?"))


pen = Turtle
pen.speed(0)
pen.color("white")
pen.hideturtle()

regular_polygon(pen, 3)

while True:
    sides = int(input("How many sides does the polygon have? "))
    pen.clear()
    if sides == 3:
        regular_polygon(pen, sides)
        name.write("TRIANGLE", font = ("Times New Roman", 20))
screen.exitonclick()