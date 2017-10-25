# -*- coding: utf-8 -*-
"""
Suppose we could access yesterday's stock prices as a list, where:

- The indices are the time in minutes past trade opening time, which was 9:30am local time.
- The values are the price in dollars of Apple stock at that time.

So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

@see https://www.interviewcake.com/?utm_medium=affiliate&utm_source=interviewingio&utm_campaign=interviewingio
"""
from __future__ import unicode_literals

stock_prices_yesterday = [
    ([10, 14, 7, 5, 8, 11, 5, 9], 6),
    ([10, 10, 7, 5, 8, 11, 4, 9], 6),
    ([10, 5, 7, 5, 8, 11, 4, 9], 6),
    ([10, 9, 8, 7, 6], -1),
    ([10], 0),
]


def get_max_profit_On2(prices):
    """
    O(n^2) time due to nested loops.
    """
    highest = None
    for idx, lowprice in enumerate(prices):
        for highprice in prices[idx+1:]:
            profit = highprice - lowprice
            if highest == None or profit > highest:
                highest = profit
    return highest


def get_max_profit_On(prices):
    """
    O(n).
    """
    if len(prices) < 2:
        return 0

    max_profit = prices[1] - prices[0]
    min_price = prices[0]

    for idx, price in enumerate(prices):
        if idx == 0:
            continue

        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)

    return max_profit

# get_max_profit = get_max_profit_On2
get_max_profit = get_max_profit_On

def main():
    for test in stock_prices_yesterday:
        print(get_max_profit(test[0]) == test[1])

if __name__ == '__main__':
    main()
