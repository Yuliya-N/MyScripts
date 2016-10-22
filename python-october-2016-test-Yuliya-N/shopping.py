def get_cost_list(shopping_list, prices):
    """
    Getting shopping list and prices for goods in it,
     returns list of costs for all products that can be purchased.
    Original order from shopping list must be preserved.

    >>> goods = [('Apple', 2.5), ('Pear', 1), ('Pumpkin', 1.5)]
    >>> prices = {'Apple': 9.50, 'Pear': 23.80, 'Pumpkin': 4.50}
    >>> get_cost_list(goods, prices)
    [('Apple', 23.75), ('Pear', 23.8), ('Pumpkin', 6.75)]

    If there's no price available for product, don't include it into output
    >>> goods = [('Apple', 2.5), ('Pear', 1), ('Pumpkin', 1.5)]
    >>> prices = {'Apple': 9.50, 'Milk': 12}
    >>> get_cost_list(goods, prices)
    [('Apple', 23.75)]
    >>> get_cost_list(goods, {})
    []

    You may assume that units and names in shopping list and price list are
     unified. I.e. if you have kg in shopping list, price will be per kg

    Args:
        shopping_list: list with (product_name : amount) pairs as tuples
            product_name is string
            amount is numeric
        prices: dictionary with {product_name : price} pairs as key-value
            product_name is string
            price is numeric

    Returns:
        List with (product_name : cost) pairs as tuples
            product_name is string
            cost is numeric
    """
    return


def get_total(shopping_list, prices):
    """
    Getting shopping list and prices for goods in it,
     returns total cost of available products.

    >>> goods = {'Apple': 2.5, 'Pear': 1, 'Pumpkin': 1.5}
    >>> prices = {'Apple': 9.50, 'Pear': 23.80, 'Pumpkin': 4.50}
    >>> get_total(goods, prices)
    54.3

    If there's no price available for product, don't include it in total
    >>> goods = {'Apple': 2.5, 'Pear': 1, 'Pumpkin': 1.5}
    >>> prices = {'Apple': 9.50, 'Coconut': 20}
    >>> get_total(goods, prices)
    23.75
    >>> get_total(goods, {})
    0

    You may assume that units and names in shopping list and price list are
     unified. I.e. if you have kg in shopping list, price will be per kg

    Args:
        shopping_list: dict with {product_name : amount} pairs as key-value
            product_name is string
            amount is numeric
        prices: dictionary with {product_name : price} pairs as key-value
            product_name is string
            price is numeric

    Returns:
        Total cost as single number
    """
    return


def sorted_shopping_list(shopping_list, mapping, departments_order):
    """
    Getting shopping list, department-to-products mapping and
     departments order inside shop, returns products from shopping list,
     ordered by department location, effectively giving you
     optimal way to go through the market.

    I.e. you need to buy bread, apples, milk and salami.
    Placement of departments inside store is
     Produce -> grocery -> deli -> bakery -> dairy
    So, optimal way to shop up is
     apples -> salami -> bread -> milk
    Possible calls for following schema:
    >>> needs = ['Bread', 'Apple', 'Milk', 'Salami']
    >>> mapping = {
    ... 'Bakery': ['Bread', 'Cake', 'Pie'],
    ... 'Produce': ['Apple', 'Pear', 'Plum', 'Pineapple'],
    ... 'Deli': ['Salami', 'Gresh pasta'],
    ... 'Grocery': ['Rice', 'Flour'],
    ... 'Dairy': ['Milk', 'Eggs', 'Butter']
    ... }
    >>> placement = ['Produce', 'Grocery', 'Deli', 'Bakery', 'Dairy']
    >>> sorted_shopping_list(needs, mapping, placement)
    ['Apple', 'Salami', 'Bread', 'Milk']

    If you need some product (it's passed in shopping_list),
     but its not available in shop, dont include this product in result.
    Department-product mapping and departments order may not be
     synced. I.e., 'Pie' is 'Bakery' product, but there's no 'Bakery'
     in current shop.
    Original order from shopping list should be preserved inside every
     single department.
    You may assume that units and names in shopping list and price list are
     unified. I.e. if you have kg in shopping list, price will be per kg

    Args:
        shopping_list: list with product names as strings
        mapping: dictionary with {department : products } as key-value
            department is string
            products is list
        departments_order: list of departments

    Returns:
        List of needed products, sorted by department position
    """
    return


# code below left for your own usage and can be deleted at will
# -------------------------------------------------------------
if __name__ == '__main__':
    # tests for this module lives in tests/test_shopping.py
    import unittest
    unittest.main(module='test_shopping')
