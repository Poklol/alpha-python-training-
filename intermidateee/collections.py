# collections module: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

#  counter for stores elements as dictionary keys and their counts as values
a = "aaaaabbbbcccd"
my_counter = Counter(a)
print("Counter object:", my_counter)
print("Keys:", my_counter.keys())
print("Values:", my_counter.values())

# most_common(n): returns the n most common elements as (element, count) tuples
print("Most common (1):", my_counter.most_common(1))
print("Most common element:", my_counter.most_common(1)[0][0])

# elements(): returns an iterator over elements repeating each as many times as counted
print("All elements as list:", list(my_counter.elements()))

# namedtuple: lightweight object type similar to a struct
Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print("Point namedtuple:", pt)
print("Fields:", pt.x, pt.y)

# OrderedDict: remembers the order in which items were inserted
# (Standard dicts in Python 3.7+ remember order as well, but OrderedDict guarantees it)
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print("OrderedDict:", ordered_dict)

# defaultdict: returns a default value if a requested key does not exist yet
d = defaultdict(int)  # default type is int (default value = 0)
d['a'] = 1
d['b'] = 2
print("Existing key 'a':", d['a'])
print("Non-existing key 'c' returns default:", d['c'])  # returns 0 instead of KeyError

# deque: double-ended queue, optimized for O(1) appends and pops from both sides
dq = deque()
dq.append(1)
dq.append(2)
dq.appendleft(3)  # add to the left side
print("Deque after appends:", dq)

dq.pop()          # removes from the right
dq.popleft()      # removes from the left
print("Deque after pops:", dq)

dq.extend([4, 5, 6])       # add multiple to right
dq.extendleft([7, 8])      # add multiple to left
print("Deque after extend:", dq)

dq.rotate(1)      # rotate all elements 1 step to the right
print("Deque rotated +1:", dq)
dq.rotate(-1)     # rotate 1 step to the left
print("Deque rotated -1:", dq)
