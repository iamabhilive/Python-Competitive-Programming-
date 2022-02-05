# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, h = 1, n
        a = n
        while l <= h:
            mid = (l + h) // 2
            if isBadVersion(mid) == False:
                l = mid + 1
            elif isBadVersion(mid) == True:
                h = mid - 1
                a = mid
        return a
