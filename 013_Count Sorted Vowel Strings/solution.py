"""
    Today's problem is available on Leetcode:
    https://leetcode.com/problems/count-sorted-vowel-strings/

    Problem is:
    Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u)
    and are lexicographically sorted.
    A string s is lexicographically sorted if for all valid i,
    s[i] is the same as or comes before s[i+1] in the alphabet.
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_strings_number = [[0] * len(vowels) for _ in range(n)]

        vowel_strings_number[0] = [1] * len(vowels)

        for i in range(1, n):
            vowel_strings_number[i][0] = (vowel_strings_number[i - 1][0] + vowel_strings_number[i - 1][1] +
                                          vowel_strings_number[i - 1][2] + vowel_strings_number[i - 1][3] +
                                          vowel_strings_number[i - 1][4])
            vowel_strings_number[i][1] = (vowel_strings_number[i - 1][1] + vowel_strings_number[i - 1][2] +
                                          vowel_strings_number[i - 1][3] + vowel_strings_number[i - 1][4])
            vowel_strings_number[i][2] = (vowel_strings_number[i - 1][2] + vowel_strings_number[i - 1][3] +
                                          vowel_strings_number[i - 1][4])
            vowel_strings_number[i][3] = vowel_strings_number[i - 1][3] + vowel_strings_number[i - 1][4]
            vowel_strings_number[i][4] = vowel_strings_number[i - 1][4]

        return sum(vowel_strings_number[-1])


if __name__ == '__main__':
    solution = Solution()

    for n in range(1, 11):
        print(f'Input: n = {n}')
        print(f'Output: {solution.countVowelStrings(n)}')
        print()
