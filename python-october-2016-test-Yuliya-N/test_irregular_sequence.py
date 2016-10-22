import doctest
import unittest

import irregular_sequence


def load_tests(loader, suite, *args):
    suite.addTest(doctest.DocTestSuite(irregular_sequence))
    return suite


if __name__ == '__main__':
    unittest.main()
