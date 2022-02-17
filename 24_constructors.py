# add constructor to the point class
class Point:
    # self is referencing this object. alternate of "this" from C++
    def __init__(self, x=1, y=2):  # constructor
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)
point2 = Point()
print(point1.x)
point2.draw()
