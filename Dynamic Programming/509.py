# 509. Fibonacci Number
class Solution:
    def fib(self, n: int) -> int:
        # DP: Constant Space
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        prev = 0
        cur = 1
        for i in range(2, n+1):
            prev, cur = cur, prev+cur

        return cur
        # Time: O(n)
        # Space: O(1)