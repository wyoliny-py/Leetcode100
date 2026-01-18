# 200. Number of Islands
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != '1':
                return
            else:
                grid[i][j] = 0
                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i, j - 1)
        num_islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        return num_islands
        # Time: O(n * m)
        # Space: O(n * m)