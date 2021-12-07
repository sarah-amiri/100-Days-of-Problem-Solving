"""
    This problem is available on Codewars.
    You can see the complete problem here:
    https://www.codewars.com/kata/5a7778790136a132a00000c1

    The problem was asked to make binary of the digit until
    the sum of digits is a single digit.

    I write all of the functions myself and I think my get_digit_sum() function
    is not a good one. I could easily count number of digit '1' in the digit.

    This approach is a good, pythonic way:
    '''
        def single_digit(n):
            while n > 9:
                n = bin(n).count('1')
            return n
    '''
"""


class Solution:
    @staticmethod
    def make_binary(n):
        binary = 0
        while True:
            binary = binary * 10 + n % 2
            if n < 2:
                break
            n = n // 2
        return binary

    @staticmethod
    def get_digit_sum(n):
        sum = 0
        while True:
            sum += n % 10
            n = n // 10
            if n < 10:
                break
        return sum + n

    def single_digit(self, n):
        if n >= 10:
            while True:
                print(n)
                binary = self.make_binary(n)
                n = self.get_digit_sum(binary)
                if n < 10:
                    break
        return self.get_digit_sum(n)


if __name__ == '__main__':
    solution = Solution()
    text = 'Sum of binary digits is {}'

    # example 1
    n = 5665
    print(text.format(solution.single_digit(n)))

    # example 2
    n = 123456789
    print(text.format(solution.single_digit(n)))
