"""
Part 5: This file will test my acme_report functions
"""

from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


def test_default_product_price():
    """
    Test default product price being 10.
    """
    prod = Product('Test Product')
    assert prod.price == 10


def test_default_product_flammability():
    """
    Test default product flammability being 0.5.
    """
    prod = Product('Test Product')
    assert prod.flammability == 0.5


def test_stealability_and_explode():
    """
    Test methods stealability() == 'Very stealable!'
    and explode() == '...boom!'
    """
    prod_1 = Product(name='Test Product 1', price=10,
                     weight=10, flammability=2.0)
    assert prod_1.stealability() == 'Very stealable!'
    assert prod_1.explode() == '...boom!'


def test_default_num_products():
    """
    Test length of product list passed to inventory_report is 30.
    """
    prod_list = generate_products()
    assert len(prod_list) == 30


def test_legal_names():
    """
    Test names of 30 generated product names are valid names to generate
    """
    prod_list = generate_products()
    for p in prod_list:
        adj, noun = p.name.split()
    assert adj in ADJECTIVES
    assert noun in NOUNS
