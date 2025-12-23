class Solution:
    def splitArray(self, nums: List[int]) -> int:
        """
        Find the minimum absolute difference between sums of a strictly
        increasing left subarray and a strictly decreasing right subarray.
        Return -1 if no valid split exists.
        """
        n = len(nums)

        # inc[i] = True if nums[0..i] is strictly increasing
        inc = [False] * n
        inc[0] = True
        for i in range(1, n):
            inc[i] = inc[i - 1] and nums[i - 1] < nums[i]

        # dec[i] = True if nums[i..n-1] is strictly decreasing
        dec = [False] * n
        dec[n - 1] = True
        for i in range(n - 2, -1, -1):
            dec[i] = dec[i + 1] and nums[i] > nums[i + 1]

        # prefix sums for O(1) range sum
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        ans = float("inf")
        valid = False
        # split after i (left: 0..i, right: i+1..n-1)
        for i in range(n - 1):
            if inc[i] and dec[i + 1]:
                left_sum = pref[i + 1]
                right_sum = pref[n] - pref[i + 1]
                ans = min(ans, abs(left_sum - right_sum))
                valid = True

        return ans if valid else -1
