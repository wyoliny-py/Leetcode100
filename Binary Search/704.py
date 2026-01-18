# 704. Binary Search
class Solution:
    def search(self, nums: list[int], target: int) -> int:
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
        if nums[mid] < target:
            return mid + 1
        else:
            return mid
print(Solution().search([-1,0,3,5,9,12], 9))