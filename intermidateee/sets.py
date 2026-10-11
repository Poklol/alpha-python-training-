# sets for unordered, mutable, no duplicate elements

#Initialization and duplicates removal
my_set = {1, 2, 3, 1, 2}
print("Set eliminates duplicates:", my_set)  # {1, 2, 3}

# converting iterables (lists, strings) to sets
set_from_list = set([1, 2, 3, 3, 4])
set_from_string = set("Hello")  # Arbitrary order, single 'l'
print("From string:", set_from_string)

# reating an empty set (must use set(), as {} creates an empty dict)
empty_set = set()
print(type(empty_set))

# modifying sets (adding and removing)
my_set.add(4)
my_set.add(5)

my_set.remove(3)    # removes element; raises KeyError if not found
my_set.discard(10)  # removes element; does NOT raise error if missing
popped_elem = my_set.pop()  # removes and returns an arbitrary element
print("After modifications:", my_set)
# my_set.clear()    # empties the set

#  iteration and membership
for item in my_set:
    print(item)

if 2 in my_set:
    print("2 is present in the set")

# mathematical Set Operations (Union, Intersection, Difference)
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# union: combines elements from both without duplication
u = odds.union(evens)
print("Union:", u)

# intersection for Elements present in both sets
i_odd_primes = odds.intersection(primes)
print("Odd primes:", i_odd_primes)
i_even_primes = evens.intersection(primes)
print("Even primes:", i_even_primes)  # {2}

# difference: elements in first set but not in second
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_b = {1, 2, 3, 10, 11, 12}
diff = set_a.difference(set_b)
print("Difference (A - B):", diff)  # {4, 5, 6, 7, 8, 9}

# symmetric difference: elements in A or B, but NOT in both
sym_diff = set_a.symmetric_difference(set_b)
print("Symmetric difference:", sym_diff)

#  in place Update Methods (Modifies the original set)
set_a.update(set_b)                     # Adds elements from B
set_a.intersection_update(set_b)        # Keeps only shared elements
set_a.difference_update(set_b)          # Removes elements found in B
set_a.symmetric_difference_update(set_b)# Keeps elements in either, not both

#  Set Comparisons (Subset, Superset, Disjoint)
group_a = {1, 2, 3, 4, 5, 6}
group_b = {1, 2, 3}
group_c = {7, 8}

print("group_b is subset of group_a:", group_b.issubset(group_a))        # True
print("group_a is superset of group_b:", group_a.issuperset(group_b))    # True
print("group_a is disjoint with group_c:", group_a.isdisjoint(group_c))  # True (no shared elements)

#  Copying sets
set_org = {1, 2, 3}
set_cpy = set_org.copy()  # Or set(set_org)
set_cpy.add(4)
print("Original set unaffected:", set_org)

#Frozenset (Immutable version of a set)
f_set = frozenset([1, 2, 3, 4])
print("Frozenset:", f_set)
# f_set.add(5)    # AttributeError: 'frozenset' object has no attribute 'add'
# f_set.remove(1) # AttributeError: cannot remove elements
