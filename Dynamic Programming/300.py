# 300. Longest Increasing Subsequence
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # My Unworking Brute Force
        # max_length = float('-inf')
        # n = len(nums)
        # for i in range(n):
        #     length = 1
        #     cur = nums[i]
        #     prev_cur = nums[i]
        #     for j in range(i+1, n):
        #         if cur < nums[j]:
        #             prev_cur = cur
        #             cur = nums[j]
        #             length += 1
        #         elif prev_cur < nums[j]:
        #             cur = nums[j]
        #     max_length = max(length, max_length)
        # return max_length

        # Bottom Up DP (Tabulation)
	    # Time: O(n^2)
	    # Space: O(n)
        n = len(nums)
        dp = [1] * n
        answer = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    answer = max(answer, dp[i])
        return answer