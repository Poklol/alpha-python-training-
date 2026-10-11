# tuples are like  ordered, immutable, allows duplicate elements
import sys
import timeit

# ccreation and syntax
my_tuple = ("charu", 28, "chennai")
print(my_tuple)

# parentheses are optional but a single element needs a trailing comma
single_item = ("charu",)  # without comma, py treats it as a string
print(type(single_item))

# creating a tuple from an iterable
my_tuple_2 = tuple(["charu", 28, "chennai"])

# accessing elements
item = my_tuple[0]       # 'charu'
last_item = my_tuple[-1] # 'chennai'
print(item, last_item)

# tuples are immutable: assigning items raises a TypeError
# my_tuple[0] = "tim"  # typeError: 'tuple' object does not support item assignment

# iteration and membership
for elem in my_tuple:
    print(elem)

if "charu" in my_tuple:
    print("Yes, charu is in the tuple")

# built-in tuple methods
letters = ('a', 'p', 'p', 'l', 'e')
print("Length:", len(letters))
print("Count of 'p':", letters.count('p'))
print("Index of 'l':", letters.index('l'))

# slicing with tuples: [start:stop:step]
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
sub_tuple = nums[2:5]        # elements at indices 2, 3, 4
step_tuple = nums[::2]       # every second element
reversed_tuple = nums[::-1]  # reversed tuple

# unpacking elements
name, age, city = my_tuple
print(name, age, city)

# unpacking multiple items with asterisk (*) into a list
numbers_tuple = (1, 2, 3, 4, 5)
i1, *i_middle, i_last = numbers_tuple
print("First:", i1)
print("Middle (list):", i_middle)
print("Last:", i_last)

# comparing size and speed (Tuple vs List)
sample_list = [0, 1, 2, "hello", True]
sample_tuple = (0, 1, 2, "hello", True)
print("List memory size:", sys.getsizeof(sample_list), "bytes")
print("Tuple memory size:", sys.getsizeof(sample_tuple), "bytes")

# time efficiency comparison
list_time = timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000)
tuple_time = timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000)
print("Time to create 1M lists:", list_time)
print("Time to create 1M tuples:", tuple_time)
