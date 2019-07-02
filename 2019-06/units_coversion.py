# Andrzej Kocielski, 2019-07-02
# Application of methods for conversion of units of measurement
# Inspired by www.pasja-informatyki.pl

###

# Definition of methods that converts length from milimeters to imperial units


def inches(m):
    """Returns value passed in mm converted to inches."""
    inch = m/25.4
    return inch


def feet(m):
    """Returns value passed in mm converted to feet."""
    return m/25.4/12


# Main body of the program
mm = float(input("Enter length in milimiters: "))

print("The length converted to inches is ", round(inches(mm), 1))
print("The length converted to feet is ", round(feet(mm), 2))
