class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        # For each j, count how many i < j have nums[i] == nums[j] * 2
        # and how many k > j have nums[k] == nums[j] * 2
        res = 0

        # Count frequencies before current position
        freq_before = {}
        # Count frequencies after current position
        freq_after = {}

        # Initialize freq_after with all elements
        for num in nums:
            freq_after[num] = freq_after.get(num, 0) + 1

        # Process each j
        for j in range(n):
            # Remove current element from freq_after
            freq_after[nums[j]] -= 1
            if freq_after[nums[j]] == 0:
                del freq_after[nums[j]]

            # Calculate target value: nums[j] * 2
            target = nums[j] * 2

            # Count i < j with nums[i] == target
            count_before = freq_before.get(target, 0)

            # Count k > j with nums[k] == target
            count_after = freq_after.get(target, 0)

            # Add to result
            res = (res + count_before * count_after) % MOD

            # Add current element to freq_before
            freq_before[nums[j]] = freq_before.get(nums[j], 0) + 1

        return res
