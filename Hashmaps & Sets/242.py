# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_1 = {}
        hash_2 = {}
        for char in s:
            if char not in hash_1:
                hash_1[char] = 1
            else:
                hash_1[char] += 1
            
        for char in t:
            if char not in hash_2:
                hash_2[char] = 1
            else:
                hash_2[char] += 1
        
        return hash_1 == hash_2