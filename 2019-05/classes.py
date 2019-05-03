# Andrzej Kocielski, 03-05-2019
# Classes
# ===


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


r1 = Rectangle(1, 3, 5, 6)
r1 = Rectangle(3, 2, 7, 4)

print(r1.x1, r1.y1, r1.x2, r1.y2)
