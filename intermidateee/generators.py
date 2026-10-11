# generators: functions that return an iterator and generate values lazily using 'yield'
import sys

# Basic generator function
def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()
print("Generator object:", g)

# retrieving values one at a time with next()
print(next(g))  # Output: 1 (pauses execution at first yield)
print(next(g))  # Output: 2 (resumes and pauses at second yield)
print(next(g))  # Output: 3

# Calling next() again when no yields remain raises StopIteration:
# print(next(g))  # Raises StopIteration

# Using generators with built-in functions
g2 = my_generator()
print("Sum of generator:", sum(g2))  # Computes 1 + 2 + 3 = 6

#  execution flow: Countdown generator
def countdown(num):
    print("Starting countdown...")
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)
for val in cd:
    print("Countdown tick:", val)

# practical Example: Fibonacci Sequence Generator
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
print("Fibonacci sequence:", list(fib))

# Memory Efficiency: Generator vs. List
# Case A: Generating sequence via normal list (stores all numbers in RAM)
def first_n(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

# Generating sequence lazily via generator (generates on-the-fly)
def first_n_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print("Sum via list:", sum(first_n(10)))
print("Sum via generator:", sum(first_n_generator(10)))

#Generator Expressions vs. List Comprehensions
# Generator expressions use () instead of []
gen_exp = (i for i in range(100000) if i % 2 == 0)
list_comp = [i for i in range(100000) if i % 2 == 0]

# Inspecting memory footprint with sys.getsizeof()
print("Memory size of Generator Expression:", sys.getsizeof(gen_exp), "bytes")
print("Memory size of List Comprehension:", sys.getsizeof(list_comp), "bytes")