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
print()
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen))
print()
# Generator Function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Generator Expression
squares = (x ** 2 for x in range(5))

# Using the Generator Function
for num in countdown(3):
    print(num)

# Using the Generator Expression
for num in squares:
    print(num)
print()
#Expressions :::::

# Arithmetic Expression
result_arithmetic = 10 + 5 * 3 - (7 / 2)

# Boolean Expression
x = 10
y = 20
result_boolean = x > 5 and y < 30

# Comparison Expression
a = 15
b = 20
result_comparison = a == b

# Membership Expression
my_list = [1, 2, 3, 4, 5]
result_membership = 3 in my_list

# Identity Expression
obj1 = [1, 2, 3]
obj2 = [1, 2, 3]
result_identity = obj1 is obj2

# Function Call Expression
result_function_call = len("Hello, world!")

# Attribute Access Expression
import math
result_attribute_access = math.pi

# List Comprehension
original_list = [1, 2, 3, 4, 5]
result_list_comprehension = [x ** 2 for x in original_list]

# Conditional Expression (Ternary Operator)
num = 15
result_conditional = "Even" if num % 2 == 0 else "Odd"

# Parenthesized Expression
result_parenthesized = (10 + 5) * 2

print("Arithmetic Expression:", result_arithmetic)
print("Boolean Expression:", result_boolean)
print("Comparison Expression:", result_comparison)
print("Membership Expression:", result_membership)
print("Identity Expression:", result_identity)
print("Function Call Expression:", result_function_call)
print("Attribute Access Expression:", result_attribute_access)
print("List Comprehension:", result_list_comprehension)
print("Conditional Expression:", result_conditional)
print("Parenthesized Expression:", result_parenthesized)
print()
# Advanced Expression Example: Filtering and Transformation
# Original List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Advanced Expression: Filtering even numbers and transforming them
even_squared = [x**2 for x in numbers if x % 2 == 0]

print("Original Numbers:", numbers)
print("Even Squared:", even_squared)








