#!/usr/bin/env python

def search(list, key):
    """If the key is in the list return the position, -1 otherwise"""

    for i, word in enumerate(list):
        if word == key:
            return i
    return -1


def main():
    number = [i for i in range(45, 100)]
    position = search(number, 56)
    print(position)
