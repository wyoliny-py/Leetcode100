# 62. Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Brute Force
        # def path(i, j):
        #     if i == 0 and j == 0:
        #         return 1
        #     if i < 0 or j < 0 or i == m or j == n:
        #         return 0
        #     return path(i-1, j) + path(i, j-1)
        # return path(m-1, n-1)


        # Memoization
        # O(n)
        memo = {(0, 0): 1}
        def path(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            memo[(i, j)] = path(i-1, j) + path(i, j-1)
            return memo[(i, j)]
        return path(m-1, n-1)