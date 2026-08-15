import turtle
import math

#colours
SAFFRON="#FF9933"
WHITE="#FFFFFF"
GREEN="#138808"
NAVY_BLUE="#000080"

def flag_color(y):
    if y > 80:
        return SAFFRON
    elif y > -60:
        return WHITE
    else:
        return GREEN
    
#Turtle setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Indian Flag Heart")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)


#Heart shape
for i in range(120):
    t.penup()
    t.goto(0, 40)

    angle = i * (math.pi * 2) / 120

    x = 16 * (math.sin(angle) ** 3)*15

    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    ) * 15

    #Tricolor flag effect
    for k in range(41):
        progress = k / 40
        current_x = x * progress
        current_y = 40+(y - 40) * progress
        t.color(flag_color(current_y))

        if k == 0:
            t.penup()
        else:
            t.pendown()
        t.goto(current_x, current_y)

#Ashoka Chakra
cx = 0
cy= 40
CHAKRA_BLUE = "#0000FF"
radius = 30

t.penup()
t.goto(cx,cy-radius)
t.setheading(0)

t.color(WHITE)
t.fillcolor(WHITE)

t.begin_fill()
t.pendown()
t.circle(radius)
t.end_fill()

t.color(CHAKRA_BLUE)
t.pensize(4)

t.penup()
t.goto(cx,cy-27)
t.setheading(0)
t.pendown()
t.circle(27)

for i in range(24):
    angle = i * (360 / 24)
    t.penup()
    t.goto(cx,cy)
    t.setheading(angle)
    t.pendown()
    t.forward(24)
    t.penup()
    t.goto(cx,cy-5)
    t.setheading(0)
    t.pendown()
    t.circle(5)  
t.penup()
t.goto(cx,cy-2)
t.dot(4, CHAKRA_BLUE)
turtle.done()

