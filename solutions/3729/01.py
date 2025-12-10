class Solution:
    def numGoodSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Build prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # For distinct subarrays, we need to track unique sequences
        # A subarray is good if (prefix[j] - prefix[i]) % k == 0
        # This means prefix[j] % k == prefix[i] % k

        # Count distinct good subarrays
        # For sorted array, distinct subarrays are determined by their value sequence
        seen = set()
        res = 0

        # Use a map to track prefix mod k and their positions
        from collections import defaultdict

        mod_map = defaultdict(list)
        mod_map[0].append(0)  # prefix[0] = 0

        for i in range(1, n + 1):
            mod_val = prefix[i] % k
            mod_map[mod_val].append(i)

        # For each mod value, count distinct subarrays
        # A subarray from i to j-1 has sum = prefix[j] - prefix[i]
        # For distinct subarrays in sorted array:
        # - Single value runs: count if (length * value) % k == 0
        # - Multi-value subarrays: each unique sequence is distinct

        # Count single-value subarrays
        i = 0
        while i < n:
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
            length = j - i
            # Check if this run contributes to good subarrays
            if (length * nums[i]) % k == 0:
                # Count distinct subarrays in this run
                # All subarrays of same value are distinct if they have different lengths
                for L in range(1, length + 1):
                    if (L * nums[i]) % k == 0:
                        res += 1
            i = j

        # Count multi-value subarrays
        # For each mod value, count pairs (i, j) where prefix[j] % k == prefix[i] % k
        # But we need distinct sequences
        for mod_val, positions in mod_map.items():
            if len(positions) < 2:
                continue

            # For sorted array, a subarray is uniquely identified by its start and end
            # But we need to ensure the sequence is distinct
            # Since array is sorted, each (start, end) pair gives a unique sequence
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    start = positions[i]
                    end = positions[j]
                    # Subarray from start to end-1
                    if end > start:
                        # Check if this is a distinct sequence
                        # In sorted array, each (start, end) is unique
                        res += 1

        return res
