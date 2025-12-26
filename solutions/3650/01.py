class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Remove duplicates and sort
        sorted_nums = sorted(set(nums))
        n = len(nums)
        unique_count = len(sorted_nums)

        # We need a continuous array of length n
        # The array should have unique elements and max - min = n - 1
        min_ops = n - 1  # Worst case: replace all but one

        # Use sliding window to find the longest continuous subarray
        # that can be extended to form a continuous array of length n
        for i in range(unique_count):
            # Try to form continuous array starting from sorted_nums[i]
            target_max = sorted_nums[i] + n - 1

            # Binary search to find how many elements are in range [sorted_nums[i], target_max]
            left, right = i, unique_count - 1
            while left < right:
                mid = (left + right + 1) // 2
                if sorted_nums[mid] <= target_max:
                    left = mid
                else:
                    right = mid - 1

            # Number of elements already in the range
            elements_in_range = left - i + 1

            # Operations needed = total elements - elements in range
            min_ops = min(min_ops, n - elements_in_range)

        return min_ops
