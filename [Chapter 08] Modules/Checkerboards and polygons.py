""" 
Turtle drawing exercises for Python practice.

Author: Jim Zieleman
Date: May, 2019
"""

from turtle import *

""" FOR PROBLEM 1 """
def checkerboard(x, y, rows, columns, size):
    blue_bool = True
    orig_x = x
    penup()
    goto(x, y)
    pendown()
    for r in range(rows):
        y -= (size)
        x = orig_x
        if (r%2 == 0):
            blue_bool = True
        else:
            blue_bool = False
        for c in range(columns):
            x += size
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
    exitonclick()
                
""" FOR PROBLEM 1 """
def square(x, y, size):
    """ Draw a square at position (x, y) with the indicated size. """
    penup()
    goto(x, y)
    pendown()
    setheading(0)       # heading 0 is right, heading 90 is up. 
    for i in range(4):  # range(4) will yield 0, 1, 2, 3
        forward(size)  
        left(90)

def draw_polygon_file(fname):
    line_numbers = []
    for line in open(fname):
        line_numbers = line.split()
        polygon(int(line_numbers[0]), int(line_numbers[1]), int(line_numbers[2]), int(line_numbers[3]))
        
def polygon(x, y, sides, size):
    """ Draw a polygon at position (x, y) with the indicated sides & size. """
    penup()
    goto(x, y)
    pendown()
    angles = 360.0/sides
    for i in range(sides):
        forward(size)
        left(angles)
    
        
def format_str(description, values):
    new_string = description
    num_cash = new_string.count('$')
    placeholder = ''
    for i in range(num_cash):
        placeholder = '$'+ str(i)
        if i >= len(values):
            new_string = new_string.replace(placeholder, 'ERROR')
        else:
            new_string = new_string.replace(placeholder, values[i])
    
    return new_string
    
def main():
    """ Tests of drawing functions. """
    """rectangle(50, 50, 90, 120)
    polygon(-300, -200, 5, 80)
    row(-400,0,5,120)
    checkerboard(-200, 0, 5, 11, 20)
    speed(0)
    draw_polygon_file("polygons-simple.txt")"""
    print(format_str("The name is $1 -- $0 $1", ["James", "Bond"]))
    

if __name__ == "__main__":
    main()
