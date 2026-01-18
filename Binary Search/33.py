# 33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        n = len(nums)
        r = n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid


        min_ind = l
        if min_ind == 0:
            l, r = 0, n - 1
        elif nums[min_ind - 1] >= target and nums[0] <= target:
            l = 0
            r = min_ind - 1
        else:
            l = min_ind
            r = n - 1

        while l <= r:
            mid = (l + r) // 2  
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: 
                l = mid + 1  
            else: 
                r = mid - 1  
        return -1
    # O(log n)