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
        # but in case we want to "help" python
        del self.cart
        del self.user

    def test_init(self):
        self.assertIs(self.cart.user, self.user)

    def test_total_empty(self):
        # self.assertTrue(hasattr(cart, 'total'))
        # self.assertTrue(callable(cart.total))
        # ---the next assert makes it unnecessary
        self.assertEqual(self.cart.total(), 0)
        self.assertEqual(len(self.cart), 0)

    def test_total_non_empty(self):
        item = Item('item1', 10)
        self.cart.add(item)
        self.assertEqual(self.cart.total(), 10)
        self.assertEqual(len(self.cart), 1)

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
        self.assertEqual(len(self.cart), 1)

    def test_muliadd(self):
        item = Item('item1', 10)
        self.cart.add(item, 1)
        self.cart.add(item, 2)
        self.assertEqual(self.cart.total(), 30)
        self.assertEqual(len(self.cart), 1)

    def test_add(self):
        item = Item('item1', 10)
        self.assertIs(self.cart.add(item, 1), None)
        self.assertEqual(len(self.cart), 1)

    # @unittest.skip('Needs identification of similar items')
    def test_add_same(self):
        """ After we added __hash__ and __eq__ methods in item
        the cart.add method recognizes the similar items and adds them do
        cart.self._items dictionary as one item
        """
        item1 = Item('item1', 10)
        item2 = Item('item1', 10)
        self.cart.add(item1)
        self.cart.add(item2)
        self.assertEqual(len(self.cart), 1)

    def test_cart_len(self):
        self.assertEqual(len(self.cart), 0)
        self.cart.add(Item('item1', 10), 1)
        self.assertEqual(len(self.cart), 1)
        self.cart.add(Item('item2', 20), 3)
        self.assertEqual(len(self.cart), 2)

    def test_cart_qt(self):
        self.assertEqual(self.cart.total_qt(), 0)
        self.cart.add(Item('item1', 10), 2)
        self.assertEqual(self.cart.total_qt(), 2)
        self.cart.add(Item('item1', 10), 5)
        self.assertEqual(self.cart.total_qt(), 7)

    def test_iteration(self):
        self.cart.add(Item('item1', 10), 1)
        self.cart.add(Item('item2', 20), 2)
        self.assertEqual(sum(i.price for i in self.cart), 30)


if __name__ == '__main__':
    unittest.main()
