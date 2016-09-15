import turtle
import math
jerry = turtle.Turtle()

print(jerry)

def square(t, length):
    for i in range(0,4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    for i in range(0,n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n
    polygon(t, n, length)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

for i in range(0,10):
    arc(jerry,100,90)
    jerry.lt(90)
jerry.lt(90)
for i in range(0,10):
    arc(jerry,100,90)
    jerry.lt(90)







turtle.mainloop()