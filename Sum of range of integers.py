"""
Sum of Integers Up to n

Write a function that takes a single integers as input and returns the sum of the integers from zero to the input parameter.

The function should return 0 if non-integer is passed in.
"""

def sum_of_integers(n):
    try:
        result = sum(range(n + 1))
    except TypeError:
        result = 0
    return result

"""
Optional lower limit
"""
def sum_of_integers_v2(n, ll):
    try:
        result = sum(range(ll, n + 1))
    except TypeError:
        result = 0
    return result
