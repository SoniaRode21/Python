__author__ = 'SONIYA RODE'
__author__ = 'TEJAS ARYA'

"""

Author: SONIYA RODE
Author: TEJAS ARYA

This is a  program that draws polygons of decreasing sizes, recursively.
"""

import sys
import turtle
import random

# global constants for window dimensions
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000


def init():
    """
    Initialize for drawing.  (-500, -500) is in the lower left and
    (500, 500) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """

    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    turtle.up()
    turtle.setheading(0)
    turtle.setpos(650, 450)
    turtle.title('Polygons')
    turtle.write("TEJAS ARYA")

    turtle.setpos(650, 430)
    turtle.write("SONIYA  RODE")

    turtle.tracer(0, 0)

    COLORS = 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'violet'
    # pen sizes to use for filled and unfilled polygons
    FILL_PEN_WIDTH = 2
    UNFILL_PEN_WIDTH = 81.5
    turtle.setpos(0, 0)
    turtle.up()


def checkInt(noOFsides):
    '''
    Function checks if the command line input for no of sides is an integer.
    Returns true if an integer.
    :param noOFsides: No of sides for the polygon
    :return: Boolean
    '''
    try:
        int(noOFsides)
        return True
    except ValueError:
        return False


'''
Function helps in drawing the polygon design

:pre: pos (0,0), heading (east), up
:post: pos (0,0), relative, down
:param depth : no of triangles to draw
:param length : length of the triangle
:param col : Color of pen
:return: None
'''

def triangle(depth,length,col) :
    turtle.pencolor(col)

    if depth==0 :
        pass
    else :

        for i in range(0,3) :

            turtle.forward(length)
            triangle(depth - 1, length / 2,col)
            turtle.left(120)


def polygon(sides, length, fillState):
    """
    Draws polygons recursively with decreasing no of sides.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), relative, down
    :param sides :number of sides
    :param length : Length of each side of polygon
    :param fillState : Fill or unfill the polygon
    :return: length traced
    """

    turtle.pendown()
    sum = 0;
    COLORS = 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'magenta', 'magenta', 'pink'
    # Check whether number of sides is >= 3
    if sides == 2:
        return 0

    for i in range(0, 6):
        turtle.pencolor(COLORS[i])

        # Draws with fill
        if fillState == "fill":
            turtle.pensize(2)
            turtle.begin_fill()
            for i in range(0, sides):
                turtle.forward(length)
                turtle.left(360 / sides)
                sum += length
                triangle(3, 40,COLORS[i])

            turtle.end_fill()

        # Draws without fill
        else:
            turtle.pensize(8)
            for i in range(0, sides):
                turtle.forward(length)
                turtle.left(360 / sides)
                sum += length
                triangle(3,40,COLORS[i])

        turtle.left(60)
    polygon(sides - 1, length / 2, fillState)
    turtle.up()
    return sum


def main():
    # Check if correct no of arguments is recieved
    if len(sys.argv) not in range(2, 4):
        print("Incorrect no of command line arguments ")
        sys.exit(" $ python3 polygons.py #_sides [fill|unfill]")

    # Commandline input for the no of sides
    noOfSides = sys.argv[1]
    fillOrUnfill = "null"

    # If fill or unfill is mentioned set equal to argument received
    if len(sys.argv) == 3:
        fillOrUnfill = (sys.argv[2])

    # if fill is mentioned, else default is set to unfill
    if fillOrUnfill == "fill" or fillOrUnfill == "Fill":
        fillOrUnfill = "fill"
    else:
        fillOrUnfill = "unfill"

    # Check whether input for number of sides can be converted to integer else exit
    if not checkInt(noOfSides):
        sys.exit("The number of sides must be integers. Exit.")

    # Convert noofSides string command line ip to int
    noOfSides = int(noOfSides)

    # Check whether no of sides is between 3 and 8 inclusive
    if noOfSides not in range(3, 9):
        sys.exit("The number of sides must be between 3 and, inclusive. Exit.")
    init()

    ans = polygon(noOfSides, 200, fillOrUnfill)
    print("The total length drawn :", ans)
    turtle.mainloop()


if __name__ == "__main__":
    main()