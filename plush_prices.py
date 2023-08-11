import math


"""
- This code returns a new price based on vendor prices
- gives the plush a new name based on type of animal, and size
- and makes the prices more attractive ( ending in .99 )
"""


class SoftPlush:
    def __init__(self, animal, size, price):
        self.animal = animal
        self.size = size
        self.price = price

    def street_value(self):
        street_price = self.price * 3.2
        new_price = round(street_price, 2)
        return new_price

    def whole_number(self):
        x = self.street_value()
        ceil_x = math.ceil(x)
        rinse = math.ceil(ceil_x / 10)
        bring_up = rinse * 10
        return bring_up

    def final_price(self):
        x = self.whole_number()
        return x - 0.01

    def name(self):
        return '{} {}'.format(self.size, self.animal)

    def request_plush(self):
        x = self.final_price()
        print()
        print(self.name())
        print('Price from vendor: {}'.format(self.price))
        print('Price that makes business sense: {}'.format((self.street_value())))
        print('Price that makes sense: {}'.format(self.final_price()))


plush_1 = SoftPlush('bear', 'small', 9)
plush_2 = SoftPlush('Lion', 'large', 14.4)

plush_1.request_plush()
plush_2.request_plush()
