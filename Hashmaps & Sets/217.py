# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash = set(nums)
        if len(hash) == len(nums):
            return False
        else:
            return True
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))