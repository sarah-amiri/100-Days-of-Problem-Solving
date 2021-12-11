"""
    In this week, I decided to focus on dynamic programming and
    today's problem is 0-1 Knapsack Problem.
    You can read more about this classic problem here:
    https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

    I solved this problem as one of the questions in the course 'Must Do Coding Questions':
    https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1/
"""


class Solution:
    def knapsack(self, W, wt, val, n):
        K = [[0 for i in range(W+1)] for j in range(n+1)]

        for i in range(n+1):
            for j in range(W+1):
                if i == 0 or j == 0:
                    K[i][j] = 0
                elif wt[i-1] > W:
                    K[i][j] = K[i-1][j]
                else:
                    K[i][j] = max(
                        val[i-1] + K[i-1][j-wt[i-1]],
                        K[i-1][j]
                    )
        return K[n][W]


if __name__ == '__main__':
    solution = Solution()

    # example 1
    n = 3
    W = 6
    wt = [1, 2, 3]
    val = [10, 15, 40]
    print(solution.knapsack(W, wt, val, n))

    # example 2
    n = 3
    W = 4
    wt = [4, 5, 1]
    val = [1, 2, 3]
    print(solution.knapsack(W, wt, val, n))

    # example 3
    n = 3
    W = 3
    wt = [4, 5, 6]
    val = [1, 2, 3]
    print(solution.knapsack(W, wt, val, n))
