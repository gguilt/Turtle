import turtle
import random

s = turtle.getscreen()
t = turtle.Turtle()

turtle.bgcolor("cyan")
turtle.title("Turtle Fun")
t.shape("turtle")

i = 1

t.rt(90)
t.speed(500)

starty = turtle.ycor()
mad = 1

while True:
    t.fd(i * mad)
    t.circle(i)
    i += 1

    print(t.ycor())

    if t.ycor() < -500:
        mad = -1
    elif t.ycor() >= 0:
        mad = 1

turtle.exitonclick()
