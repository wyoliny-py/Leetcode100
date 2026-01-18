# 771. Jewels and Stones
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash = dict()
        for char in stones:
            if char in hash:
                hash[char] += 1
            else:
                hash[char] = 1
        total = 0
        for k in jewels:
            if k in hash:
                total += hash[k]
        return total
print(Solution().numJewelsInStones("aA", "aAAbbbb"))