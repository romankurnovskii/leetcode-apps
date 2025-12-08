class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # We need to construct an array where:
        # 1. nums[i+1] > nums[i]
        # 2. AND of all elements = x
        # 3. Minimize nums[n-1]

        # The idea: merge x with (n-1) by keeping x's bits and filling others with (n-1)'s bits
        res = x
        v = n - 1
        bit_pos = 0

        while v > 0:
            # Find a position where x has 0
            while (res >> bit_pos) & 1:
                bit_pos += 1

            # Set that bit if v has 1
            if v & 1:
                res |= 1 << bit_pos

            v >>= 1
            bit_pos += 1

        return res
