"""
    This problem is available on Codewars.
    You can see the complete problem here:
    https://www.codewars.com/kata/5818d00a559ff57a2f000082

    The problem was asked to find the nth pell sequence.
    Pell sequence is defined by:
    P(0) = 0, P(1) = 1, P(n) = 2 * P(n-1) + P(n-2)

    I used the recursive solution and array solution. As you may
    using recursive is not efficient (But you can use cache and make it more efficient).

    I also like this approach by 'BitemNet':
    ```
    class Pell(object):
        @staticmethod
        def get(n):
            x, y = 0, 1
            for i in range(n):
                x, y = y, x + 2 * y
            return x
    ```
"""


class Solution:
    def pell_number_recursive(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return 2 * self.pell_number_recursive(n-1) + self.pell_number_recursive(n-2)

    def pell_number_array(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            pell_sequence = [0, 1]
            for index in range(2, n+1):
                next_pell_number = 2 * pell_sequence[index-1] + pell_sequence[index-2]
                pell_sequence.append(next_pell_number)
            return pell_sequence[-1]


if __name__ == '__main__':
    solution = Solution()

    row_format = '{:<5} {:<40} {:<40}'
    print(row_format.format('n', 'using array', 'using recursive'))

    for n in [1, 10, 20, 100]:
        print(row_format.format(n,
                                solution.pell_number_array(n),
                                solution.pell_number_recursive(n)))
