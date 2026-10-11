# errors and exceptions: raising, handling, and custom error classes

#raising an exception manually with 'raise'
x = -5
if x < 0:
    # raise Exception("x should be positive")
    pass

# Using 'assert' to test conditions (raises AssertionError if False)
assert (x < 0), "x is not negative"

#handling exceptions with try, except, else, and finally
try:
    a = 5 / 1
    b = a + 4
except ZeroDivisionError as e:
    print(f"Caught ZeroDivisionError: {e}")
except TypeError as e:
    print(f"Caught TypeError: {e}")
else:
    print("Everything is fine (runs only if NO exceptions occurred)")
finally:
    print("Cleaning up (runs always, whether an exception occurred or not)")

# catching multiple specific exceptions
try:
    val = 5 / 0
except (ZeroDivisionError, TypeError) as e:
    print("Handled arithmetic/type failure:", e)

#defining custom exception classes (inherit from Exception)
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(val):
    if val > 100:
        raise ValueTooHighError("Value is too high")
    if val < 5:
        raise ValueTooSmallError("Value is too small", val)

# testing custom exceptions
try:
    test_value(1)
except ValueTooHighError as e:
    print("Custom error:", e)
except ValueTooSmallError as e:
    print(f"Custom error: {e.message}, received value: {e.value}")
