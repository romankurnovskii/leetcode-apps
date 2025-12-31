from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix = {0: -1}  # prefix_sum -> last index
        prefix_sum = 0

        # best[i] = minimum length of subarray ending before or at i with sum = target
        best = [float("inf")] * n
        res = float("inf")
        min_prev = float("inf")

        for i in range(n):
            prefix_sum += arr[i]

            # Check if there's a subarray ending at i with sum = target
            if prefix_sum - target in prefix:
                length = i - prefix[prefix_sum - target]
                min_prev = min(min_prev, length)
                best[i] = min_prev

                # Check if there's a previous non-overlapping subarray
                prev_idx = prefix[prefix_sum - target]
                if prev_idx >= 0 and best[prev_idx] != float("inf"):
                    res = min(res, best[prev_idx] + length)

            prefix[prefix_sum] = i

        return res if res != float("inf") else -1
