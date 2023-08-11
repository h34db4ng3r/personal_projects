"""

- This code returns a new price based on vendor prices
- gives the plushies a new name based on type of animal, and size
- and makes the prices make more sense to a consumer

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


"""

    I need this to take in the new value of the plush
    and give it a new price
    the new price should end with 9.99
    and if the price is in the hundreds it should end with 99.99
    and should scale accordingly

"""

    def pretty_prices(self):
        x = self.street_value()
        

        return x


    def name(self):
        return '{} {}'.format(self.size, self.animal)


plush_1 = SoftPlush('bear', 'small', 9)
plush_2 = SoftPlush('Lion', 'large', 14.4)

print(plush_1.size)
print(plush_2.size)


print(plush_2.street_value())

print(plush_1.name())

print(plush_1.price)
print(plush_1.street_value())
print(plush_1.pretty_prices())
