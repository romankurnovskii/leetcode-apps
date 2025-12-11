from typing import List
from collections import defaultdict


class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        # Build prefix sum array: prefix[i] = sum of capacity[0:i]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + capacity[i]

        res = 0
        # Map: (value, prefix_sum) -> count of indices with this value and prefix sum
        # For a stable subarray [l, r]:
        # - capacity[l] == capacity[r]
        # - capacity[l] == prefix[r] - prefix[l+1]
        # Rearranging: prefix[l+1] == prefix[r] - capacity[r]
        # So we need to find l where capacity[l] == capacity[r] and prefix[l+1] == prefix[r] - capacity[r]
        count_map = defaultdict(int)

        for r in range(n):
            # For each r, we want to count valid l where:
            # - l < r - 1 (at least 3 elements: l, l+1, ..., r)
            # - capacity[l] == capacity[r]
            # - prefix[l+1] == prefix[r] - capacity[r]

            # Add the newest possible left index (r - 2) to the map before counting
            # This ensures l < r - 1 (subarray length at least 3)
            if r >= 2:
                l = r - 2
                count_map[(capacity[l], prefix[l + 1])] += 1

            # Calculate the required prefix sum for a valid l
            required_prefix = prefix[r] - capacity[r]

            # Count how many previous indices l satisfy:
            # capacity[l] == capacity[r] and prefix[l+1] == required_prefix
            res += count_map.get((capacity[r], required_prefix), 0)

        return res
