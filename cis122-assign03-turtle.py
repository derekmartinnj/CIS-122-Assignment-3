'''
Author: Derek Martin
Credit: CIS 122
Description: Create functions that draw lines using Turtle graphics
References: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle as t

# Question 3
def draw_line(t, x, y, angle, length):
    '''
    Draws a line given specific input

    Uses given degrees, length, and starting location to draw a line

    Args:
        t (turtle): argument representing the Turtle
        x (int): starting x location
        y (int): starting y location
        angle (int): starting angle of the line
        length (int): length of the line

    Returns:
        None
    '''
    def move(t, x, y):
        '''
        Moves the starting location to a given spot

        Uses coordinates to move to a specific location. The pen ends in the up position, at the location of the end of the line.

        Args:
            t (turtle): argument representing the Turtle
            x (int): starting x location
            y (int): starting y location

        Returns:
            None
        '''
        t.pu()
        t.setx(int(x))
        t.sety(int(y))
        t.seth(int(angle))
        t.pd()

    move(t, x, y)
    t.fd(int(length))
    t.pu()

# Test
# draw_line(t, 100, 100, 0, 200)
# draw_line(t, -100, -100, 270, 50)
# draw_line(t, 200, -200, 45, 75)

def draw_radial_lines(t, x, y, length, num_lines):
    '''
    Draw radial lines given specific input

    Draw radial lines with a specific center location, length, and amount of lines.

    Args:
        t (turtle): A variable representing the Turtle
        x (int): x location of starting point
        y (int): y location of starting point
        length (int/float): the length of each line
        num_lines (int): the number of radial lines to draw

    Returns: None
    '''
    radial_gap = 360 / num_lines
    for i in range(num_lines):
        t.pu()
        t.goto(int(x), int(y))
        t.rt(radial_gap)
        t.pd()
        t.fd(length)

# Test
# draw_radial_lines(t, -100, -100, 25, 8)
# draw_radial_lines(t, -100, 100, 100, 4)
# draw_radial_lines(t, 100, -100, 200, 16)
# draw_radial_lines(t, 100, 100, 50, 32)

def draw_radials_in_quadrants(t, length, num_lines):
    '''
    Draw radiants in quadrants

    Draw the same radial in 4 different quadrants using different distance values for each quadrant

    Args:
        t (turtle): A variable that represents the Turtle
        lenght (int): the length of the lines
        num_lines (int): the number of radial lines to draw in each quadrant

    Returns:
        None
    '''
    
    t.seth(0)
    angle = 90 / int(num_lines)
    for j in range(4):
        for i in range(num_lines):
            t.goto(0,0)
            t.fd(length)
            t.lt(angle)
        length = int(length) * 2
    

# Test
# draw_radials_in_quadrants(t, 100, 8)
# draw_radials_in_quadrants(t, 50, 16)
