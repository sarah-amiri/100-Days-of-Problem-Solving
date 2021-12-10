"""
    This problem is available on Geeks for Geeks.
    It is a part of 'Must Do Coding Questions' course and y
    ou can see the complete problem here:
    https://practice.geeksforgeeks.org/problems/count-number-of-hops-1587115620/1/

    I wanted to practice dynamic programming so I chose an easy one in this field.
    This question was asked to count in how many ways a frog can reach to the top
    while it jumps 1, 2 or 3 steps every time.
"""


def get_number_of_hops(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        n0, n1, n2 = 1, 1, 2
        for i in range(3, n+1):
            n0, n1, n2 = n1, n2, n0 + n1 + n2
        return n2


if __name__ == '__main__':
    for i in range(1, 101):
        print(f'Number of hops for {i} is {get_number_of_hops(i)}')
