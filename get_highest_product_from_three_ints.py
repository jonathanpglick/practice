# -*- coding: utf-8 -*-
"""
Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.

@see https://www.interviewcake.com/question/python/highest-product-of-3
"""
from __future__ import unicode_literals
from functools import partial

def get_highest_product_from_three_v1(arr):
    """
    Only works with positive numbers.
    """
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[0] * sorted_arr[1] * sorted_arr[2]

def get_highest_product_from_three_On(arr):
    """
    """
    highest_int = max(arr[0], arr[1])
    highest_product_of_2 = arr[0] * arr[1]
    lowest_int = min(arr[0], arr[1])
    lowest_product_of_2 = arr[0] * arr[1]
    highest_product = arr[0] * arr[1] * arr[2]

    for i in arr:
        highest_product = max(highest_product, i * highest_product_of_2, i * lowest_product_of_2)
        highest_product_of_2 = max(highest_product_of_2, i * highest_int)
        lowest_product_of_2 = min(lowest_product_of_2, i * lowest_int)
        highest_int = max(highest_int, i)
        lowest_int = max(lowest_int, i)

    return highest_product


# get_highest_product_from_three = get_highest_product_from_three_v1
get_highest_product_from_three = get_highest_product_from_three_On

def main():
    arr = [1, 5, 7, 4, 2, 9]
    answer = 315
    result = get_highest_product_from_three(arr)
    print(result == answer)
    print(result)

    arr = [-10, -10, 1, 3, 2]
    answer = 300
    result = get_highest_product_from_three(arr)
    print(result == answer)
    print(result)


if __name__ == '__main__':
    main()
