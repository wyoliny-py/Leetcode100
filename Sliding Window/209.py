# 209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        total = nums[0]
        n = len(nums)
        longest = 10000000000000000000

        for r in range(n):
            if total < target:
                total += nums[r]
            else:
                longest = min(longest, (r - l) + 1)
                l = r
                total = l
        
        return longest
print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))