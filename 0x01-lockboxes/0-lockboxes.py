#!/usr/bin/python3

"""
This is a simple module and it only has
one function called canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """Check if can unlock all the boxes

    Args:
        boxes (_type_): Boxes list

    Returns:
        bool: _description_
    """
    open_boxes = [0]
    boxes_count = len(boxes)
    keys = [0]

    while len(keys):
        new_keys = []
        for key in keys:
            new_keys.extend(open(boxes[key]))

        valid_keys = checkKeys(new_keys, open_boxes, boxes_count)
        keys = valid_keys
        open_boxes.extend(keys)

    return len(open_boxes) == boxes_count


def checkKeys(keys, open_boxes, boxes_count):
    """Check if provided keys are for valid or unopened boxes

    Args:
        keys (_type_): _description_
        open_boxes (_type_): _description_
        boxes_count (_type_): _description_

    Returns:
        _type_: _description_
    """
    valid_keys = []
    for key in keys:
        if key not in open_boxes and key < boxes_count:
            valid_keys.append(key)

    return valid_keys


def open(box):
    """Open a box

    Args:
        box (_type_): _description_

    Returns:
        _type_: _description_
    """
    return box
