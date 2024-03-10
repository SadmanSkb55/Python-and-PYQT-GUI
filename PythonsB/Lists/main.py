names=['Alex','Summit','McGregore','george']
print(names)
print(names[2])
print(names[-1])
print(names[3].upper())
print(names[2:])
print(names[:2])
print(names[:2].reverse())
names[2]='Ryukendo'
print(names[:])

nums=[3,4,8,1,0.2,5,9,5.01,9.000000001]
max=nums[0]
min=nums[0]
for n in nums:
    if n>max:
        max=n
    elif n<min:
        min=n
print(min)
print(max)
#2D

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
matrix[2][2]=10
for row in matrix:
    for item in row:
        print(item)
