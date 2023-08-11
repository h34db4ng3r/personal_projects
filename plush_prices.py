import math


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
        if x > 0:
            return x - 0.01
        else:
            return 0

    def name(self):
        return '{} {}'.format(self.size, self.animal)

    def lowercase_name(self):
        x = self.name()
        return x.lower()

    def request_plush(self):
        x = self.final_price()
        y = self.price
        z = self.street_value()
        w = self.lowercase_name()

        print()
        print(w)
        print(f'Price from vendor: {y},-')
        print(f'Price that makes business sense: {z},-')
        print(f'Price that makes sense for the shelf: {x},-')


plush_1 = SoftPlush('bear', 'small', 9.5645)
plush_2 = SoftPlush('Lion', 'large', 0)
plush_3 = SoftPlush('Cat', 'medium', 11)
plush_4 = SoftPlush('dog', 'medium', -10)

plush_1.request_plush()
plush_2.request_plush()
plush_3.request_plush()
plush_4.request_plush()


"""

it would be nice for a solution for the values that are equal to or below zero,
f.ex taking the size and approximating a value based on that, ( hashmap / dict )

"""
