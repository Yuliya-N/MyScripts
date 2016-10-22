import doctest
import unittest

import duplicates


class RemoveDupsTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(
            duplicates.remove_duplicates(data=''),
            []
        )

    def test_no_dups(self):
        self.assertEqual(
            duplicates.remove_duplicates('abcdefgABCDEFG'),
            list('abcdefgABCDEFG')
        )

    def test_datatypes(self):
        self.assertEqual(
            duplicates.remove_duplicates([1, 2, 3, 8, 3, 2, 8]),
            [1, 2, 3, 8]
        )
        self.assertEqual(
            duplicates.remove_duplicates(
                ('alpha', 'bravo', 'charlie', 'bravo', 'delta', 'alpha', 'foxtrot')
            ),
            ['alpha', 'bravo', 'charlie', 'delta', 'foxtrot']
        )
        self.assertEqual(
            duplicates.remove_duplicates('abcbad'),
            ['a', 'b', 'c', 'd']
        )


class GetDupsTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(
            duplicates.get_duplicates(data=[]),
            {}
        )

    def test_no_dups(self):
        self.assertEqual(
            duplicates.get_duplicates([8, 4.0, 6, 1]),
            {}
        )

    def test_datatypes(self):
        self.assertEqual(
            duplicates.get_duplicates([8, 8, 8, 8]),
            {8: 4}
        )
        self.assertEqual(
            duplicates.get_duplicates((8, 6, 8, 4, 8, 4, 8, 2)),
            {8: 4, 4: 2}
        )
        self.assertEqual(
            duplicates.get_duplicates('8888'),
            {'8': 4}
        )


def load_tests(loader, suite, *args):
    suite.addTest(doctest.DocTestSuite(duplicates))
    return suite


if __name__ == '__main__':
    unittest.main()
