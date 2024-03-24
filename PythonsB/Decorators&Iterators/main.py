def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")

say_hello()

import time
from functools import wraps

def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join(f"{key}={value}" for key, value in kwargs.items())
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        print(f"Function '{func.__name__}' with args [{all_args}] executed in {execution_time:.6f} seconds. Returned: {result}")
        return result
    return wrapper

@log_time
def example_function(x, y):
    time.sleep(1)
    return x + y

result = example_function(3, 4)
print("Result:", result)

#iterators
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

my_list = [1, 2, 3, 4, 5]
my_iter = MyIterator(my_list)
for num in my_iter:
    print(num)

class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

# Usage
fib_iter = FibonacciIterator(1000)
for num in fib_iter:
    print(num, end=" ")
