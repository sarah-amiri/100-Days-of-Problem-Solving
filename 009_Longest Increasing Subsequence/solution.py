"""
    In this week, I decided to focus on dynamic programming and
    today's problem is to find the longest increasing subsequence (LIS)
    in an array of integers.
    You can read more about this problem here:
    https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

    I solved this problem as one of the questions in the course 'Must Do Coding Questions':
    https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1/
"""


class Solution:
    def longest_increasing_subsequence(self, a, n):
        lis_a = [1 for _ in range(n)]

        for i in range(1, n):
            for j in range(0, i):
                if a[i] > a[j] and lis_a[i] < lis_a[j] + 1:
                    lis_a[i] = lis_a[j] + 1

        return max(lis_a)


if __name__ == '__main__':
    solution = Solution()

    # example 1
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(solution.longest_increasing_subsequence(arr, len(arr)))

    # example 2
    arr = [5, 8, 3, 7, 9, 1]
    print(solution.longest_increasing_subsequence(arr, len(arr)))

    # example 3
    arr = [3, 10, 2, 11]
    print(solution.longest_increasing_subsequence(arr, len(arr)))
