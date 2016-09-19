import turtle
import math
jerry = turtle.Turtle()
jerry.pensize(4)
jerry.hideturtle()


print(jerry)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.rt(angle)

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

#for i in range(0,6):
#    petal(jerry, 200, 360/6)
#    jerry.lt(360/6)
#arc(jerry, 200, 360/6)
#jerry.lt(61)
#circle(jerry,200)


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

jerry.lt(30)
bowtie(jerry, 200)
jerry.lt(90)
bowtie(jerry, 200)

jerry.fd(200)
jerry.lt(91)
jerry.circle(200)
jerry.lt(90)
jerry.fd(100)
jerry.circle(56)
jerry.rt(2)
jerry.fd(200)
circle(jerry, 56)
jerry.lt(180)
jerry.up()
jerry.fd(100)
jerry.lt(31)
jerry.fd(100)
jerry.down()
jerry.circle(56)
jerry.up()
jerry.lt(180)
jerry.fd(200)
jerry.down()
jerry.circle(56)







turtle.mainloop()