from turtle import *
import random




def gen_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def make_turtle():
    yert = Turtle()
    yert.shape("triangle")
    yert.setheading(random.randint(0, 360))
    yert.color(gen_color())


def play_area():
        
    pen = Turtle()
    # pen = Turtle.color(gen_color)
    pen.speed(0)
    pen.penup()
    pen.color("white")
    pen.hideturtle()
    
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(-240,-240)
    pen.goto(240,-240)
    pen.goto(240,240)
    pen.goto(-240,240)
    pen.end_fill()

def move_forward(turt):
    turt.forward(5)

    if turt.xcor() > 235 or turt.xcor() < -235: 
        turt.speed(0)
        turt.setheading(180- turt.heading()) 
        turt.forward(10)  
        turt.speed(.5)
    if turt.ycor() > 235 or turt.ycor() <-235:
        yert.speed(0)
        turt.setheading(0 - turt.heading())
        turt.forward(10)
        yert.speed(.5)

def move_xy(turt, deltaX, deltaY):
    newX = turt.xcor() + deltaX
    newY = turt.ycor() + deltaY

    #out of bounds or right or left
    if newX > 240 or newX < -240:
        deltaX *= -1
        newX = turt.xcor()
    #out of bounds top or bottom    
    if newY > 240 or newY < -240:
        deltaY *= -1
        newY = turt.ycor()

    turt.goto(newX, newY)
    return deltaX, deltaY

screen = Screen()
screen.bgcolor("black")
screen.setup(2256, 1504)

play_area()

yert = Turtle()
yert.shape("triangle")
yert.setheading(random.randint(0, 360))
yert.color(gen_color())
deltaX = random.randint(-5,5)
deltaY = random.randint(-5,5)

# while True:
#     move_forward(yert)

print(f"DeltaX = {deltaX} \nDeltaY = {deltaY}")   

while True:
    deltaX, deltaY = move_xy(yert, deltaX, deltaY)


screen.exitonclick()

