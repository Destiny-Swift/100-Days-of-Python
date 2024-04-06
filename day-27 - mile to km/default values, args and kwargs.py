# functions with default values
# def my_function(a=1, b=2, c=3):
#     print(a, b, c)
#
#
# my_function(b=3)
# default values get set by equating the arguments to values when creating the function


# functions with unlimited *positional* arguments
# def add(*args):
#     return sum(args)
#
#
# print(add(3, 5, 6))


# functions with unlimited keyword arguments
def calculate(n, **kwargs):

    # testing default args with unlimited kwargs
    add = 2  # only way to set default values that could be altered by unlimited kwargs
    if 'add' in kwargs.keys():
        add = kwargs['add']
    n += add
    n *= kwargs['multiply']
    print(n)


calculate(2, multiply=5)
'''
And works like a charm. Used in the turtle, tkinter, et. al. modules. default values that could be altered using 
unlimited keyword arguments

When a default value is set; and reset when calling an instance; default arguments apply; not kwargs
add = default argument, multiply = kwarg

To get default values that could be changed with the unlimited kwargs; don't pass as argument. Create variable inside 
function or class and use if statement to check kwargs and then replace if found.
'''


# also works for classes
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')


my_car = Car(make='Lamborghini', model='Sesto Elemento')  # , make='GT-R')

print(my_car.make, my_car.model)
