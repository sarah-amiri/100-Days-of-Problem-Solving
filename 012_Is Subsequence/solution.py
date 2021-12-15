"""
    Today's problem is available on Leetcode:
    https://leetcode.com/problems/is-subsequence/

    In this problem two strings are given. if first string is substring of
    the second string, it must return true. Otherwise false would be returned.
    I used to pointers to solve this problem.
"""


class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        m = len(s) - 1
        n = len(t) - 1
        while n >= m >= 0:
            if s[m] == t[n]:
                m -= 1
            n -= 1
        return m == -1


if __name__ == '__main__':
    solution = Solution()

    # example 1
    str1, str2 = 'abc', 'ahbgdc'
    print(f'Output: {solution.is_subsequence(str1, str2)}')

    # example 2
    str1, str2 = 'axc', 'ahbgdc'
    print(f'Output: {solution.is_subsequence(str1, str2)}')
