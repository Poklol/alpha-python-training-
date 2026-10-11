# itertools: product, permutations, combinations, accumulate, groupby, infinite iterators
from itertools import (
    product,
    permutations,
    combinations,
    combinations_with_replacement,
    accumulate,
    groupby,
    count,
    cycle,
    repeat,
)
import operator

#product (cartesian product of input iterables)
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print("product:", list(prod))  # [(1, 3), (1, 4), (2, 3), (2, 4)]

# repeat argument for Cartesian product with itself
prod_repeat = product(a, b, repeat=1)

# permutations (all possible orderings of elements)
a_perm = [1, 2, 3]
perm = permutations(a_perm)
print("permutations:", list(perm))

# specify length of permutations
perm_len2 = permutations(a_perm, 2)
print("Permutations (len 2):", list(perm_len2))

# combinations (all unique combinations of a specific length)
a_comb = [1, 2, 3, 4]
comb = combinations(a_comb, 2)
print("Combinations (len 2):", list(comb))

# combinations with replacement (allows picking the same element)
comb_wr = combinations_with_replacement(a_comb, 2)
print("Combinations with replacement:", list(comb_wr))

# accumulate (returns cumulative sums or cumulative results of binary functions)
a_acc = [1, 2, 3, 4]
acc_sum = accumulate(a_acc)
print("Accumulated sum:", list(acc_sum))  # [1, 3, 6, 10]

# using a custom binary function 
acc_mul = accumulate(a_acc, func=operator.mul)
print("Accumulated multiplication:", list(acc_mul))  # [1, 2, 6, 24]

# Tracking cumulative max
a_max = [1, 2, 5, 3, 4]
acc_max = accumulate(a_max, func=max)
print("Accumulated max:", list(acc_max))

# groupby (makes an iterator returning keys and groups from an iterable)
def smaller_than_3(x):
    return x < 3

a_group = [1, 2, 3, 4]
group_obj = groupby(a_group, key=smaller_than_3)
for key, value in group_obj:
    print("Group key:", key, "Values:", list(value))

#  grouping dictionaries by shared attribute using lambda
persons = [
    {"name": "Tim", "age": 25},
    {"name": "Dan", "age": 25},
    {"name": "Lisa", "age": 27},
    {"name": "Claire", "age": 28},
]
group_persons = groupby(persons, key=lambda x: x["age"])
for key, value in group_persons:
    print(f"Age {key}:", list(value))

#  Infinite Iterators (count, cycle, repeat)
# count(start, step): counts indefinitely from start
for i in count(10):
    print("Count:", i)
    if i == 15:
        break

# cycle(iterable): cycles infinitely through an iterable
cycle_count = 0
for i in cycle([1, 2, 3]):
    print("Cycle:", i)
    cycle_count += 1
    if cycle_count == 6:
        break

# repeat(elem, n): repeats an element n times
for i in repeat(1, 4):
    print("Repeat:", i)
