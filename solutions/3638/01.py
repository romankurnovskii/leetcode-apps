class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = [0] * n  # cnt[j] stores count of 132 triplets with j as the middle
        res = 0

        for j in range(n):
            prev_small = 0  # Count of numbers smaller than nums[j] before j
            for i in range(j):
                if nums[j] > nums[i]:
                    # nums[i] < nums[j], so (i, j) can form part of 1324
                    prev_small += 1
                    res += cnt[i]  # Add count of 132 triplets ending at i
                elif nums[j] < nums[i]:
                    # nums[j] < nums[i], so j can be the '3' in 132 pattern for i
                    cnt[i] += prev_small

        return res
