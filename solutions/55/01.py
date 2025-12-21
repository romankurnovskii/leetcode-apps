from typing import List


def canJump(nums: List[int]) -> bool:
    max_reach = 0

    for i in range(len(nums)):
        # If we can't reach the current position, we can't reach the end
        if i > max_reach:
            return False

        max_reach = max(max_reach, i + nums[i])

    return True
