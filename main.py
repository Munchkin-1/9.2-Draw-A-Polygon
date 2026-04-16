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
        pen.left(90)
        pen.forward(height)
        pen.left(90)

def draw_parallelogram(side1, side2, angle):
    for _ in range(2):
        pen.forward(side1)
        pen.left(angle)
        pen.forward(side2)
        pen.left(180 - angle)

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
    pen.left(110)
    pen.forward(80)
    pen.left(100)
    pen.forward(110)
    pen.goto(0, 0)
    pen.setheading(0)


sides = int(input("How many sides does your shape have? "))

if sides == 3:
    print("This is a Triangle.")
    draw_regular_polygon(3, 100)

elif sides == 4:
    is_all_sides_equal = input("Are all four sides the same length? (yes/no): ").lower()
    
    if is_all_sides_equal == "yes":
        print("This is a Square.")
        draw_regular_polygon(4, 100)
    else:
        is_all_angles_equal = input("Are all four angles the same measure? (yes/no): ").lower()
        if is_all_angles_equal == "yes":
            print("This is a Rectangle.")
            draw_rectangle(150, 80)
        else:
            is_parallel_pairs = input("Is each side parallel to one other side? (yes/no): ").lower()
            if is_parallel_pairs == "yes":
                print("This is a Parallelogram.")
                draw_parallelogram(120, 70, 70)
            else:
                is_two_parallel = input("Are exactly two sides parallel to each other? (yes/no): ").lower()
                if is_two_parallel == "yes":
                    print("This is a Trapezoid.")
                    draw_trapezoid()
                else:
                    print("This is an Unknown Quadrilateral.")
                    draw_irregular_quad()

elif sides == 5:
    print("This is a Pentagon.")
    draw_regular_polygon(5, 100)

elif sides == 6:
    print("This is a Hexagon.")
    draw_regular_polygon(6, 80)

else:
    print("Unknown polygon.")
    if sides > 0:
        draw_regular_polygon(sides, 50)

print("Drawing complete.")
screen.mainloop()





turtles = [yertle]
