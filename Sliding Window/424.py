# 424. Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_w = 0
        max_length = 0
        counts = [0] * 26
        n = len(s)

        for r in range(n):
            ind_elem = ord(s[r]) - 65
            counts[ord(s[r]) - 65] += 1
            max_length = max(max_length, counts[ind_elem])
            while (r - l) + 1 - max_length > k:  # while (r - l) + 1 - max(counts) > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1
            
            max_w = max(max_w, (r-l)+1)
        return max_w  # O(n)