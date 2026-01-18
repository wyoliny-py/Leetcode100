# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs = sorted(strs, key=len)
        res = ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return res
            res += strs[0][i]
        return res
        # O(n log n)
