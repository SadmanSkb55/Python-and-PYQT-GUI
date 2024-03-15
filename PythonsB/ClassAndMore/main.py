import math
class point:
    def move(self):
        print("Move!!!")
    def draw(self):
        print("Draw")
class pointx(point):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    pass

    def distance(self):
        print(f'Value of x:{self.x} and y:{self.y} and distance is {abs(self.x-self.y)}')

point1=point()
point1.move()
point1.x=10
point1.y=20
print(point1.x)

point2=point()
point2.x=point1.x+point1.y
point2.y=abs(point1.x-point1.y)
print(f'x:{point2.x} y:{point2.y}')

point3=pointx(10,20)
point3.x=121
print(point3.x)
print(point3.distance())
point3.move()
point3.draw()

class mamal:
    def walk(self):
        print("Walking")

class vertebomammary:
    def isit(self):
        print("Yes")
    pass
class omnivore(mamal,vertebomammary):
    def eatsal(self):
        print("Eats All")

class dog(omnivore):
    pass
class cat(mamal,vertebomammary):
    pass

class rat(mamal,vertebomammary):
    pass

rat1=rat()
rat1.isit()
rat1.walk()
cat1=cat()
cat1.isit()
cat1.walk()
dog1=dog()
dog1.isit()
dog1.walk()
dog1.eatsal()

 


