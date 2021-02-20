#!/usr/bin/env python
def search(list, key):
    """Returns position of  the word in the list, -1 otherwise"""
    left = 0
    right = len(list) - 1
    while left <= right:

        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1


num = [i for i in range(12, 100)]
w = search(num, 23)
print(w)
