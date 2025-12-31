class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque

        max_deque = deque()  # Decreasing deque for max
        min_deque = deque()  # Increasing deque for min
        left = 0
        res = 0

        for right in range(len(nums)):
            # Maintain max deque (decreasing)
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)

            # Maintain min deque (increasing)
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # Shrink window if needed
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if max_deque[0] == left:
                    max_deque.popleft()
                if min_deque[0] == left:
                    min_deque.popleft()
                left += 1

            res = max(res, right - left + 1)

        return res
