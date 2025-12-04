class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark numbers that appear by negating the value at index (num - 1)
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        
        # Collect indices where value is still positive (these numbers are missing)
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        
        return res

