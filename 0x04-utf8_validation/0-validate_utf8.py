#!/usr/bin/python3
"""
This is a simple module and it only has
one function called validUTF8(data)
"""

from typing import List


def validUTF8(data: List) -> bool:
    """ determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List): _description_

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False
    """
    n_bytes = 0

    for num in data:
        if n_bytes == 0:
            if (num >> 5) == 0b110:
                n_bytes = 1
            elif (num >> 4) == 0b1110:
                n_bytes = 2
            elif (num >> 3) == 0b11110:
                n_bytes = 3
            elif (num >> 7):
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0
