# 383. Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = dict()
        for char in ransomNote:
            if char in hash:
                hash[char] += 1
            else:
                hash[char] = 1
        for char in magazine:
            if char in hash:
                if hash[char] != 0:
                    hash[char] -= 1
        for k in hash.keys():
            if hash[k] != 0:
                return False
        return True
print(Solution().canConstruct("aa", "aab"))