# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l <= r:
            flag1 = s[l].isalnum()
            flag2 = s[r].isalnum()
            if flag1 and flag2:
                if s[l].lower() != s[r].lower():
                    return False
            else:
                if flag1:
                    r -= 1
                if flag2:
                    l += 1
                continue
            l += 1
            r -= 1
        return True
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))