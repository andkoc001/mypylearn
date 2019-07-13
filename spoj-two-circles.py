# Andrzej Kocielski, 2019-07-10
# SPOJ.com solution to problem Two Circles, https://www.spoj.com/problems/SMPCIRC/
###

# Import of required modules
import math  # this module includes square root method
import time  # for duration of calculation


def boundary_check(xo, yo, r):


"""Checks if the boundary conditions are satisfied."""
if (xo >= 0 and xo <= 10000) and (yo >= 0 and yo <= 10000) and (r >= 0 and r <= 10000):
    return True


def user_input():


"""Asks user to input the required data."""
  # Boundary contirions reminder
  print("0 ≤ xo, yo,  ≤ 10000 and 0 < r1, r2 ≤ 10000 \n")
   # Coords of centre and radious of 1st circle
   print("Enter xo1, yo1 and r1 for the 1st circle respectively: ")
    xo1 = int(input())
    yo1 = int(input())
    r1 = int(input())
    # Coords and radius of 2nd circle
    print("Enter xo2, yo2 and r2 for the 2nd circle respectively: ")
    xo2 = int(input())
    yo2 = int(input())
    r2 = int(input())

    # Boundary conditions check
    if boundary_check:
        print(xo1, yo1, r1, xo2, yo2, r2)
    else:
        print("Some entries out of range.")


def main():


"""Program checks relative position of the two circles."""

  # Number of test cases - entered by user, t<=1000
  cases = int(input("Number of test cases (max 1000 tests): "))
   if 0 < cases < 1000:
        for i in range(cases):
            user_input()
    else:
        print("Too many cases!")


main()
