class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        # Sort the array
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        
        # Sum of k largest elements (last k elements)
        sum_largest = sum(sorted_nums[n - k:])
        
        # Sum of k smallest elements (first k elements)
        sum_smallest = sum(sorted_nums[:k])
        
        # Return absolute difference
        res = abs(sum_largest - sum_smallest)
        return res
