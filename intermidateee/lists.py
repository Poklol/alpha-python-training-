#Initialization and printing
my_list = ["banana", "cherry", "apple"]
print(my_list)

# empty list creation
my_list_2 = list()

#different data types and duplicates
mixed_list = [5, True, "apple", "apple"]
print(mixed_list)

#accessing elements by index
item = my_list[0]       # first element: 'banana'
last_item = my_list[-1] # last element: 'apple'
print(item, last_item)

#Iterating and membership check
for fruit in my_list:
    print(fruit)

if "banana" in my_list:
    print("Yes, banana is in the list")

# List methods
print("Length:", len(my_list))
my_list.append("lemon")             # add to the end
my_list.insert(1, "blueberry")      # insert at index 1
popped_item = my_list.pop()         # removes and returns last item
my_list.remove("cherry")            # removes specific item
# my_list.clear()                   # empties the list

#Sorting
numbers = [4, 2, 3, 1, -1, -5, 10]
numbers.sort()                      # in-place sort (modifies original)
new_sorted = sorted(numbers)        # returns a new sorted list

#Repetition and concatenation
zeros = [0] * 5
combined = zeros + [1, 2, 3]

#Slicing: [start:stop:step]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub = nums[1:5]                     # index 1 up to (not including) 5
step_slice = nums[::2]              # every second item
reversed_nums = nums[::-1]          # reverse trick

# copying (prevent modifying original reference)
original = ["banana", "cherry", "apple"]
copy_list = original.copy()         # aalternatives: list(original) or original[:]

#  list Comprehension
squared = [x * x for x in [1, 2, 3, 4, 5, 6]]
print("Squared numbers:", squared)
