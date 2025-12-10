from typing import List


class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        res = 0

        # Build prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + capacity[i]

        # For each subarray [l, r] where length >= 3
        # Check if capacity[l] == capacity[r] == sum of elements between them
        for l in range(n):
            for r in range(l + 2, n):  # length >= 3
                if capacity[l] == capacity[r]:
                    # Sum of elements strictly between l and r
                    interior_sum = prefix[r] - prefix[l + 1]
                    if capacity[l] == interior_sum:
                        res += 1

        return res
