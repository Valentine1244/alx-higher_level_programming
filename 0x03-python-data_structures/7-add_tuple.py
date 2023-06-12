#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If the tuples are smaller than 2, add 0 for each missing integer
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))

    # Add the first elements and the second elements of the tuples
    first_element = tuple_a[0] + tuple_b[0]
    second_element = tuple_a[1] + tuple_b[1]

    # Return the result as a tuple
    return (first_element, second_element)
