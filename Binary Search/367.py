# 367. Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # O(1) with no binary search
        # res = num ** 0.5
        # if int(res) == res:
        #     return True
        # else:
        #     return False
        
        # binary search O(log n)
        r = num
        l = 1
        while l <= r:
            mid = (l + r) // 2
            res = mid * mid
            if res == num:
                return True
            elif res < num:
                l = mid + 1
            elif res > num:
                r = mid - 1
        return False
