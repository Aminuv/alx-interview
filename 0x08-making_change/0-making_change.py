#!/usr/bin/python3
"""
Make a file that change the module
"""


def makeChange(coins, total):
    if total == 0:
        return 0
    amounts = [float("inf")] * (total + 1)
    amounts[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            amounts[i] = min(amounts[i], amounts[i - coin] + 1)
    if amounts[total] != float("inf"):
        return amounts[total]
    else:
        return -1
