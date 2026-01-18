# 1189. Maximum Number of Balloons
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash = {}
        for char in text:
            if char not in hash:
                hash[char] = 1
            else:
                hash[char] += 1
        total_min = 10 ** 5
        for char in "balon":
            if char not in hash:
                return 0
            if char == "l" or char == 'o':
                if hash[char] < 2:
                    return 0
                total_min = min(total_min, hash[char] // 2)
            else:
                total_min = min(total_min, hash[char])
        return total_min