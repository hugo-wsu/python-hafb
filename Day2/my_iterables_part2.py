#!/usr/bin/env python3
"""
Author : hvalle <me@wsu.com>
Date   : 8/10/2021
Purpose: Continue Comprehensions and iterables
"""


# --------------------------------------------------
def main():
    """Make your noise here"""

    # List Comprehensions:  [expr(item) for item in iterable]
    # Set Comprehensions:  {expr(item) for item in iterable}
    s = {i for i in range(10)}
    print(s)
    # Dict Comprehensions:  {key_expr:value_expr for item in iterable}
    d = {i: i*2 for i in range(10)}
    print(d)
    # Comprehensions: (item for item in iterable)
    g = (i for i in range(10))
    print(g)

    # Multiple If-Clauses
    points = []
    for x in range(5):
        for y in range(3):
            points.append((x, y))
    print(points)
    # Now use a comprehension:
    points = [(x, y) for x in range(5) for y in range(3)]
    print(points)
    # Version 1: Loops
    values = []
    for x in range(100):
        if x > 50:
            for y in range(100):
                if x-y != 0:
                    values.append(x/(x-y))
    print(values)
    # Comprehension
    values = [x/(x-y)
              for x in range(100) if x > 50
              for y in range(100) if x - y != 0]
    print(values)

    # Task: Nested Comprehension
    outer = []
    for x in range(10):
        inner = []
        for y in range(x):
            inner.append(y*3)
        outer.append(inner)
    print(outer)
    # 2D Comprehension
    outer = [[y*3 for y in range(x)] for x in range(10)]
    print(outer)
    #
    g = ((x, y) for x in range(5) for y in range(5))
    print(g)
    print(list(g))



# --------------------------------------------------
if __name__ == '__main__':
    main()
