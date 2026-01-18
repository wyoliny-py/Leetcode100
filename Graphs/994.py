# 994. Rotting Oranges
from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        m, n = len(grid), len(grid[0])
        q = deque()
        num_fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    q.append((i, j))
                elif grid[i][j] == FRESH:
                    num_fresh += 1
        
        if num_fresh == 0:
            return 0
        
        num_minutes = -1
        while q:
            q_size = len(q)
            num_minutes += 1
            for _ in range(q_size):
                i, j = q.popleft()
                for i_off, j_off in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                    if 0 <= i_off < m and 0 <= j_off < n and grid[i_off][j_off] == FRESH:
                        num_fresh -= 1
                        grid[i_off][j_off] = ROTTEN
                        q.append((i_off, j_off))
        if num_fresh == 0:
            return num_minutes
        else:
            return -1
        
        # O(m * n)
