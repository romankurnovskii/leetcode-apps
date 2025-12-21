from typing import List
from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Group indices by value
        indices_map = defaultdict(list)
        for i, num in enumerate(nums):
            indices_map[num].append(i)

        min_distance = float("inf")

        # For each value that appears at least 3 times
        for num, indices in indices_map.items():
            if len(indices) < 3:
                continue

            # Sort indices (they should already be sorted, but just to be safe)
            indices.sort()

            # Check every three consecutive indices
            # For indices p < q < r, the distance is 2 * (r - p)
            # We want to minimize r - p, so we check consecutive triplets
            for i in range(len(indices) - 2):
                p = indices[i]
                q = indices[i + 1]
                r = indices[i + 2]

                # Distance formula: abs(p - q) + abs(q - r) + abs(r - p)
                # Since p < q < r, this simplifies to: (q - p) + (r - q) + (r - p) = 2 * (r - p)
                distance = 2 * (r - p)
                min_distance = min(min_distance, distance)

        return min_distance if min_distance != float("inf") else -1
