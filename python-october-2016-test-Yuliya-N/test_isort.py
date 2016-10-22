import doctest
import unittest

import isort as isort_module
from isort import isort


class iSortTestCase(unittest.TestCase):
    def test_empty(self):
        msg = 'Calling `isort` with empty list should return empty list'
        self.assertEqual(
            isort(data=[]),
            [],
            msg
        )

    def test_single(self):
        msg = 'Calling `isort` with 1-element list sould return equal list'
        self.assertEqual(
            isort(['apple']),
            ['apple'],
            msg
        )

    def test_presorted(self):
        msg = 'Calling `isort` with presorted list should return equal list'
        self.assertEqual(
            isort(['a', 'b', 'c', 'd']),
            ['a', 'b', 'c', 'd'],
            msg
        )

    def test_reversed(self):
        self.assertEqual(
            isort(['d', 'c', 'b', 'a']),
            ['a', 'b', 'c', 'd'],
        )

    def test_mutable_arg(self):
        msg = '`isort` should not change passed arguments, but return new structues instead'
        data = ['d', 'a', 'c', 'b']
        self.assertFalse(
            isort(data) is data,
            msg
        )
        self.assertEqual(
            data, ['d', 'a', 'c', 'b'],
            msg
        )

    def test_tuple(self):
        """ `isort` must be able to accept tuples """
        self.assertEqual(
            isort(('d', 'c', 'b', 'a')),
            ['a', 'b', 'c', 'd']
        )

    def test_generator(self):
        """ `isort` must be able to accept geenrators """
        gen = (str(x) for x in range(5))
        self.assertEqual(
            isort(gen),
            ['0', '1', '2', '3', '4']
        )

    def test_preserve_case(self):
        msg = '`isort` should not change letter case, but just sort them'
        self.assertEqual(
            isort(['Mango', 'olive', 'ORANGE', 'pLUM']),
            ['Mango', 'olive', 'ORANGE', 'pLUM'],
            msg
        )

    def test_preserve_order(self):
        msg = '`isort` should preserve word order if they have same sorting value'
        self.assertEqual(
            isort(['Tomato', 'TOMATO', 'tomato', 'ToMaTo']),
            ['Tomato', 'TOMATO', 'tomato', 'ToMaTo'],
            msg
        )


def load_tests(loader, suite, *args):
    suite.addTest(doctest.DocTestSuite(isort_module))
    return suite


if __name__ == '__main__':
    unittest.main()
