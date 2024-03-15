import Converter
from Converter import lbstokgs

import Ecommerce.Shipping
Ecommerce.Shipping.CalcShipping()
from Ecommerce.Shipping import Cart
Cart()
from Ecommerce import Shipping
Shipping.Items()

import random

print(Converter.kgstolbs(100))
print(lbstokgs(233 ))

number=[1,56,77,34,45,32,11,67,0.056]
sorterx=Converter.sorter()
print(sorterx.findmin(number))
print(max(number))

pointX=[3,4]
pointY=[5,6]
Dist=Converter.distance(pointX,pointY)
print(Dist.dist())

for i in range(5):
    print(random.random())
    print(random.randint(1,100))
    print(random.randrange(1,100))
    print(random.randbytes(1))


members=['Alex','Drake','Abel','Jordan']
leader=random.choice(members)
print(leader)
print(members[random.randint(0,3)]) 