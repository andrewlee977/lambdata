"""
This file contains the class `Product` for Acme Corporation
"""

import random


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        """
        Part 1: Constructor initializes Product class
        """
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = int(identifier)

    def stealability(self):
        """
        Part 2: function calculates stealability of an instance
        """
        ppw = self.price / self.weight
        if ppw < 0.5:
            return ('Not so stealable...')
        elif (ppw >= 0.5) and (ppw < 1.0):
            return ('Kinda stealable...')
        else:
            return ('Very stealable!')

    def explode(self):
        """
        Part 2: function calculates explodability of an instance
        """
        ftw = self.flammability * self.weight
        if ftw < 10:
            return ('...fizzle')
        elif (ftw >= 10) and (ftw < 50):
            return ('...boom!')
        else:
            return ('...BABOOM!!')


class BoxingGlove(Product):
    def __init___(self, name, price, flammability,
                  identifier, weight=10):
        """
        Part 3: Constructor initializes BoxingGlove class
        """
        super().__init__(name, price, weight, flammability,
                         identifier)

    def explode(self):
        """
        Part 3: function calculates explodability of an instance
        """
        return ("...it's a glove.")

    def punch(self):
        if self.weight < 5:
            return ('That tickles')
        elif (self.weight >= 5) and (self.weight < 15):
            return ('Hey that hurt!')
        else:
            return ('OUCH!')
