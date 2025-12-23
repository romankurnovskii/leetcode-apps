class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Maximum product of two numbers with disjoint set bits.
        Bitmask DP: best[mask] = largest number whose bits are subset of mask.
        """
        MAX_BITS = 20  # nums[i] <= 1e6
        FULL = (1 << MAX_BITS) - 1

        best = [0] * (1 << MAX_BITS)
        for x in nums:
            mask = x
            best[mask] = max(best[mask], x)

        # Subset DP: propagate maxima to supermasks
        for b in range(MAX_BITS):
            for mask in range(1 << MAX_BITS):
                if mask & (1 << b):
                    best[mask] = max(best[mask], best[mask ^ (1 << b)])

        ans = 0
        for x in nums:
            mask = x
            comp = FULL ^ mask  # masks disjoint with mask
            partner = best[comp]
            ans = max(ans, x * partner)

        return ans
