

import turtle

def get_dimensions():
    """input dimensions to put in the turtle"""
    w = input()
    h = input()

    #I like my demensions at 500,400

    if int(w) > 0 and int(h) > 0:
        turtle.setup(int(w), int(h))
    else:
        print("Width and height must be positive integers.")
        exit()

get_dimensions()
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

def draw_rays(scale):
    adjusted_scale = scale*20/2.4
    t.forward(adjusted_scale)
    t.rt(130)
    t.forward(adjusted_scale)
    t.lt(120)

def draw_sun(scale):
    """draws a circle and triangle rays"""
    t.setheading(0)
    draw_circle(scale*.7)
    t.setheading(60)
    for i in range(360//10):
        draw_rays(scale)

def move_ur_pen(x,y):
    """Moves pen without drawing"""
    t.penup()
    t.goto(x,y)
    t.pendown()


#Call functions start here


def draw():

    move_ur_pen(0,115)

    num = 115//4

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
    draw_moon(.6)
    t.end_fill()

    move_ur_pen(0, 115-num)

    t.pencolor("gold4")
    t.fillcolor("goldenrod")
    t.begin_fill()
    draw_sun(.7)
    t.end_fill()

    turtle.mainloop()

draw(1,1)

'''
Copied *exactly* as it is in codio

'''
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
'''
import turtle

#print("test")

def get_dimensions():
    """input dimensions to put in the turtle"""
    w = input()
    h = input()
    #print("Test three")
    #I like my demensions at 500,400

    if int(w) > 0 and int(h) > 0:
        turtle.setup(int(w), int(h))
        #print("test too")
    else:
        print("Width and height must be positive integers.")
        exit()

get_dimensions()
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

def draw_rays(scale):
    adjusted_scale = scale*20/2.4
    t.forward(adjusted_scale)
    t.rt(130)
    t.forward(adjusted_scale)
    t.lt(120)

def draw_sun(scale):
    """draws a circle and triangle rays"""
    t.setheading(0)
    draw_circle(scale*.7)
    t.setheading(60)
    for i in range(360//10):
        draw_rays(scale)

def move_ur_pen(x,y):
    """Moves pen without drawing"""
    t.penup()
    t.goto(x,y)
    t.pendown()



def draw(width, height):
    """
    Sets the size of the screen to width and height and draws a doodle.
    UM ACTUALLY they should already be set at this point so 
    it's just gonna draw
    """
    # (2) replace pass with your code
    #print("test print")

    move_ur_pen(0,115)

    num = 115//4

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
    draw_moon(.6)
    t.end_fill()

    move_ur_pen(0, 115-num)

    t.pencolor("gold4")
    t.fillcolor("goldenrod")
    t.begin_fill()
    draw_sun(.7)
    t.end_fill()

    turtle.mainloop()

draw(1,1)

'''

'''
And here's the error message

Traceback (most recent call last):
  File ".guides/secure/turtle_grader.py", line 253, in 
    main()
  File ".guides/secure/turtle_grader.py", line 172, in main
    mut = import_program(program)
  File ".guides/secure/turtle_grader.py", line 26, in import_program
    return importlib.import_module(package_name)
  File "/usr/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "", line 994, in _gcd_import
  File "", line 971, in _find_and_load
  File "", line 955, in _find_and_load_unlocked
  File "", line 665, in _load_unlocked
  File "", line 678, in exec_module
  File "", line 219, in _call_with_frames_removed
  File "/home/codio/workspace/doodles.py", line 35, in 
    get_dimensions()
  File "/home/codio/workspace/doodles.py", line 23, in get_dimensions
    w = input()
EOFError: EOF when reading a line
'''