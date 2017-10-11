import math


def add(a, b):
    pass
    # Eventually this will be the adding code
    #TODO have t make this not just add two numbers but to be able to add more than two.

def subtract(a, b):
    pass
    # Eventually this will be the subtracting code

def multiply(a, b):
    pass
    # eventully this will be the multiplication code


def divide(a, b):
    pass
    # and conquer

def fibonacci(limit):
    # Will calculate a fibonacci sequence up to the limit value
    # Is recursive to save memory usage for large sequences.
    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        yield current





if __name__ == '__main__':
    print("Fibonnaci sequence: ")
    for n in (fibonacci(1000)):
        print(n, end=', ')