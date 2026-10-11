# lambda functions: small anonymous functions 
from functools import reduce

# basic lambda syntax vs standard function
add10 = lambda x: x + 10
print("add10(5):", add10(5))  # Output: 15

# equivalent standard function:
# def add10_func(x):
#     return x + 10

mult = lambda x, y: x * y
print("mult(2, 7):", mult(2, 7))  # Output: 14

# custom sorting using lambda as the key
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

# default sort sorts by first element (x-coordinate)
points2D_sorted = sorted(points2D)
print("Sorted by X:", points2D_sorted)

# sort by second element (y-coordinate) using lambda
points2D_sorted_y = sorted(points2D, key=lambda point: point[1])
print("Sorted by Y:", points2D_sorted_y)

# sort by sum of coordinates
points2D_sorted_sum = sorted(points2D, key=lambda point: point[0] + point[1])
print("Sorted by sum:", points2D_sorted_sum)

#  map(func, iterable): transforms each element
nums = [1, 2, 3, 4, 5]

# using map with lambda
mapped_nums = map(lambda x: x * 2, nums)
print("Mapped (doubled):", list(mapped_nums))

# equivalent list comprehension (often preferred in modern Python):
comp_mapped = [x * 2 for x in nums]
print("List comprehension doubled:", comp_mapped)

# filter(func, iterable) for  returns items where func evaluates to True
nums_filter = [1, 2, 3, 4, 5, 6]

# filter even numbers
filtered_evens = filter(lambda x: x % 2 == 0, nums_filter)
print("Filtered evens:", list(filtered_evens))

# equivalent list comprehension with condition:
comp_filtered = [x for x in nums_filter if x % 2 == 0]
print("List comprehension evens:", comp_filtered)

# reduce(func, iterable) for  repeatedly applies func to reduce sequence to a single value
# func must take two arguments: (accumulator, current_value)
nums_reduce = [1, 2, 3, 4]
product_all = reduce(lambda x, y: x * y, nums_reduce)
print("Product of all numbers:", product_all)  # 1 * 2 * 3 * 4 = 24
