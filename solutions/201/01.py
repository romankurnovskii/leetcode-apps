class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # Find the common prefix of left and right
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        # Shift back to get the common prefix
        return left << shift
