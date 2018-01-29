def outer():
    def inner():
        print('This is inner.')

    print('This is outer, returning inner.')
    return inner


my_func = outer()   # This is outer, re

my_func()   # This is inner.
my_func()   # This is inner.
