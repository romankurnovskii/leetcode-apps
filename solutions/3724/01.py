from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        res = float("inf")

        # nums2 has n+1 elements, so one element must come from an append operation
        # Try each index j in nums1 as the one to append
        for j in range(n):
            # Cost to make nums1[j] match both nums2[j] and nums2[-1]
            # We need: one copy becomes nums2[j], appended copy becomes nums2[-1]
            # The cost is |nums1[j] - nums2[j]| + |nums1[j] - nums2[-1]|
            append_cost = abs(nums1[j] - nums2[j]) + abs(nums1[j] - nums2[-1])

            # Cost to transform all other positions
            other_cost = 0
            for i in range(n):
                if i != j:
                    other_cost += abs(nums1[i] - nums2[i])

            total_cost = append_cost + other_cost
            res = min(res, total_cost)

        return res
