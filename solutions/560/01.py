class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Prefix sum approach
        prefix_sum = {0: 1}  # sum 0 appears once (empty subarray)
        current_sum = 0
        res = 0

        for num in nums:
            current_sum += num
            # If (current_sum - k) exists in prefix_sum, we found a subarray
            if current_sum - k in prefix_sum:
                res += prefix_sum[current_sum - k]

            # Update prefix_sum count
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return res
