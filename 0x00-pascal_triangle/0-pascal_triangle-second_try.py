#!/usr/bin/python3
""" returns a list of lists of integers representing the Pascals triangle of n
    """


def pascal_triangle(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n <= 0:
        return []
    pascal = []

    for i in range(n):
        if len(pascal) == 0:
            new_item = generate_new_item()
        else:
            new_item = generate_new_item(pascal[i - 1])
        pascal.append(new_item)

    return pascal


def generate_new_item(prev=[], new=[]):
    if len(prev) == 0:
        return [1]

    if len(new) == 0:
        new.append(prev[0])
        return generate_new_item(prev, new)

    if len(prev) == 1:
        new.append(prev[0])
        return new

    new.append(prev[0] + prev[1])
    prev.pop(0)

    return generate_new_item(prev, new)


print(pascal_triangle(3))
