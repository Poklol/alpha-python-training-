# Context Managers: allocating and releasing resources precisely when intended
from contextlib import contextmanager
with open('notes.txt', 'w') as file:
    file.write('some todo...')

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("Enter: Allocating resource")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # If an exception occurred inside the with block:
        if exc_type is not None:
            print(f"Exception caught in context manager: {exc_val}")
            # Returning True suppresses the exception from propagating further
            return True
        print("Exit: Resource safely released")


# usage of class-based context manager
with ManagedFile('notes.txt') as f:
    f.write('Custom class context manager writing data.')
    print("Writing finished inside context.")



@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        print("Generator enter: opening file")
        yield f  # temporarily suspends execution and returns resource
    finally:
        print("Generator exit: closing file")
        f.close()


# usage of generator-based context manager
with open_managed_file('notes2.txt') as f:
    f.write('Generator-based context manager writing data.')
    print("Writing finished inside generator context.")
