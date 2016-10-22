import unittest
from cache import lru_cache


class CacheTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_default_cahce_size(self):
        l = lru_cache(32)
        self.assertEqual(l.cache_size, 32)


if __name__ == '__main__':
    unittest.main()
