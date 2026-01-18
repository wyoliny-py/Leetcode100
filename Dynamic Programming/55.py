# 55. Jump Game
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Recursive Solution (Brut Force)
        # Time: O(max(nums) ^ n)
        # Space: O(n)
        # n = len(nums)
        # def jumping(i):

        #     if i == n - 1:
        #         return True
        #     for jump in range(1, nums[i]+1):
        #         if jumping(i+jump):
        #             return True
            
        #     return False
        # return jumping(0)
    
        # Memoization
        # Time: O(n ^ 2)
        # Space: O(n)
        # n = len(nums)
        # memo = {n - 1: True}
        # def jumping(i):
        #     if i in memo:
        #         return memo[i]
            
        #     for jump in range(1, nums[i]+1):
        #         if jumping(i+jump):
        #             memo[i] = True
        #             return True
        #     memo[i] = False
        #     return False
        # return jumping(0)
    
        # Greedy -- Start at end
        # Time: O(n)
	    # Space: O(1)
        n = len(nums)
        goal = n - 1
        for i in range(n-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0