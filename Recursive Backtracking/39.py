# 39. Combination Sum
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res, sol = [], []
        n = len(candidates)
        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return
            
            if cur_sum > target or i == n:
                return
            
            backtrack(i+1, cur_sum)

            sol.append(candidates[i])
            backtrack(i, cur_sum + candidates[i])
            sol.pop()
        
        backtrack(0, 0)
        return res
    
        # O(n ** t)

        