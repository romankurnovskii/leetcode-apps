class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        res = []
        
        # Precompute validity check: lastMatchIdx[i] stores the rightmost index
        # starting from i such that all elements have the same modulo k
        last_match_idx = [0] * n
        last_match_idx[n - 1] = n - 1
        
        for i in range(n - 2, -1, -1):
            if nums[i] % k == nums[i + 1] % k:
                last_match_idx[i] = last_match_idx[i + 1]
            else:
                last_match_idx[i] = i
        
        # Process each query
        for l, r in queries:
            # Check if query is valid (all elements have same modulo k)
            if last_match_idx[l] < r:
                res.append(-1)
                continue
            
            # Extract subarray and normalize by dividing by k
            subarray = [nums[i] // k for i in range(l, r + 1)]
            
            # Sort to find median
            subarray.sort()
            median = subarray[len(subarray) // 2]
            
            # Calculate minimum operations: sum of absolute differences from median
            operations = sum(abs(x - median) for x in subarray)
            res.append(operations)
        
        return res

