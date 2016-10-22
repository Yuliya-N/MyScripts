def isort(words):
    """
    Performs case-insensitive sorting
    >>> isort(['Avocado', 'apple', 'Lime', 'lemon'])
    ['apple', 'Avocado', 'lemon', 'Lime']

    If mutable argument passed, it must remain unchanged:
    >>> data = ['Avocado', 'apple', 'Lime', 'lemon']
    >>> isort(data)
    ['apple', 'Avocado', 'lemon', 'Lime']
    >>> data
    ['Avocado', 'apple', 'Lime', 'lemon']

    Elements with equal sorting values should preserve original order:
    >>> isort(['lemon', 'Avocado', 'avocado', 'leMon', 'Lemon'])
    ['Avocado', 'avocado', 'lemon', 'leMon', 'Lemon']

    You may assume that strings in `words` will contain only ASCII characters

    Args:
        words: iterable of strings (list, tuple, generator etc.)

    Returns:
        List with original items sorted
    """
    return


# code below left for your own usage and can be deleted at will
# -------------------------------------------------------------
if __name__ == '__main__':
    # tests for this function lives in tests/test_isort.py
    import unittest
    unittest.main(module='test_isort')
