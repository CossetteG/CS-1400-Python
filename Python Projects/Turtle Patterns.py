import turtle
turtle.setup(500,400)

t = turtle.Turtle()

def draw_circle(scale):
    """draws a circle, turning right. Put in a scale agrument"""
    for i in range(180):
        t.forward(scale*2)
        t.rt(2)

def draw_right_half_circle(scale):
    for i in range(180):
        t.forward(scale)
        t.rt(1)

def draw_left_half_circle(scale):
    for i in range(180):
        t.forward(scale)
        t.lt(1)

def draw_moon(scale):
    """draws a moon"""
    t.setheading(160)
    for i in range(288):
        t.forward(scale)
        t.lt(1)

    t.lt(160)
    for i in range(215):
        t.forward(scale*.85)
        t.rt(1.18)


#Call functions start here


t.penup()
t.goto(0,115)
t.pendown()


turtle.mainloop()