from typing import List


class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        res = 0

        # State variables
        curr_xor = 0
        balance = 0  # Acts as: Count(Odd) - Count(Even)

        # Map stores (xor_val, balance) -> first_index_seen
        # Initialize with (0,0): -1 to handle valid subarrays starting at index 0
        seen = {(0, 0): -1}

        for i, num in enumerate(nums):
            # 1. Update running XOR
            curr_xor ^= num

            # 2. Update balance (+1 for Odd, -1 for Even)
            if num % 2 != 0:
                balance += 1
            else:
                balance -= 1

            state = (curr_xor, balance)

            # 3. Check if we've seen this state before
            if state in seen:
                # The subarray between the first occurrence and now is valid
                length = i - seen[state]
                res = max(res, length)
            else:
                # Store the first occurrence of this state
                seen[state] = i

        return res
