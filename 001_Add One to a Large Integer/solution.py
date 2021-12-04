"""
    This problem is available on LeetCode.
    You can see the complete problem here:
    https://leetcode.com/problems/plus-one/

    The problem asked to add '1' to a large integer
    that is given as an integer array digits.
    I used two solutions for this problem.
"""

from typing import List


class Solution:
    def plus_one_solution_one(self, digits: List[int]) -> List[int]:
        integer_number = 0
        for digit in digits:
            integer_number = integer_number * 10 + digit
        integer_number += 1
        return [int(n) for n in str(integer_number)]

    def plus_one_solution_two(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        while index != -1 and digits[index] + 1 == 10:
            digits[index] = 0
            index -= 1

        if index == -1:
            digits.insert(0, 1)
        else:
            digits[index] += 1
        return digits


if __name__ == '__main__':
    solution = Solution()

    # example one
    digits = [1, 2, 3]
    print(solution.plus_one_solution_one(digits))
    print(solution.plus_one_solution_two(digits))

    # example two
    digits = [4, 3, 2, 1]
    print(solution.plus_one_solution_one(digits))
    print(solution.plus_one_solution_two(digits))

    # example three
    digits = [0]
    print(solution.plus_one_solution_one(digits))
    print(solution.plus_one_solution_two(digits))

    # example four
    digits = [9]
    print(solution.plus_one_solution_one(digits))
    print(solution.plus_one_solution_two(digits))
