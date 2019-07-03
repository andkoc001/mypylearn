# Andrzej Kocielski, 2019-07-03
# This program resolves quadratic equotion ax^2+bx+c=0.
# Inspired by Socratica at https://youtu.be/g8nQ90Hk328.
###


# Import of required modules

import math  # this module includes square root method


# Definition of the method resolving the quadratic equation problem for a, b and c parameters.

def quadratic(a, b, c):
    """For passed parameters a, b and c of the quadratic equation, returns the roots."""
    # Compute the discriminant (b^2-4ac)
    disc = b**2 - 4*a*c

    # Compute the roots depending on the discriminant
    if disc > 0:
        root1 = (-b - math.sqrt(disc)) / (2*a)
        root2 = (-b + math.sqrt(disc)) / (2*a)
        # return as a tuple
        return print("The equation has two real roots: ", (root1, root2))
    elif disc == 0:
        root = -b / 2*a
        return print("The equation has a single real root: ", root)
    else:
        return print("The equation has no real root.")


# Main body of the program
# For simlicity and for testing, the a, b and c values are explicitely given.
quadratic(1.0, 0.0, -4.0)
