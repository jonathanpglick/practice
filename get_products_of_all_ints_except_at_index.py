# -*- coding: utf-8 -*-
"""
You have a list of integers, and for each index you want to find the product of
every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list 
of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Do not use division in your solution.

@see https://www.interviewcake.com/question/python/product-of-other-numbers
"""
from __future__ import unicode_literals
from functools import partial

def get_products_of_all_ints_except_at_index_On2(arr):

    def get_product_of_all_except_index(arr, idx):
        slice_before = arr[:idx]
        slice_after = arr[idx+1:]
        to_multiply = slice_before + slice_after
        return reduce(lambda x, y: x*y, to_multiply)

    return map(partial(get_product_of_all_except_index, arr), range(0, len(arr)))

def get_products_of_all_ints_except_at_index_On(arr):
    results = [None] * len(arr)

    # Step through forwards and figure out all the before values.
    arr_len = len(arr)
    product_before = 1
    for idx, val in enumerate(arr):
        results[idx] = product_before
        product_before = product_before * val

    # Step through backwards and figure out the after values.
    product_after = 1
    for idx, val in enumerate(arr):
        rev_idx = arr_len - 1 - idx
        rev_val = arr[rev_idx]

        if rev_idx == arr_len - 1:
            product_after = product_after
        else:
            product_after = product_after * arr[rev_idx + 1]

        results[rev_idx] = results[rev_idx] * product_after

    return results

# get_products_of_all_ints_except_at_index = get_products_of_all_ints_except_at_index_On2
get_products_of_all_ints_except_at_index = get_products_of_all_ints_except_at_index_On

def main():
    arr = [1, 7, 3, 4]
    answer = [84, 12, 28, 21]
    result = get_products_of_all_ints_except_at_index(arr)
    print(result == answer)
    print(result)

if __name__ == '__main__':
    main()
