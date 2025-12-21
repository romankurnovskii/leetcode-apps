class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        # Sort the array
        nums.sort()

        # Sum of k largest elements (last k elements)
        sum_largest = sum(nums[-k:])

        # Sum of k smallest elements (first k elements)
        sum_smallest = sum(nums[:k])

        # Return absolute difference
        return abs(sum_largest - sum_smallest)
