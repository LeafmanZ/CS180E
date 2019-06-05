""" 
Turtle drawing exercises for Python practice.

Author: Jim Zieleman
Date: May, 2019
"""

from turtle import *
        
def square(x, y, size):
    """ Draw a square at position (x, y) with the indicated size. """
    penup()
    goto(x, y)
    pendown()
    setheading(0)       # heading 0 is right, heading 90 is up. 
    for i in range(4):  # range(4) will yield 0, 1, 2, 3
        forward(size)
        left(90)

def rectangle(x, y, width, height):
    """ Draw a rectangle at position (x, y) with the indicated width and height. """
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    forward(width)
    left(90)
    forward(height)
    left(90)
    forward(width)
    left(90)
    forward(height)
    
def polygon(x, y, sides, size):
    """ Draw a polygon at position (x, y) with the indicated sides & size. """
    penup()
    goto(x, y)
    pendown()
    angles = 360.0/sides
    for i in range(sides):
        forward(size)
        left(angles)
        
def row(x, y, count, size):
    """ Draw a rectangle at position (x, y) with the indicated width and height. """
    penup()
    goto(x, y)
    pendown()
    for i in range(count):
        x += 5 + size
        square(x, y, size)

def grid(x, y, rows, columns, size):
    blue_bool = True
    orig_x = x
    penup()
    goto(x, y)
    pendown()
    for r in range(rows):
        y -= (5+size)
        x = orig_x
        if (r%2 == 0):
            blue_bool = True
        else:
            blue_bool = False
        for c in range(columns):
            x += 5 + size
            if blue_bool:
                fillcolor('blue')
                begin_fill()
                square(x, y, size)
                end_fill()
                fillcolor('black')
                blue_bool = False
            else:
                square(x, y, size)
                blue_bool = True
                
def main():
    """ Tests of drawing functions. """
    """rectangle(50, 50, 90, 120)
    polygon(-300, -200, 5, 80)
    row(-400,0,5,120)"""
    grid(-500, 0, 2, 5, 20)

    exitonclick()

if __name__ == "__main__":
    main()
