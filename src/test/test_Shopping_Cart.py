import unittest
from Shopping_Cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Apple", 5)
        self.cart.add_item("Apple", 3)
        self.cart.add_item("Banana", 3)
        self.cart.add_item("Orange", 3)
        self.cart.add_item("Pear", 1)
        self.cart.add_item("Kiwi", 1)
        self.assertEqual(self.cart.items["Apple"], 8)
        self.assertEqual(self.cart.items["Banana"], 3)
        self.assertEqual(self.cart.items["Orange"], 3)
        self.assertEqual(self.cart.items["Pear"], 1)
        self.assertEqual(self.cart.items["Kiwi"], 1)

    def test_remove_item(self):
        self.cart.add_item("Apple", 5)
        self.cart.remove_item("Apple", 3)
        self.assertEqual(self.cart.items["Apple"], 2)

        self.cart.remove_item("Apple", 2)
        self.assertNotIn("Apple", self.cart.items)



    def test_add_item_negative_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Banana", -2)
            #self.cart.add_item("Apple", -2)
            #self.cart.add_item("Kiwi", -1)
            #self.cart.add_item("Orange", -3)
            #self.cart.add_item("Pear", -1)"""

    def test_add_item_zero_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Banana", 0)
            #self.cart.add_item("Kiwi", 0)

    def test_get_total(self):
        self.cart.add_item("Apple", 5)
        self.cart.add_item("Banana", 3)
        self.cart.add_item("Orange", 3)
        self.cart.add_item("Pear", 1)
        self.cart.add_item("Kiwi", 1)

        self.assertEqual(self.cart.get_total(), 130)

        self.cart.remove_item("Apple", 3)
        self.assertEqual(self.cart.get_total(), 100)

        self.cart.remove_item("Banana")
        self.assertEqual(self.cart.get_total(), 90)

        self.cart.remove_item("Orange")
        self.assertEqual(self.cart.get_total(), 80)

        self.cart.remove_item("Pear")
        self.assertEqual(self.cart.get_total(), 70)

        self.cart.remove_item("Kiwi")
        self.assertEqual(self.cart.get_total(), 60)