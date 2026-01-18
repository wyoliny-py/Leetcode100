# 198. House Robber
class Solution:
    def rob(self, nums: list[int]) -> int:
        # Brute Force
        # def robbing(i):
        #     if i == 0:
        #         return nums[i]
        #     if i == 0 or i == 1:
        #         return max(nums[0], nums[1])
        #     return max(nums[i] + robbing(i-2), robbing(i-1))
        # return robbing(len(nums) - 1)

        # Memoization O(N)
        n = len(nums)
        if n == 1: return nums[0]
        memo = {0:nums[0], 1:max(nums[0], nums[1])}
        def robbing(i):
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + robbing(i-2), robbing(i-1))
            return memo[i]
        return robbing(n - 1)