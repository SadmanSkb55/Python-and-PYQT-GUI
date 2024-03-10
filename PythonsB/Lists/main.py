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
#list methods

nums2=[2,4,6,7,9,12]
nums2.append(39)
print(nums2)
nums2.insert(2,55)
print(nums2)
nums2.remove(39)
print(nums2)
matrix.clear()
print(matrix)
nums2.pop()
print(nums2)
print(nums2.index(9))
#print(nums2.index(99))
nums2.append(9)
print(nums2.count(9))
nums2.sort()
print(nums2)
nums2.reverse()
print(nums2)
nums3=nums2.copy()
nums3.append(66)
print(nums3)
nsx=[3,6,8,0,6,3,6,4,7,1,0,8,5,3,6,2,7,1,7,8,9,5]
uniques=[]
for i in nsx:
    if i not in uniques:
        uniques.append(i)
print(uniques)