"""
    Today's problem is available on Leetcode:
    https://leetcode.com/problems/sort-integers-by-the-power-value

    In this problem a formula for integers power value is defined.
    In a range given as an input, this power value must be calculated, then numbers sorted based on that,
    then the kth number returned.
"""


class Solution:
    def __init__(self):
        self.steps = {1: 0}

    def add_to_steps(self, numbers):
        last_step = self.steps[numbers.pop()]
        while numbers:
            n = numbers.pop()
            last_step += 1
            self.steps[n] = last_step

    def calculate_power_value(self, n: int) -> int:
        step = 0
        numbers_between = []

        while n != 1:
            numbers_between.append(n)
            if self.steps.get(n):
                step += self.steps.get(n)
                break

            step += 1
            if n % 2 == 0:
                n = n // 2
            else:
                n = n * 3 + 1

        if n == 1:
            numbers_between.append(n)
        self.add_to_steps(numbers_between)
        return step

    def get_kth(self, lo: int, hi: int, k: int) -> int:
        low_to_high_steps = {n: self.calculate_power_value(n)
                             for n in range(lo, hi+1)}
        low_to_high_steps = [k for k in dict(sorted(low_to_high_steps.items(), key=lambda n: n[1])).keys()]
        return low_to_high_steps[k - 1]


if __name__ == '__main__':
    solution = Solution()

    # example 1
    lo, hi, k = 1, 2, 2
    print(solution.get_kth(lo, hi, k))

    # example 2
    lo, hi, k = 12, 15, 2
    print(solution.get_kth(lo, hi, k))

    # example 3
    lo, hi, k = 7, 11, 4
    print(solution.get_kth(lo, hi, k))
