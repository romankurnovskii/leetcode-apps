class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            # Check if all elements are consecutive and sorted
            sorted_sub = sorted(subarray)
            is_consecutive = True
            
            for j in range(k - 1):
                if sorted_sub[j + 1] - sorted_sub[j] != 1:
                    is_consecutive = False
                    break
            
            if is_consecutive and subarray == sorted_sub:
                res.append(max(subarray))
            else:
                res.append(-1)
        
        return res

