import turtle

a = turtle.Turtle()
a.pensize(5)
a.speed(2)
a.color("Red")
for i in range(4) :
    a.forward(100)
    a.left(90)

b = turtle.Turtle()
b.speed(2)
b.color("Green")
for i in range(0,4) :
    b.backward(100)
    b.left(90)

turtle.exitonclick()