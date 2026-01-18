# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        # Brute Force
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # O(n)
        memo = {1:1, 2:2}
        def f(x):
            if x in memo:
                return memo[x]
            memo[x] = f(x-1) + f(x-2)
            return memo[x]
        return f(n)