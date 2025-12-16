class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum_largest = sum(nums[-k:])
        sum_smallest = sum(nums[:k])
        return abs(sum_largest - sum_smallest)

