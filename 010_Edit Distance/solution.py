"""
    In this week, I decided to focus on dynamic programming and
    today's problem is 'Edit Distance'.
    You can read more about this problem here:
    https://www.geeksforgeeks.org/edit-distance-dp-5/

    I solved this problem as one of the questions in the course 'Must Do Coding Questions':
    https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1/
"""


class Solution:
    def edit_distance(self, s1, s2, n1, n2):
        d = [[0 for i in range(n1 + 1)] for j in range(n2 + 1)]

        for i in range(n2 + 1):
            for j in range(n1 + 1):
                if i == 0:
                    d[i][j] = j
                elif j == 0:
                    d[i][j] = i
                elif s2[i-1] == s1[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = 1 + min(d[i][j-1],
                                      d[i-1][j],
                                      d[i-1][j-1])
        return d[n2][n1]


if __name__ == '__main__':
    solution = Solution()

    # example 1
    str1 = 'sunday'
    str2 = 'saturday'
    print(solution.edit_distance(str1, str2, len(str1), len(str2)))

    # example 2
    str1 = 'geek'
    str2 = 'gesek'
    print(solution.edit_distance(str1, str2, len(str1), len(str2)))

    # example 3
    str1 = 'gfg'
    str2 = 'gfg'
    print(solution.edit_distance(str1, str2, len(str1), len(str2)))
