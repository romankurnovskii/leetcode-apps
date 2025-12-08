class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Check if any element is less than k (impossible case)
        if any(num < k for num in nums):
            return -1
        
        # Count distinct numbers greater than k
        distinct_greater = set()
        for num in nums:
            if num > k:
                distinct_greater.add(num)
        
        res = len(distinct_greater)
        return res
