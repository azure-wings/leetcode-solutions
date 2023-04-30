# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1

        lo, hi = 1, n

        while lo <= hi:
            mid = (lo + hi) // 2

            if isBadVersion(mid) == True:
                if isBadVersion(mid - 1) == False:
                    return mid
                else:
                    hi = mid - 1
            else:
                lo = mid + 1

        return lo