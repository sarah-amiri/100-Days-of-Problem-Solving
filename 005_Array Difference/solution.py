"""
    This problem is available on Codewars.
    You can see the complete problem here:
    https://www.codewars.com/kata/523f5d21c841566fde000009

    The problem was asked to calculate difference between two arrays.
"""


def array_diff(a, b):
    for item in b:
        while a.count(item):
            a.remove(item)
    return a


if __name__ == '__main__':
    print(array_diff([1, 2], [2]))
    print(array_diff([1, 2, 2, 2, 3], [2]))
