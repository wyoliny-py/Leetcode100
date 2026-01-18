# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stk = ['']
        hash = {'(':')', '{':'}', '[':']', '':''}
        for elem in s:
            if stk[-1] in hash:
                if hash[stk[-1]] == elem and stk:
                    stk.pop()
                else:
                    stk.append(elem)
            else:
                return False
        return True if len(stk) == 1 else False
print(Solution().isValid("(])"))