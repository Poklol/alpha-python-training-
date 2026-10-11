# Random Numbers: pseudo-random (random), cryptographically secure (secrets), and numpy arrays
import random
import secrets

# The random module (pseudo-random, reproducible, not for security)
float_val = random.random()          # Random float in range [0.0, 1.0)
uniform_val = random.uniform(1, 10)  # Random float in range [1.0, 10.0]
int_val = random.randint(1, 10)      # Random int in range [1, 10] (upper bound included)
range_val = random.randrange(1, 10)  # Random int in range [1, 10) (upper bound excluded)
norm_val = random.normalvariate(0, 1)# Normal distribution (mean=0, std=1)

print("Random float:", float_val)
print("Random int (1-10):", int_val)

# Working with sequences
letters = list("ABCDEFGH")
picked_one = random.choice(letters)          # Single random choice
unique_sample = random.sample(letters, 3)    # 3 unique items
repeated_choices = random.choices(letters, k=3) # 3 items, allows duplicates

random.shuffle(letters)                      # Shuffles list in-place
print("Shuffled letters:", letters)

# Reproducibility via seed 
random.seed(1)
print("Seeded random (1):", random.random())
random.seed(1)
print("Seeded random (1 repeated):", random.random())  # Exactly identical

# 2. The secrets module (cryptographically strong, used for passwords/auth tokens)
# Slower, but non-reproducible and safe for security purposes
sec_int = secrets.randbelow(10)      # Random int in range [0, 10)
sec_bits = secrets.randbits(4)       # Random integer with 4 bits (values 0-15)
sec_choice = secrets.choice(letters) # Cryptographically secure choice

print("Secure int (0-9):", sec_int)
print("Secure 4-bit integer:", sec_bits)
print("Secure choice:", sec_choice)

#   NumPy random 
try:
    import numpy as np

    # np.random generates multidimensional arrays of random numbers
    arr_floats = np.random.rand(3, 3)             # 3x3 array of floats in [0, 1)
    arr_ints = np.random.randint(0, 10, (3, 4))   # 3x4 array of ints between 0 and 9
    print("NumPy random 3x3 floats:\n", arr_floats)
    print("NumPy random 3x4 ints:\n", arr_ints)

    # NumPy has its own separate seed generator
    np.random.seed(1)
except ImportError:
    print("NumPy is not installed (run 'pip install numpy' if needed)")