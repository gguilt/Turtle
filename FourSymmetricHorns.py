import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.bgcolor("cyan")
turtle.title("Turtle Fun")
t.shape("turtle")

i = 1

t.rt(90)
t.fd(100)
t.speed(500)

while True:
    t.rt(90)
    t.circle(i)
    t.rt(90)
    t.circle(i)
    if i > 500:
        i -= 1
    else:
        i += 1

turtle.exitonclick()
