# 11. Container With Most Water
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        maxA = 0
        while l <= r:
            maxA = max(maxA, (r - l) * min(height[r], height[l]))
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return maxA
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))