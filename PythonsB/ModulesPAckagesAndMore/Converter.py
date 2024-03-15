import math
def lbstokgs(weight):
    return weight*0.45
def kgstolbs(weight):
    return weight/0.45

class sorter:
    def findmax(self,number):
        max=number[0]
        for n in number:
            if n>max:
                max=n
        return max

    def findmin(self, number):
        min = number[0]
        for n in number:
            if n < min:
                min = n
        return min
class subs:
    def minus(self, A, B):
        return A - B

class distance(subs):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self):
        A = self.minus(self.x[0], self.x[1])
        B = self.minus(self.y[0], self.y[1])
        return math.sqrt((A * A) + (B * B))
