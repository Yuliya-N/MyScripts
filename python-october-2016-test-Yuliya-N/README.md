Python course assignment
========================

Getting started
---------------
1. Clone this repository with `git clone ...`
2. Take task
3. Write code
4. Ensure that tests are passing (if available)
5. Commit/push
6. Go to #2 :)

Rules
-----
1. Given files should remain in same places with same names. You can add any additioanl files you need
2. If files provide function interface/signature, it must remain unchanged (until otherwise stated). You can add any wrappers, helpers, adapters as you need, but tests will still run against original signatures

3rd-party code
--------------
If your code requires some 3rd-party library, add its name to `requirements.txt`

Running tests
-------------
1. To run all available tests – `python -m unittest discovery` from root directory.
2. To run tests against single file – simply run corresponding test file. I.e. `python test_duplicates.py`
3. Most of task files will trigger unittest for themself upon running. I.e. `python duplicates.py` will run testing suite for this file.
4. Most functions' docstring contains usage examplse/doctests. All this tests run together with unittests. If you want to ensure that docstring examples passes correctly – simply run unittest for this file.

Tasks
-----
There's 14 exercises total with no difficulty difference shown nor priority. You should take as much as you can in priority you want.
List of tasks, sorted alphabetically by boilerplate filename:

1. Implement LRU_cache decorator `cache.py`
2. Remove duplicates `duplicates.py`
3. Count duplicates `duplicates.py`
4. Count sum of numbers in nested structure `irregular_sequence.py`
5. Count multiplication of numbers in nested structure `irregular_sequence.py`
6. Implement case-insensitive sorting `isort.py`
7. Implement hierarchy of food `OOP_food.py`
8. Implement hierarchy of shapes `OOP_shapes.py`
9. Count sum of numbers in flat structure `regular_sequence.py`
10. Count multiplication of numbers in flat structure `regular_sequence.py`
11. Get shopping list cost `shopping.py`
12. Get shopping list total `shopping.py`
13. Get optimal route fro your shopping list `shopping.py`
14. Implement class hierarchy for transport graph `transport.py`
