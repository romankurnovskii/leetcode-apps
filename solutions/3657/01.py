class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        # Try all triplets (i, j, k) where i < j < k
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    value = (nums[i] - nums[j]) * nums[k]
                    res = max(res, value)

        return res
