# 1. Two Sum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i
        
        for i in range(len(nums)):
            y = target - nums[i]
            if y in h and h[y] != i:
                return [i, h[y]]
            
        # Time: O(n)
        # Space: O(1)