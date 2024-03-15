import Converter
from Converter import lbstokgs



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
