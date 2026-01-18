# 215. Kth Largest Element in an Array
import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Brute Force
        # return sorted(nums, reverse=True)[k-1]
        n = len(nums)
        for i in range(n):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)
        # O(n)
        