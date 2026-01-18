# 977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # return sorted([x ** 2 for x in nums]) Time: O(n log n)
        l, r = 0, len(nums) - 1
        answer = []
        while l <= r:
            l_mean = nums[l] ** 2
            r_mean = nums[r] ** 2

            if l_mean > r_mean:
                answer.append(l_mean)
                l += 1
            else:
                answer.append(r_mean)
                r -= 1
        answer.reverse()
        return answer  # O((n)
print(Solution().sortedSquares([-7,-3,2,3,11]))