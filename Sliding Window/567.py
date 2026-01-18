# 567. Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O(n)
        l = 0
        r = len(s1) - 1
        n = len(s2)

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(min(len(s1), len(s2))):
            s2_counts[ord(s2[i]) - 97] += 1
            s1_counts[ord(s1[i]) - 97] += 1
        while r < n:
            if s2_counts == s1_counts:
                return True
            else:
                el = s2_counts[ord(s2[l]) - 97]
                s2_counts[ord(s2[l]) - 97] =  el - 1 if el - 1 >= 0 else 0
                l += 1
                r += 1
                if r >= n:
                    break
                s2_counts[ord(s2[r]) - 97] += 1
        return False


print(Solution().checkInclusion("ab", "eidbaooo"))