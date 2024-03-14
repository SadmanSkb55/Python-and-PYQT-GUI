import math
class point:
    def move(self):
        print("Move!!!")
    def draw(self):
        print("Draw")

point1=point()
point1.move()
point1.x=10
point1.y=20
print(point1.x)

point2=point()
point2.x=point1.x+point1.y
point2.y=abs(point1.x-point1.y)
print(f'x:{point2.x} y:{point2.y}') 