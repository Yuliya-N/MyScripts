import doctest
import unittest

import shopping
from shopping import sorted_shopping_list as ssl


class OrderTestCase(unittest.TestCase):
    def setUp(self):
        self.mapping = {
            'Bakery': ['Bread', 'Cake', 'Pie'],
            'Produce': ['Apple', 'Pear', 'Plum', 'Pineapple'],
            'Deli': ['Salami', 'Gresh pasta'],
            'Grocery': ['Rice', 'Flour'],
            'Dairy': ['Milk', 'Eggs', 'Butter'],
            'Pet': ['Cage', 'Petfood']
        }
        self.order = ['Produce', 'Grocery', 'Deli', 'Bakery', 'Dairy', 'Pet']

    def test_empty_departments(self):
        self.assertEqual(
            ssl(['Apple', 'Meat'], self.mapping, []),
            [],
            msg='There may be no departments at all.'
        )

    def test_missing_mapping(self):
        self.assertEqual(
            ssl(['Milk', 'Unknown Product'], self.mapping, self.order),
            ['Milk'],
            msg="If product's missing in mapping, "
            "it shouldn't be included in result"
        )

    def test_empty_mapping(self):
        self.assertEqual(
            ssl(['Apple', 'Pear', 'Milk'], {}, self.order),
            []
        )

    def test_missing_department(self):
        self.assertEqual(
            ssl(['Cake', 'Pineapple'], self.mapping, ['Bakery', 'Deli']),
            ['Cake'],
            msg='There may be department in mapping,'
            ' but no such department in market. '
            'You should not include products from such department '
            'in your result'
        )

    def test_reverse(self):
        self.assertEqual(
            ssl(['Milk', 'Salami', 'Pear', 'Cage'], self.mapping, self.order),
            ['Pear', 'Salami', 'Milk', 'Cage']
        )
        self.assertEqual(
            ssl(
                shopping_list=['Milk', 'Salami', 'Pear', 'Cage'],
                mapping=self.mapping,
                departments_order=list(reversed(self.order))
            ),
            ['Cage', 'Milk', 'Salami', 'Pear']
        )

    def test_preserve_list_order(self):
        self.assertEqual(
            ssl(['Butter', 'Eggs', 'Milk'], self.mapping, self.order),
            ['Butter', 'Eggs', 'Milk'],
            msg='Order from shopping list should '
            'be preserved as much as possile'
        )

    def test_extra_department(self):
        self.order.append('New dep')
        self.assertEqual(
            ssl(['Butter', 'Pie'], self.mapping, self.order),
            ['Pie', 'Butter']
        )

    def test_empty_shopping_list(self):
        self.assertEqual(
            ssl([], self.mapping, self.order),
            []
        )


def load_tests(loader, suite, *args):
    suite.addTest(doctest.DocTestSuite(shopping))
    return suite


if __name__ == '__main__':
    unittest.main()
