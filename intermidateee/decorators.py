# decorators for extending function behavior without modifying the original code
import functools

#Basic Function Decorator Template
# Functions are first-class objects: can be passed, nested, and returned
def my_decorator(func):
    @functools.wraps(func)  # Preserves the identity and docstring of the original function
    def wrapper(*args, **kwargs):
        print("Start: Doing something before function execution")
        result = func(*args, **kwargs)
        print("End: Doing something after function execution")
        return result
    return wrapper

@my_decorator
def print_name(name):
    print(f"Executing function: Hello {name}")
    return name

res = print_name("charu")
print("Returned result:", res)
print("Function name preserved:", print_name.__name__)  # Prints 'print_name', not 'wrapper'

# 2. Decorators that take arguments (requires 3 nested function levels)
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Greetings, {name}!")

greet("sivani")

# Nested / Stacked Decorators 
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@my_decorator
def add_five(x):
    return x + 5

print("Nested result:", add_five(10))

# Class Decorator (used to maintain and track internal state)
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0  # Internal state counter

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This function has been executed {self.num_calls} time(s)")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi there!")

say_hi()
say_hi()