import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("Black")
t.speed(10000)
n=50
h=100
for i in range(1000):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=1/n
    t.color(c)
    t.right(5)
    for j in range(5):
        t.backward(250)
        t.right(145)
        t.circle(50)
        t.tiltangle(10010)