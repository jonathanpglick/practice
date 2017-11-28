# -*- coding: utf-8 -*-
"""
Your company built an in-house calendar tool called HiCal. You want to add a
feature to see the times in a day when everyone is available.

To do this, you’ll need to know when any team is having a meeting. In HiCal,
a meeting is stored as tuples ↴ of integers (start_time, end_time). These
integers represent the number of 30-minute blocks past 9:00am.

Do not assume the meetings are in order. The meeting times are coming from
multiple teams.

Write a solution that's efficient even when we can't put a nice upper bound on
the numbers representing our time ranges. Here we've simplified our times down
to the number of 30-minute slots past 9:00 am. But we want the function to work
even for very large numbers, like Unix timestamps. In any case, the spirit of
the challenge is to merge meetings where start_time and end_time don't have an
upper bound.

@see https://www.interviewcake.com/question/python/merging-ranges
"""
from __future__ import unicode_literals


def merge_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    range_group = list(ranges[0])
    result = []
    for idx, r in enumerate(ranges):
        if r[0] > range_group[1]:
            result.append(tuple(range_group))
            range_group = list(r)
            continue

        if r[0] < range_group[0] and r[1] < range_group[1]:
            range_group[0] = r[0]
        elif r[0] < range_group[0] and r[1] > range_group[1]:
            range_group[0] = r[0]
            range_group[1] = r[1]
        elif r[0] > range_group[0] and r[1] > range_group[1]:
            range_group[1] = r[1]

    result.append(tuple(range_group))

    return result


def main():
    ranges = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    result = merge_ranges(ranges)
    expected =  [(0, 1), (3, 8), (9, 12)]
    print(result)
    print(result == expected)

if __name__ == '__main__':
    main()
