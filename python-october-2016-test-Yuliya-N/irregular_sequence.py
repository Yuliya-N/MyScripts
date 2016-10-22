def sum_irregular(data):
    """
    Sums all elements in passed sequence.
    Sequence can contain plain numbers as well as other sequences with numbers

    >>> sum_irregular([3, 6, 9])
    18
    >>> sum_irregular([3, [6, 9]])
    18
    >>> sum_irregular([3, [6, [9]]])
    18
    >>> sum_irregular(range(10))
    45
    >>> sum_irregular([range(7), [7, 8], 9])
    45
    >>> sum_irregular((8.2, 6.3, 13.1))
    27.6
    >>> sum_irregular([])
    0
    >>> sum_irregular([[], tuple(), [], [[]]])
    0
    >>> sum_irregular([1, [2, 3], (4, 5), [6, [7, 8]], range(9, 10)])
    45

    Args:
        data: iterable or sequence with numbers or same sequences

    Returns:
        Sum of all single elements in passed args, as single number
    """
    return


def multiply_irregular(data):
    """
    Multiplies all elements in passed sequence.
    Sequence can contain plain numbers as well as other sequences with numbers

    >>> multiply_irregular(data=[3, 6, 9])
    162
    >>> multiply_irregular([3, [6], 9])
    162
    >>> multiply_irregular(range(10))
    0
    >>> multiply_irregular(range(1, 10))
    362880
    >>> multiply_irregular([1, [2, [3, 4], 5], range(6, 9), 9])
    362880
    >>> multiply_irregular(({8.2, 6.3}, 13.1))
    676.746
    >>> multiply_irregular([])
    1
    >>> multiply_irregular([[[]]])
    1

    Args:
        data: iterable or sequence with numbers

    Returns:
        Multiplication of all elements in passed args, as single number
    """
    return


# code below left for your own usage and can be deleted at will
# -------------------------------------------------------------
if __name__ == '__main__':
    # tests for this module uses docstrings as source
    import doctest
    doctest.testmod(verbose=True)
