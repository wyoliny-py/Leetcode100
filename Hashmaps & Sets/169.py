# 169. Majority Element
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Мое решение (неэффективно) O(n)
        # hash = {}
        # n = len(nums)
        # for elem in nums:
        #     if elem not in hash:
        #         hash[elem] = 1
        #     else:
        #         hash[elem] += 1
        #         if hash[elem] >= n / 2:
        #             return elem
    
        ans = -1
        counter = 0
        for elem in nums:
            if counter == 0:
                ans = elem

            if ans != elem:
                counter -= 1
            else:
                counter += 1
        return ans
print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))