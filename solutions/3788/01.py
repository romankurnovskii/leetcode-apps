class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)

        # Precompute suffix minimums: suffixMin[i] = min of nums[i] to nums[n-1]
        suffixMin = [0] * n
        suffixMin[n - 1] = nums[n - 1]
        for i in range(n - 2, 0, -1):
            suffixMin[i] = min(suffixMin[i + 1], nums[i])

        # Calculate prefix sum and find maximum score
        res = nums[0] - suffixMin[1]  # Initial score at index 0
        prefixSum = nums[0]

        for i in range(1, n - 1):
            prefixSum += nums[i]
            # Score at split index i: prefixSum - suffixMin[i+1]
            res = max(res, prefixSum - suffixMin[i + 1])

        return res
