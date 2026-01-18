# 695. Max Area of Island
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_value = [0, 0]
        
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != 1:
                return
            else:
                max_value[1] += 1
                grid[i][j] = 0
                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i, j - 1)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i, j)
                    max_value[0] = max(max_value[0], max_value[1])
                    max_value[1] = 0
        
        return max_value[0]
    
    
    # Time Complexity: O(m*n)
	# Space Complexity: O(m*n)
	 