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
    pascal = [[1]]

    for i in range(1, n):
        prev_item = pascal[i - 1]
        new_item = [1]
        for i in range(len(prev_item)):
            if i == len(prev_item) - 1:
                new_item.append(prev_item[i])
            else:
                new_item.append(prev_item[i] + prev_item[i + 1])
        pascal.append(new_item)

    return pascal
