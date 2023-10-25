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
    current_value = data.pop(0)
    if current_value > 255:
        return False
    if len(data):
        return True and validUTF8(data)

    return True
