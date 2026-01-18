# 49. Group Anagrams
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_dict = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key not in anagrams_dict:
                anagrams_dict[key] = [word]
            else:
                anagrams_dict[key].append(word)
        return list(anagrams_dict.values())
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))