# 278. First Bad Version
# The isBadVersion API is already defined for you.
from random import randint
def isBadVersion(version: int) -> bool:
    return bool(randint(0, 1))  # for example
class Solution:
    def firstBadVersion(self, n: int) -> int:
        r = n
        l = 1
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l
        