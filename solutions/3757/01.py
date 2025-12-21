from typing import List


class Solution:
    def countEffective(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Step 1: Calculate total OR - all "light bulbs" that are on
        full = 0
        for v in nums:
            full |= v

        if full == 0:
            return 0

        # Step 2: Find which bits are set in the total OR
        # These are the "light bulbs" we care about
        bits = [i for i in range(31) if (full >> i) & 1]
        B = len(bits)

        # Create a mapping from bit position to index in our compressed representation
        idx = {bits[i]: i for i in range(B)}

        # Step 3: Map each number to a bitmask showing which bits it contributes to
        # freq[mask] = count of numbers that contribute exactly the bits in mask
        freq = [0] * (1 << B)
        for v in nums:
            m = 0
            for b in bits:
                if (v >> b) & 1:
                    m |= 1 << idx[b]
            freq[m] += 1

        # Step 4: SOS DP - count how many numbers are submasks of each mask
        # dp[mask] = count of numbers that contribute only bits contained in mask
        dp = freq[:]
        for i in range(B):
            for mask in range(1 << B):
                if mask & (1 << i):
                    dp[mask] += dp[mask ^ (1 << i)]

        # Precompute powers of 2
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        # Step 5: Inclusion-Exclusion to count effective subsequences
        # A subsequence is effective if it removes all "guardians" of at least one bit
        # We count subsequences that keep bits in mask s (removing bits in comp)
        # and subtract/add based on how many bits are removed
        res = 0
        full_mask = (1 << B) - 1

        # Iterate over all non-empty subsets of bits to keep
        for s in range(1, 1 << B):
            # comp = bits we're removing (complement of s)
            comp = full_mask ^ s
            # count_zero = how many numbers contribute only to bits in comp
            # These are the numbers we can freely include/exclude
            count_zero = dp[comp]
            term = pow2[count_zero]

            # Inclusion-exclusion: sign depends on popcount(s) (bits kept)
            # This follows from the inclusion-exclusion formula structure
            if s.bit_count() & 1:
                res = (res + term) % MOD
            else:
                res = (res - term) % MOD

        return res % MOD
