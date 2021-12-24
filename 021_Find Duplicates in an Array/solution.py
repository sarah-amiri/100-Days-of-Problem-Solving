"""
    This problem is available on LeetCode:
    https://leetcode.com/problems/find-all-duplicates-in-an-array/

    Given an integer array of size n with integers between 1 to n,
    every integer may appear once or twice and it was asked to
    return a list of integers that appeared twice.
"""
from typing import List


class Solution:
    def find_duplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        duplicates = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                duplicates.append(nums[i])
                i += 1
        return duplicates


if __name__ == '__main__':
    solution = Solution()

    numbers_array = [
        [4, 3, 2, 7, 8, 2, 3, 1],
        [1, 1, 2],
        []
    ]

    for i, numbers in enumerate(numbers_array):
        print(f'# example {i+1}')
        print(f'Input: {numbers}')
        print(f'Output: {solution.find_duplicates(numbers)}')
