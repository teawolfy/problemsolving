import turtle
import math
jerry = turtle.Turtle()
jerry.pensize(4)
jerry.hideturtle()


print(jerry)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n
    polygon(t, n, length)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def petal(t, r, angle):
    for i in range(0,2):
        arc(t, r, angle)
        t.lt(180-angle)

def bowtie(t, length):
    t.fd(length)
    t.rt(120)
    t.fd(length)
    t.rt(120)
    t.fd(length*2)
    t.lt(120)
    t.fd(length)
    t.lt(120)
    t.fd(length)

def problem1():
    for i in range(0,6):
        petal(jerry, 200, 360/6)
        jerry.lt(360/6)
    arc(jerry, 200, 360/6)
    jerry.lt(61)
    circle(jerry,200)

def problem2():
    jerry.lt(30)
    bowtie(jerry, 200)
    jerry.lt(90)
    bowtie(jerry, 200)

    jerry.fd(200)
    jerry.lt(91)
    jerry.circle(200)
    jerry.lt(90)
    jerry.fd(100)
    jerry.circle(55)
    jerry.rt(.5)
    jerry.fd(100)
    jerry.lt(28)
    jerry.fd(100)
    jerry.circle(57)
    jerry.rt(178)
    jerry.fd(200)
    jerry.circle(55)
    jerry.lt(180)
    jerry.fd(100)
    jerry.rt(90)
    jerry.fd(100)
    jerry.circle(55)

def problem3(radius):
    jerry.circle(radius/2., 180)
    jerry.circle(radius, 180)
    jerry.left(180)
    jerry.circle(-radius/2., 180)
    jerry.left(90)
    jerry.up()
    jerry.forward(radius*0.35)
    jerry.right(90)
    jerry.down()
    jerry.circle(radius*0.15)
    jerry.left(90)
    jerry.up()
    jerry.backward(radius*0.35)
    jerry.down()
    jerry.left(90)
    jerry.circle(radius/2., 180)
    jerry.circle(radius, 180)
    jerry.left(180)
    jerry.circle(-radius/2., 180)
    jerry.left(90)
    jerry.up()
    jerry.forward(radius*0.35)
    jerry.right(90)
    jerry.down()
    jerry.circle(radius*0.15)
    jerry.left(90)
    jerry.up()
    jerry.backward(radius*0.35)
    jerry.down()
    jerry.left(90)

def spiral(t):
    length = 10
    x = 0
    for i in range(300):
        t.fd(length)
        y = 1 / (.01 + x * .0002)
        t.lt(y)
        x += y

def myreset(t):
    t.reset()
    t.pensize(4)
     
spiral(jerry)
myreset(jerry)
problem1()
myreset(jerry)
problem2()
myreset(jerry)
problem3(200)

turtle.mainloop()