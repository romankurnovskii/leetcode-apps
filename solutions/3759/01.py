from typing import List


class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        # Sort the array
        sorted_nums = sorted(nums)
        n = len(sorted_nums)

        res = 0

        # For each distinct value, count how many elements are strictly greater
        i = 0
        while i < n:
            # Count occurrences of current value
            count = 1
            while i + count < n and sorted_nums[i] == sorted_nums[i + count]:
                count += 1

            # Find the first index with value strictly greater than current
            # Use binary search to find upper bound
            left, right = i + count, n
            while left < right:
                mid = (left + right) // 2
                if sorted_nums[mid] > sorted_nums[i]:
                    right = mid
                else:
                    left = mid + 1

            # Number of elements strictly greater
            greater_count = n - left

            # If at least k elements are greater, add count to result
            if greater_count >= k:
                res += count

            i += count

        return res
