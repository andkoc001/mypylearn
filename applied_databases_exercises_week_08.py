# Applied Databases, GMIT 2020
# Exercises from week 08 lecture
# Author: Andrzej Kocielski
# ------------------------------


# -----
'''
Exercise 01
Write a Pyton program that has two arrays in the main function:
- one containing several elements which are numbers,
- the other is empty.

Write another function which accepts a number as a parameter
and returns the number doubled.

The main function should call this function for each element of the first array
and populate the second array with the doubled values.

When the second array is full, it should be printed out.
'''

arr_1 = [4, 7, 5, 1, 0]
arr_2 = []


# double_value(arr_1)
# print("Range:", range(len(arr_1)))     # Range: range(0, 5)
# print("Len:", len(arr_1))              # Len: 5
# print("Array:", (arr_1))               # Array: [4, 7, 5, 1, 0]
# print("Array elem.1:", (arr_1[0]))     # Array elem.1: 4


def double_array(array):
    for item in range(len(array)):
        arr_2.append((arr_1[item] * 2))

    return arr_2


def double_number(num):
    num = num * 2
    return num


def main_01(array):
    # print(double_array(arr_1))

    for i in range(len(array)):
        arr_2.append(double_number(array[i]))
    print(arr_2)


# main_01(arr_1)


# -----
'''
Exercise 02
From Q2.py, paste the code below and modifiy it to make it behave as follows.

When run a main menu is shown as follows:
    Menu
    ====
    1 - Fill Array
    2 - Print Array
    3 - Find > in Array
    4 - Exit
    Enter choice:

* If the user chooses 1:

He/She should be prompted to keep entering numbers until -1 is entered.
All numbers up to, but not including -1, should be sored in an array:
    Enter choice: 1
    Enter Number: 9
    Enter Number: 23
    Enter Number: -1

* If the user chooses 2:

The content of the array should be printed.
    Enter choice: 2
    [1, 9, 23]

* If the user chooses 3:

He/She should be prompted to enter a number.
Any number in the array greater than the number entered should be printed:
    Enter choice: 3
    Enter Number: 12
    [23]

* If the user chooses 4:

The program should end.

* If the user enters anything else, the program menu should be displayed again.

The main_02() function should not be changed.
The definition of the functions fill_array() and find_gt_in_array() should not be changed.
The necessary code should be written in the two funtions mentioned above,
so that the program performs as described.

'''


# Main function
def main_02():

    # Initialise array
    array = [4, 4, 25, 6, 1, 78, 0, 51]

    display_menu()

    while True:
        choice = input("Enter choice: ")

        if (choice == "1"):
            array = fill_array()
            display_menu()
        elif (choice == "2"):
            print(array)
            display_menu()
        elif (choice == "3"):
            find_gt_in_array(array)
            display_menu()
        elif (choice == "4"):
            break
        else:
            display_menu()


def fill_array():
    # Write the necessary code to fill the array.
    # -1 should not be part of the array

    # Initialise array
    arr_a = []

    while True:
        next_number = int(input("Enter next number (-1 to end): "))

        if next_number == -1:
            break
        else:
            arr_a.append(next_number)

    return arr_a


def find_gt_in_array(array):
    # Write the necessary code to get a number from the user
    # and print out all numbers in the array that are greater
    # than this number

    gt_number = int(input("Enter cut-off number: "))

    gt_array = []

    for x in array:             # for x in range(len(array))
        if x > gt_number:       # if array[x] > gt_number
            gt_array.append(x)  # gt_array.append(array[x])

    print(gt_array)

    return


def display_menu():
    print("")
    print("MENU")
    print("=" * 4)
    print("1 - Fill Array")
    print("2 - Print Array")
    print("3 - Find > in Array")
    print("4 - Exit")


if __name__ == "__main__":
    # execute only if run as a script
    main_02()


# -----
'''
Exercise 11
Write a Pyton program that takes a name and age in form the console.
If the age is less than 18, the program prints "Too young", 
otherwise the program prints the name followed by "@gmit.ie" 
and the age incremented by 2.
'''


def main_11():

    name = input("Enter your name: ")

    try:
        age = int(input("Enter your age: "))
    except:
        print("Invalid age")

    if age < 18:
        return print("Too young")

    else:
        return print(name + "@gmit.ie, age:", age+2)

    print()


# main_11()
