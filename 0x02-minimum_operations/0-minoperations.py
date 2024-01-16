#!/usr/bin/python3

"""
   the method that calculates the fewest number of operations
   needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """ The function """
    nbr_operation = 0
    min_divisor = 2

    while n > 1:
        while n % min_divisor == 0:
            nbr_operation += min_divisor
            n /= min_divisor
        min_divisor += 1
    return nbr_operation
