class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        # A subarray is beautiful if its XOR is 0
        # Use prefix XOR and hash map
        prefix_xor = 0
        count = {0: 1}  # Initialize with 0 XOR (empty prefix)
        res = 0

        for num in nums:
            prefix_xor ^= num
            # If we've seen this prefix_xor before, the subarray between
            # those two positions has XOR 0 (beautiful)
            res += count.get(prefix_xor, 0)
            count[prefix_xor] = count.get(prefix_xor, 0) + 1

        return res
