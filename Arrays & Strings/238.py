# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l_mult = 1
        r_mult = 1
        l = [0] * len(nums)
        r = [0] * len(nums)
        for i in range(len(nums)):
            j = -i -1
            l[i] = l_mult
            r[i] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
        ans = []
        for i in range(len(nums)):
            ans.append(l[i] * r[-i -1])
        return ans
    
        # Time: O(n)
        # Space: O(n)


print(Solution().productExceptSelf([1,2,3,4]))