import doctest
import unittest

import regular_sequence


def load_tests(loader, suite, *args):
    suite.addTest(doctest.DocTestSuite(regular_sequence))
    return suite


if __name__ == '__main__':
    unittest.main()
