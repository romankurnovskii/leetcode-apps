class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        # Work with absolute values and sort
        arr = sorted(abs(x) for x in nums)
        
        res = 0
        j = 1
        
        # For each i, find the rightmost j such that arr[j] <= 2 * arr[i]
        for i in range(len(arr)):
            # Ensure j > i
            if j <= i:
                j = i + 1
            # Advance j while arr[j] <= 2 * arr[i]
            while j < len(arr) and arr[j] <= 2 * arr[i]:
                j += 1
            # Count pairs: all indices between i+1 and j-1 form valid pairs with i
            # j points to first element > 2*arr[i], so valid pairs are from i+1 to j-1
            res += max(0, j - i - 1)

