import turtle
import random

s = turtle.getscreen()
t = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()

turtle.bgcolor("cyan")
turtle.title("Turtle Fun")
t.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")

i = 1
t.speed(500)
t2.speed(500)
t3.speed(500)
t4.speed(500)

while True:
    t.setpos(i, i*2)
    t2.setpos(i*2, i)
    t3.setpos(-i,-i)
    t4.setpos(-i*2, i)
    i += 1
    t.circle(i)
    t2.circle(i)
    t3.circle(i)
    t4.circle(i)

turtle.exitonclick()
