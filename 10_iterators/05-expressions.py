__doc__ = """Generator expressions are high performance, 
memory efficient generalization of list comprehensions and generators.
"""


# 1. Implement range generator
def range_gen(start, end):
    """
    Range generator
    """
    current = start
    while current < end:
        yield current
        current += 1


# 2. Generator expressions uses range generator
def sum_square(start, end):
    """
    Sum of squares
    """
    return sum(x*x for x in range_gen(start, end))


print(sum_square(0, 10))

