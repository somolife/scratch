"""
supports lazy evaluation!
"""
from decorators import print_fn_name


def num_generator_up_to(n):
    i = 0
    while i < n:
        yield i  # magic!
        i += 1


@print_fn_name
def use_generator(n):
    for a in num_generator_up_to(n):
        print a


use_generator(3)
