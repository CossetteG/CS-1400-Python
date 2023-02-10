"""
Project Name: Turtle Patters: YIN and YANG
Author: Cossette
Due Date: today (2/5/23)
Course: CS1400-zzz

Ok so importing the turtle and also defining the turtle
are both outside of functions because they are necessary
so please don't doc points for that

also I'm putting the setup in get get_dimensions()
and putting my functions after initializing the turtle
so it doesn't freak out that t.whatever isn't defined
I dont know if it's gonna me points for that

"""
import turtle as t

# print("test")


def get_dimensions():
    """input dimensions to put in the turtle"""
    w = int(input())
    h = int(input())
    # I like my demensions at 500,400

    if w <= 0 or h <= 0:
        raise ValueError("Width and height must be positive integers.")
    return w, h


# get_dimensions()
# t = turtle.Turtle()


def draw_circle(scale):
    """draws a circle, turning right. Put in a scale agrument"""
    for _ in range(180):
        t.forward(scale * 2)
        t.rt(2)


def draw_right_half_circle(scale):
    for _ in range(180):
        t.forward(scale)
        t.rt(1)


def draw_left_half_circle(scale):
    for _ in range(180):
        t.forward(scale)
        t.lt(1)


def draw_moon(scale):
    """draws a moon"""
    t.setheading(160)
    for _ in range(288):
        t.forward(scale)
        t.lt(1)

    t.lt(160)
    for _ in range(215):
        t.forward(scale * 0.85)
        t.rt(1.18)


def draw_rays(scale):
    adjusted_scale = scale * 20 / 2.4
    t.forward(adjusted_scale)
    t.rt(130)
    t.forward(adjusted_scale)
    t.lt(120)


def draw_sun(scale):
    """draws a circle and triangle rays"""
    t.setheading(0)
    draw_circle(scale * 0.7)
    t.setheading(60)
    for _ in range(360 // 10):
        draw_rays(scale)


def move_ur_pen(x, y):
    """Moves pen without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw(width, height):
    """
    Sets the size of the screen to width and height and draws a doodle.
    UM ACTUALLY they should already be set at this point so
    it's just gonna draw
    """
    # (2) replace pass with your code
    # print("test print")

    t.setup(width, height)

    move_ur_pen(0, 115)

    num = 115 // 4

    t.fillcolor("gray0")
    t.begin_fill()
    draw_right_half_circle(2)
    draw_right_half_circle(1)
    draw_left_half_circle(1)
    t.end_fill()
    draw_left_half_circle(2)

    move_ur_pen(10, -num)

    t.pencolor("SteelBlue")
    t.fillcolor("SteelBlue")
    t.begin_fill()
    draw_moon(0.6)
    t.end_fill()

    move_ur_pen(0, 115 - num)

    t.pencolor("gold4")
    t.fillcolor("goldenrod")
    t.begin_fill()
    draw_sun(0.7)
    t.end_fill()


if __name__ == "__main__":
    wid, heig = get_dimensions()
    draw(wid, heig)
    t.mainloop()
