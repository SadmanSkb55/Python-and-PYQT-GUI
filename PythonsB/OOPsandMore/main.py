#constructor and method overloading concept,actually dont exists here
class mather:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    @classmethod
    def from_list(cls,lst):
        return cls(*lst)#using class methods as alternative constructors

    def adder(self,x=0,y=0):
       if self.x>0 or self.y>0:
           return self.x + self.y
       else:
           return x+y
    def subber(self,x=0,y=0):
        if self.x > 0 or self.y > 0:
            return self.x - self.y
        else:
          return x-y
    def multi(self,x=0,y=0):
        if self.x > 0 or self.y > 0:
            return self.x*self.y
        else:
            return x*y
    def diver(self,x=0,y=0):
        try:
            if self.x > 0 or self.y > 0:
                return self.x/self.y
            else:
                return x/y
        except Exception as e:
            print('Cant divide with 0',e)


math1=mather(5,9)
print(math1.adder())
print(math1.subber())
print(math1.diver())
print(math1.multi())
print(math1.x,math1.y)
print("\n")

math1o2=mather(7)
print(math1o2.adder())
print(math1o2.subber())
print(math1o2.diver())
print(math1o2.multi())
print("\n")

math2=mather()
print(math2.adder(9,67))
print(math2.subber(9,54))
print(math2.diver(8,8))
print(math2.multi(9,0))
print("\n")
print(math2.adder(78))
print(math2.subber(678))
print(math2.diver(78))
print(math2.multi(456))
print("\n")

math3=mather(2,3)
print(math3.x,math3.y)

math4=mather.from_list([2,5])
print(math4.adder())
print(math4.subber())
print(math4.diver())
print(math4.multi())


#method overriding
class mathEng(mather):
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def multiplier_Eng(self):
        return self.x*self.y

class sqare(mathEng):
    def __init__(self,x):
        self.x=x
    def multiplier_Eng(self,x=0):
        return self.x*self.x

class cube(mathEng):
    def __init__(self,y):
        self.y=y
    def multiplier_Eng(self,y=0):
        return self.y*self.y*self.y


sq=sqare(5)
print(sq.multiplier_Eng())
cb=cube(8)
print(cb.multiplier_Eng())
print("\n")
#encapsulation
class Car:
    def __init__(self, make, model):
        self._make = make  # protected
        self.__model = model  # private

    def get_make(self):
        return self._make
    def set_model(self, model):
        self.__model = model
    def get_model(self):
        return self.__model

car = Car("Toyota", "gt86")
print(car.get_make())
print(car.get_model())
car.set_model("Corolla")
print(car.get_model())
print("\n")


#generics/template

#duck typing........(Liton Typing)
class Player:
    def __init__(self, Run):
        self.Run = Run
    #Type Hints
    def repeat(self,item: str, times: int) -> str:#gibving the type as hint
        return item * times

liton=Player(0)
print(f'Liton took {liton.Run} Runs')
liton=Player("Liton out at 0 balls")
print(liton.Run)
print(liton.repeat("Liton Liton Duck Pari\n",3))

#Generic(py3.9+)


from typing import TypeVar, Generic

T = TypeVar('T')
class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value
    def adder(self):
        return self.value+self.value

con1 = Container(23456789.987654)
print("Type of con1", type(con1.value))
print(con1.value)
print(con1.adder())
print('\n')
con2 = Container("Amar code Davin maire dibe ")
print("Type of con2", type(con2.value))
print(con2.value)
print(con2.adder())

#ABC(Abstract Base Classes)


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
print()
rectangle = Rectangle(5, 4)
print(rectangle.area())
print(rectangle.perimeter())
print()

circle = Circle(3)
print(circle.area())
print(circle.perimeter())






