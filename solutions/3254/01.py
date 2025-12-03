class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            # Check if all elements are consecutive and sorted
            expected = list(range(subarray[0], subarray[0] + k))
            if subarray == expected:
                res.append(max(subarray))
            else:
                res.append(-1)
        
        return res
