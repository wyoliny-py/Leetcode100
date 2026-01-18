# 228. Summary Ranges
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # nums -- unigue and sorted
        ans_list = []
        ind_start = 0
        for i in range(len(nums)):
            if i + 1 == len(nums):
                if ind_start == i:
                    ans_list.append(str(nums[i]))
                else:
                    res = f'{nums[ind_start]}->{nums[i]}'
                    ans_list.append(res)
            else:
                if nums[i+1] - nums[i] != 1:
                    if ind_start != i:
                        res = f'{nums[ind_start]}->{nums[i]}'
                        ans_list.append(res)
                        ind_start = i+1
                    else:
                        ans_list.append(str(nums[i]))
                        ind_start = i+1
        return ans_list
    
        # Time: O(n)
        # Space: O(n)
print(Solution().summaryRanges([0,2,3,4,6,8,9]))