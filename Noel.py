from turtle import *
import random
import time

# Drawing Santa Hat
def drawHat():
    pen.speed(1)
    pen.color('red')
    pen.fillcolor('red')
    pen.begin_fill()
    for i in range(3):
        pen.fd(50)
        pen.right(120)
    pen.end_fill()
    for i in range(6):
        pen.dot(10,'white')
        pen.fd(10)
    pen.right(130)
    pen.fd(55)
    pen.dot(10,'white')

# Width and Height of Tree Object 
n = 170
speed("fastest")
left(90)
forward(3*n)
# Celebration Card setup
card=Screen()
card.setup(1.0,1.0,0,0)
card.title("Em gái Hạ Vy")
colors=['#92b6f0','#d95d78','#5cdbb5','#5ccde0','#e0d758','#ed9277']
card.bgcolor(random.choice(colors))
time.sleep(2)
# Tree color
color("dark green")
# Draw backward desgin cordinates
backward(n*4.8)
# Turn turtle animation on/off and set delay for update drawings
tracer(8,50)

# Draw Christmas Tree
def tree(d, s):
    if d <= 0:
        return
    forward(s)
    tree(d-1, s*.8)
    right(120)
    tree(d-3, s*.5)
    right(120)
    tree(d-3, s*.5)
    right(120)
    backward(s)

# Draw Snow before Christmas Tree
def makeSnow():
    for i in range(50):
        snow=Turtle()
        snow.pu()
        snow.color("white")
        snow.shape("circle")
        snow.speed(0)
        snow.goto(random.randint(-700,700),random.randint(-700,700))
        snow.dot(7,'white')
        snowlist.append(snow)

# Snowfall 
def snowfall():
    for i in snowlist:
        i.goto(random.randint(-700,700),random.randint(-700,700))
        i.dot(7,'white')

# Calling makeSnow funtion
snowlist=[]
makeSnow()
time.sleep(1)
# Draw Merry Christmas heading
pen=Turtle()
pen.speed(10)
# pen.hideturtle()
pen.left(270)
pen.penup()
pen.forward(400)
pen.color("black")
pen.setx(-395)
pen.color('Yellow')
pen.write("Merry Christmas Vy  !!",font=("ravie",40,"italic"),align="left")

# Calling Draw hat funtion
pen.setheading(0)
pen.speed(1)
pen.fd(850)
pen.left(145)
pen.fd(40)
time.sleep(1)
drawHat()
tree(15, n)

card.tracer(False)
card.tracer(True)

while True:
    snowfall()
    card.bgcolor(random.choice(colors))
              
backward(n/2)
bye()