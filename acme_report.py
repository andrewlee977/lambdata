"""
Part 4: This file contains random products
generated from Product class in acme.py
"""

from acme import Product
import random
from statistics import mean


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Peanuts']


def generate_products(num_products=30):
    """
    Function generates 30 (default) products at random.
    """
    products = []

    for n in range(num_products):
        full_name = random.choice(ADJECTIVES) + " " + random.choice(NOUNS)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0, 2.5)
        new_prod = Product(name=full_name, price=price,
                           weight=weight, flammability=flammability)
        products.append(new_prod)
    return products


def inventory_report(product_list):
    """
    Function prints official inventory report of products passed to it
    """
    unique_list = []
    prices = []
    weights = []
    flammabilities = []

    for p in product_list:
        prices.append(p.price)
        weights.append(p.weight)
        flammabilities.append(p.flammability)

        if p.name not in unique_list:
            unique_list.append(p.name)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print("Number of unique product names: ", len(unique_list))
    print("Average Prices: ", mean(prices))
    print("Average Weights: ", mean(weights))
    print("Average Flammability: ", mean(flammabilities))


if __name__ == '__main__':
    """
    This function runs when the file runs
    """
    inventory_report(generate_products())
