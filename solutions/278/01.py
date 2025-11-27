# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        while left < right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                # Mid is bad, so first bad is at mid or before
                right = mid
            else:
                # Mid is good, so first bad is after mid
                left = mid + 1
        
        return left

