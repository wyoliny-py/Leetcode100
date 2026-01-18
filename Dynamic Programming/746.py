# 746. Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Brute Force
        # n = len(cost)
        # def min_cost(i):
        #     if i < 2:
        #         return 0
        #     return min(cost[i-1] + min_cost(i-1), cost[i-2] + min_cost(i-2))
        # return min_cost(n)
    
        # O(n)
        n = len(cost)
        memo = {0:0, 1:0}
        def min_cost(i):
            if i < 2:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = min(cost[i-1] + min_cost(i-1), cost[i-2] + min_cost(i-2))
            return memo[i]
        return min_cost(n)