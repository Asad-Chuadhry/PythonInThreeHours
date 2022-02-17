#First Letter of Class name always capital
# pascal naming convention or camel convention EmailClient
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.draw()
point1.x = 10
point1.a = 20
print(point1.a)

point2 = Point()
point2.asad = 20
point2.xyz = "testing"
print(point2.xyz)