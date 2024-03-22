#Comprehensions

#List
squares = [x**2 for x in range(10)]
print(f'Sqaures w List : {squares}')

cubes = [x**3 for x in range(10)]
print(f'Cubes w List : {cubes}')
print()
#Dictionary
square_dict = {x: x**2 for x in range(10)}
print(f'Sqaures w Dictionary : {square_dict}')

cube_dict = {x: x**3 for x in range(10)}
print(f'Cubes w Dictionary : {cube_dict}')
print()

#Set
square_set = {x**2 for x in range(10)}
print(f'Sqaure w Set : {square_set}')
cube_set = {x**3 for x in range(10)}
print(f'Cube w Set : {cube_set}')
print()

# Create a tuple of squares
square_tuple = tuple(x**2 for x in range(10))
print(f'Squares w Tuple: {square_tuple}')
cube_tuple = tuple(x**3 for x in range(10))
print(f'Cubes w Tuple: {cube_tuple}')
print()

# Set comprehension for squares as tuples
square_set_tuples = {(x, x**2) for x in range(10)}
print(f'Squares w Set of Tuples: {square_set_tuples}')
cube_set_tuples = {(x, x**3) for x in range(10)}
print(f'Cubes w Set of Tuples: {cube_set_tuples}')
print()

#Tuple comprehension for tuples of squares
square_tuples = tuple((x, x**2) for x in range(10))
print(f'Squares w Tuple of Tuples: {square_tuples}')
cube_tuples = tuple((x, x**3) for x in range(10))
print(f'Cubes w Tuple of Tuples: {cube_tuples}')
print()

# Generator function
def square_numbers(n):
    for i in range(n):
        yield i ** 2

# Generator expression
squares = (i ** 2 for i in range(10))

# Using generator function
for num in square_numbers(5):
    print(num)

# Using generator expression
for num in squares:
    print(num)









