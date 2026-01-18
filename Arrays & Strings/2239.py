# 2239. Find Closest Number to Zero
class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        # Brute Force

        # nums = sorted(nums, key=abs)
        # if nums[0] < 0 and abs(nums[0]) in set(nums):
        #     return abs(nums[0])
        # else:
        #     return nums[0]


        closest = nums[0]
        h = {closest}
        for i in range(1, len(nums)):
            h.add(nums[i])
            if abs(nums[i]) < abs(closest):
                closest = nums[i]
        if abs(closest) in h:
            return abs(closest)
        else:
            return closest
        
        # Time: O(n)
        # Space: O(n)