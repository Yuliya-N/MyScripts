import unittest
from Cart import Cart
from User import User
from Item import Item


class CartTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User('user1', 'ashgdhsfv')
        self.cart = Cart(self.user)

    def tearDown(self):
        # redundant here, as on each cycle setUp will re-create those objects
        # but in case we waqnt to "help" python
        del self.cart
        del self.user

    def test_init(self):
        # user2 = User('user1', 'ashgdhsfv', email='user1@gmail.com')
        self.assertIs(self.cart.user, self.user)

    def test_total_empty(self):
        # self.assertTrue(hasattr(cart, 'total'))
        # self.assertTrue(callable(cart.total))
        # the next assert makes it unnecessary
        self.assertEqual(self.cart.total(), 0)

    # @unittest.skip('Needs .add')
    def test_total_non_empty(self):
        item = Item('item1', 10)
        self.cart.add(item)
        self.assertEqual(self.cart.total(), 10)

    def test_total_two_different_items(self):
        item1 = Item('item1', 10)
        item2 = Item('item2', 20)
        self.cart.add(item1, 1)
        self.cart.add(item2, 2)
        self.assertEqual(self.cart.total(), 50)

    def test_total_multiple_items(self):
        item1 = Item('item1', 10)
        self.cart.add(item1, 2)
        self.assertEqual(self.cart.total(), 20)

    def test_muliadd(self):
        item = Item('item1', 10)
        self.cart.add(item, 1)
        self.cart.add(item, 2)
        self.assertEqual(self.cart.total(), 30)

    def test_add(self):
        item = Item('item1', 10)
        self.assertIs(self.cart.add(item, 1), None)

    def test_add_same(self):
        item1 = Item('item1', 10)
        item2 = Item('item1', 10)
        self.cart.add(item1)
        self.cart.add(item2)
        self.assertEqual(self.cart._items, 1)
        # add method that returns items and then >> len 1



if __name__ == '__main__':
    unittest.main()
