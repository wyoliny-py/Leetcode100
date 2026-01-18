# 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res = ''
        prev_index = -1
        for i in range(len(s)):
            for j in range(prev_index+1, len(t)):
                if t[j] == s[i]:
                    prev_index = j
                    res += t[j]
                    break
        if res == s:
            return True
        else:
            return False
print(Solution().isSubsequence("ab", "baab"))