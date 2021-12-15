"""
    In this week, I decided to focus on dynamic programming and
    today's problem is about finding the 'largest sum contiguous sub array'.
    You can read more about this problem here:
    https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

   This problem is available on Leetcode:
    https://leetcode.com/problems/maximum-subarray/
"""


def find_max_sum_contiguous_sub_array(a, n):
    sum_max, current_max = a[0], a[0]

    for i in range(1, n):
        current_max = max(a[i], a[i] + current_max)
        sum_max = max(current_max, sum_max)

    return sum_max


if __name__ == '__main__':
    # example 1
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(f'The maximum sum contiguous sub array is {find_max_sum_contiguous_sub_array(arr, len(arr))}')

    # example 2
    arr = [1]
    print(f'The maximum sum contiguous sub array is {find_max_sum_contiguous_sub_array(arr, len(arr))}')

    arr = [5, 4, -1, 7, 8]
    print(f'The maximum sum contiguous sub array is {find_max_sum_contiguous_sub_array(arr, len(arr))}')
