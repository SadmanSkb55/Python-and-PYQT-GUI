#constructor and method overloading concept,actually dont exists here
class mather:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
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

#




