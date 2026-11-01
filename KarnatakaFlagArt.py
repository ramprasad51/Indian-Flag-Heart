import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Kannada Nadu")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)

# Karnataka Flag Colors
YELLOW = "#FFD700"
RED = "#FF0000"

# Select colour based on Y coordinate
def flag_color(y):
    if y >= 0:
        return YELLOW
    else:
        return RED


# Draw mathematical heart shape
for i in range(180):

    t.penup()
    t.goto(0, 40)

    angle = i * (2 * math.pi / 180)

    x = 16 * (math.sin(angle) ** 3) * 15

    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    ) * 15

    # Draw heart using Karnataka flag colours
    for k in range(51):

        progress = k / 50

        current_x = x * progress
        current_y = 40 + (y - 40) * progress

        t.color(flag_color(current_y))

        if k == 0:
            t.penup()
        else:
            t.pendown()

        t.goto(current_x, current_y)

# Display Kannada text
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0, -230)
text.color("#FFD700")
text.write(
    "ಜೈ ಕರ್ನಾಟಕ!",
    align="center",
    font=("Noto Sans Kannada", 28, "bold")
)


turtle.done()