from typing import List
import math


class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d[0], d[1]
        r1, r2 = r[0], r[1]

        # Binary search on total time T
        def can_complete(T):
            # Calculate available hours for each drone
            # Drone 1: T - floor(T/r1) hours available (subtract recharge hours)
            avail1 = T - (T // r1)
            avail2 = T - (T // r2)

            # Hours when both are recharging (unavailable)
            lcm_r = math.lcm(r1, r2)
            both_recharging = T // lcm_r

            # Shared available hours (when at least one is available)
            shared = T - both_recharging

            # Check if we can complete all deliveries
            # Each drone needs its deliveries, and they can't overlap in time
            # We need: avail1 >= d1 and avail2 >= d2, and total available >= d1 + d2
            return avail1 >= d1 and avail2 >= d2 and shared >= d1 + d2

        # Binary search
        left, right = 1, 10**18
        while left < right:
            mid = (left + right) // 2
            if can_complete(mid):
                right = mid
            else:
                left = mid + 1

        return left

