class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        from collections import Counter

        # Find the dominant element
        count = Counter(nums)
        dominant = max(count, key=count.get)
        total_freq = count[dominant]

        # Track frequency in left subarray
        left_freq = 0

        for i in range(len(nums) - 1):
            if nums[i] == dominant:
                left_freq += 1

            right_freq = total_freq - left_freq
            left_len = i + 1
            right_len = len(nums) - left_len

            # Check if dominant in both subarrays
            if left_freq * 2 > left_len and right_freq * 2 > right_len:
                return i

        return -1
