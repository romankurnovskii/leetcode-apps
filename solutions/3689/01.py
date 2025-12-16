class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # The hint says to choose the whole subarray k times
        # Value of whole subarray = max(nums) - min(nums)
        max_val = max(nums)
        min_val = min(nums)
        return (max_val - min_val) * k

