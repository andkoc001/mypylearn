# Andrzej Kocielski, 2019-07-10
# SPOJ.com solution to problem Two Circles, https://www.spoj.com/problems/SMPCIRC/
###

# Import of required modules
import math  # this module includes square root method
import time  # for duration of calculation


def user_input():
    """Asks user to input the required data."""
    # Boundary contirions reminder
    print("0 ≤ xo, yo  ≤ 10000 and 0 < r ≤ 10000 \n")
    # Coords of centre and radious of 1st circle
    print("Enter xo1, yo1 and r1 for the 1st circle respectively: ")
    xo1 = float(input())
    yo1 = float(input())
    r1 = float(input())
    # Coords and radius of 2nd circle
    print("Enter xo2, yo2 and r2 for the 2nd circle respectively: ")
    xo2 = float(input())
    yo2 = float(input())
    r2 = float(input())

    # Boundary conditions check
    # c1 = boundary_check(xo1, yo1, r1)
    # c2 = boundary_check(xo2, yo2, r2)
    if (boundary_check(xo1, yo1, r1) and boundary_check(xo2, yo2, r2)) == True:
        return xo1, yo1, r1, xo2, yo2, r2
    else:
        return print("Some entered data is out of range. \n")


def boundary_check(xo, yo, r):
    """Checks if the boundary conditions are satisfied."""
    if (xo >= 0 and xo <= 10000) and (yo >= 0 and yo <= 10000) and (r > 0 and r <= 10000):
        return True


def solution(xo1, yo1, r1, xo2, yo2, r2, i):
    """Checks position of the circles."""

    # Distance between centres of two circles
    dist = math.sqrt((abs(xo1-xo2))**2 + (abs(yo1-yo2))**2)
    print(dist)

    print("*"*5, i+1, "solution:", "*"*5)
    # Solution conditions
    if ((dist+r1) == r2) or ((dist+r2) == r1):
        print("E - internally tangible.")
    elif ((dist+r1) < r2) or ((dist+r2) < r1):
        print("I - one inside the other.")
    else:
        print("O - other scenario.")


def main():
    """Program checks relative position of the two circles."""

    # Number of test cases - entered by user, t<=1000
    print("="*5)
    cases = int(input("Number of test cases (max 1000 tests): "))
    if 0 < cases < 1000:
        for i in range(cases):
            print("-"*5)
            print(i+1, "pair of circles: ")
            xo1, yo1, r1, xo2, yo2, r2 = user_input()
            print("Data of the", i+1, "set of circles: ",
                  xo1, yo1, r1, xo2, yo2, r2)
            solution(xo1, yo1, r1, xo2, yo2, r2, i)
            print("|"*22)
    else:
        print("Too many cases!")


main()
