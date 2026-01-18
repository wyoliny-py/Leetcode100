# 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: list[int]) -> int:
        # return min(nums) O(n)

        # O (log n)
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left