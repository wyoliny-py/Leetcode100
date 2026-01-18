# 35. Search Insert Position
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        r = n - 1
        l = 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        