def add(*args):
    total = 0
    for n in args:
        total += n
    return total


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('make')
        self.color = kwargs.get('color')
        self.num_seats = kwargs.get('num_seats')


my_car = Car()
print(my_car.make)