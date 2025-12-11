from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        # Base cost to align all existing positions (before considering append)
        base = sum(abs(nums1[i] - nums2[i]) for i in range(n))
        last_target = nums2[-1]

        def triple_min_cost(a: int, b: int, c: int) -> int:
            # Minimal sum of absolute differences to a median point
            x, y, z = sorted((a, b, c))
            median = y
            return abs(a - median) + abs(b - median) + abs(c - median)

        res = float("inf")

        for j in range(n):
            # Remove the direct alignment cost for position j
            current = base - abs(nums1[j] - nums2[j])

            # Optimal adjustment for nums1[j] used twice (position j and appended)
            # We can adjust nums1[j] to a median of (nums1[j], nums2[j], last_target)
            adjust_cost = triple_min_cost(nums1[j], nums2[j], last_target)

            # Total = other positions + adjustment for j + append operation
            res = min(res, current + adjust_cost + 1)

        return res
