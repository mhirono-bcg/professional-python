import unittest

from cart import ShoppingCart
from product import Product


class ShoppingCartTestCase(unittest.TestCase):
    def test_cart_empty(self):
        cart = ShoppingCart()
        self.assertDictEqual({}, cart.products)

    def test_add_product(self):
        cart = ShoppingCart()
        product = Product("shoes", "S", "blue")
        cart.add_product(product)
        expected_value = {"SHOES-S-BLUE": {"quantity": 1}}
        self.assertDictEqual(expected_value, cart.products)

    def test_add_and_remove_product(self):
        cart = ShoppingCart()
        product = Product("shoes", "S", "blue")
        cart.add_product(product)
        cart.remove_product(product)

        self.assertDictEqual({}, cart.products)

    def test_add_and_remove_product_excessively(self):
        cart = ShoppingCart()
        product = Product("shoes", "S", "blue")
        cart.add_product(product, quantity=1)
        cart.remove_product(product, quantity=2)

        self.assertDictEqual({}, cart.products)
