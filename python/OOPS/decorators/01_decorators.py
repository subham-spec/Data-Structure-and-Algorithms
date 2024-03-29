# Decorator to measure the time of execution of a function

import time

def func(*args, **kwargs):
    mul = 1
    for i in args:
        mul *= i
    return mul

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        total_time = time.time()-start
        print(f"{func.__name__} result runs for {total_time}")
        return result
    return wrapper

@timer
def sleeper(t):
    time.sleep(t)

if __name__ == '__main__':
    sleeper(5)