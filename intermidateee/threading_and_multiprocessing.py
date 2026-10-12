# Multiprocessing vs Threading, Race Conditions, Locks, and Process Pool
import time
from threading import Thread, Lock
from multiprocessing import Process, Value, Array, Pool
database_value = 0

def increase(lock):
    """ accessing and updating shared data."""
    global database_value
    # using lock as context manager automatically acquires and releases it
    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.01)  # Simulates I/O operation
        database_value = local_copy


def cube(number):
    """CPU-bound task to calculate the cube of a number."""
    return number * number * number


if __name__ == "__main__":
    #  Demonstration of Threading with a Lock
    t_lock = Lock()
    thread1 = Thread(target=increase, args=(t_lock,))
    thread2 = Thread(target=increase, args=(t_lock,))

    thread1.start()
    thread2.start()

    # join() blocks the main thread until the worker thread finishes
    thread1.join()
    thread2.join()

    print("End value threading (protected with Lock):", database_value)

    # Demonstration of Multiprocessing Pool
    # Controls a pool of worker processes to run functions in parallel
    numbers = range(10)
    with Pool() as pool:
        # map() splits the input iterable into chunks across available CPU cores
        results = pool.map(cube, numbers)
        print("Multiprocessing Pool results:", results)
