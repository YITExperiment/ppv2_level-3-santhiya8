import turtle
from itertools import cycle
colors=cycle(['red','orange','blue','purple','black','orange'])


def draw_circle(size,angle,shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+3,angle+4,shift+3)
turtle.bgcolor('blue')
turtle.speed('slow')
turtle.pensize(30)
draw_circle(20,0,5)
    
