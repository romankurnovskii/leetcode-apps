class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        # If k == 0, every element qualifies
        if k == 0:
            return len(nums)
        
        # Sort the array
        nums.sort()
        n = len(nums)
        
        # Find the threshold: the k-th largest element
        # Index of k-th largest is n - k
        threshold = nums[n - k]
        
        # Count all elements smaller than the threshold
        res = 0
        for x in nums:
            if x < threshold:
                res += 1
        
        return res

