# Spoj.com problem #2 - Pola - zraszacze
# https://pl.spoj.com/problems/POLA/
# Andkoc001, 19-06-2020

# Short description: as an input 6 numbers are given: centre and radius of two circles.
# As an output provide the difference between the two areas that do not overlap.

#####

import math

###


def read_data(tests):

    print("For each test enter the following: x1, y1, r1, x2, y2, r2")
    print(tests)

    for t in range(tests):

        # create an empty list
        t = []

        # read data from keyboard [x1, y1, r1, x2, y2, r2]
        max_length = 6
        while len(t) < max_length:
            item = int(input())
            t.append(item)
        print(t)
        print()

        # distance between centres of circles: sqrt((x2 - x1)**2 + (y2 - y1)**2)
        dist = math.sqrt((t[3] - t[0])**2 + (t[4] - t[1])**2)
        print(dist)

        # case no.1 - no overlap (r1+r2 < dist)
        if t[2] + t[5] < dist:
            print("case 1 - no overlap")

        # case no.2 - one circle entirely inside another one
        # circle 2 inside circle 1
        elif (t[2] > t[5]) and (dist + t[5] < t[2]):
            print("case 2 - c2 inside c1")

        # circle 1 inside circle 2
        elif (t[2] < t[5]) and (dist + t[2] < t[5]):
            print("case 2 - c1 inside c2")

        # case no.3 - partial overlap
        else:
            print("case 3 - partial overlap")


###


def main():
    # Number of tests (for time being assumed, but later it will be a random number < 1001):
    t = int(input("How many tests (< 1001): "))
    read_data(t)


if __name__ == "__main__":
    # execute only if run as a script
    main()
