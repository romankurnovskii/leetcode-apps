from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Use deque to maintain indices of elements in decreasing order
        dq = deque()
        res = []

        for i in range(len(nums)):
            # Remove indices outside the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove indices whose corresponding values are smaller than current
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # If we've processed at least k elements, add max to result
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
