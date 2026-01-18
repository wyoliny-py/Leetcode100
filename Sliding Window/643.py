class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i]
        max_sum = cur_sum
        n = len(nums)


        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i - k]

            max_sum = max(max_sum, cur_sum)

        return max_sum / k  # O(n)