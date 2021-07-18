# Based on code from https://youtu.be/TYBqsjc04aM

import turtle

# The algorithm


def side(l):
    # calculate the length of side wall of a square of diagonal length l
    return (l**2/2)**0.5


def dragon(l, n, turn="right"):

    # define recursion stop condition
    if n == 0:
        turtle.forward(l)
        return

    if turn == "right":
        turtle.right(45)
    else:  # turn == "left"
        turtle.left(45)

    # recurcsive call
    dragon(side(l), n - 1, turn="right")

    if turn == "right":
        turtle.left(90)
    else:  # turn == "left"
        turtle.right(90)
        # turtle.update()  # for seeing drawing progress

    # recurcsive call
    dragon(side(l), n - 1, turn="left")

    if turn == "right":
        turtle.right(45)
    else:  # turn == "left"
        turtle.left(45)


###
# drawing settings
screen = turtle.Screen()
turtle.tracer(0, 0)
turtle.hideturtle()
screen.tracer(False)

# number of iterations
num_iter = 10
# size of drawing - dependent on the number of iterations
size = num_iter * 40

# main program function
dragon(size, num_iter)
turtle.update()

# keep result on screen until clicked
turtle.Screen().exitonclick()
