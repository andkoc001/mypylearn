# Spoj.com problem #2 - Pola - zraszacze
# https://pl.spoj.com/problems/POLA/
# Andkoc001, 19-06-2020

# Short description: as an input 6 numbers are given: centre and radius of two circles.
# As an output provide the difference between the two areas that do not overlap.

#####

import math

###


def read_data(tests):

    for i in range(tests):
        # create an empty list
        t = []

        print()
        print("Test no.:", i+1)
        print("Enter the following: x1, y1, r1, x2, y2, r2")

        # read data from keyboard [x1, y1, r1, x2, y2, r2]
        max_length = 6
        while len(t) < max_length:
            item = int(input())
            t.append(item)
        print()

        # distance between centres of circles: sqrt((x2 - x1)**2 + (y2 - y1)**2)
        dist = math.sqrt((t[3] - t[0])**2 + (t[4] - t[1])**2)
        print(f"Distance between centres: {dist: .2f}")

        # area of circle 1
        s1 = math.pi*t[2]**2
        print(f"Circle 1 area: {s1: .2f}")

        # area of circle 2
        s2 = math.pi*t[5]**2
        print(f"Circle 2 area: {s2: .2f}")

        print()

        # case no.1 - no overlap (r1+r2 < dist)
        if t[2] + t[5] < dist:
            print("Case 1 - no overlap")

        # case no.2 - one circle entirely inside another one
        # circle 2 inside circle 1
        elif (t[2] > t[5]) and (dist + t[5] < t[2]):
            print("Case 2a - circle C2 inside C1")

        # circle 1 inside circle 2
        elif (t[2] < t[5]) and (dist + t[2] < t[5]):
            print("Case 2b - circle C1 inside C2")

        # case no.3 - partial overlap
        # division by zero protection yet to be implemented
        else:
            print("Case 3 - partial overlap")
            # common area of both circles
            intersecting_area = abs(t[2]**2 * math.cos((2*dist*t[2])/(dist**2 + t[2]**2 - t[5]**2))) + (t[5]**2 * math.cos((2*dist*t[5]) /
                                                                                                                           (dist**2 + t[5]**2 - t[2]**2))) - (0.5 * math.sqrt((-dist+t[2]+t[5])*(dist+t[2]-t[5])*(dist-t[2]+t[5])*(dist+t[2]+t[5])))

            result = abs((s1-intersecting_area)-(s2-intersecting_area))

            print(f"Result: {result: .2f}")

        print(7*"-")


###


def main():
    # Number of tests (for time being assumed, but later it will be a random number < 1001):
    t = int(input("How many tests (< 1001): "))
    read_data(t)


if __name__ == "__main__":
    # execute only if run as a script
    main()
