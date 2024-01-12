#!/usr/bin/python3
""" The method that determines if all the boxes can be opened. """


def canUnlockAll(boxes):
    """
        A key with the same number as a box opens that box.
        There can be keys that do not have boxes.
        first box boxes[0] is unlocked.
    """
    m = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))

    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= m or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return m == len(seen_boxes)
