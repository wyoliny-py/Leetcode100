# 1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        if len(word2) > len(word1):
            big = word2
            small = word1
        else:
            big = word1
            small = word2
        for i in range(len(small)):
            res += word1[i] + word2[i]

            
        return res + big[i+1:len(big)]