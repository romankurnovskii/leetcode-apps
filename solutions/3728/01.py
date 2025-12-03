class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        
        # Compute prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + capacity[i]
        
        res = 0
        
        # For each right endpoint r, find valid left endpoints l
        # Condition: capacity[l] == capacity[r] and
        # capacity[l] == sum(capacity[l+1:r])
        # Which means: capacity[l] == prefix[r] - prefix[l+1]
        # Rearranging: prefix[l+1] == prefix[r] - capacity[r]
        
        # Use a map: (value, prefix_sum) -> count
        from collections import defaultdict
        freq_map = defaultdict(int)
        
        # Process from left to right
        for r in range(n):
            # For each r, we want to find l such that:
            # capacity[l] == capacity[r] and prefix[l+1] == prefix[r] - capacity[r]
            target_prefix = prefix[r] - capacity[r]
            key = (capacity[r], target_prefix)
            res += freq_map[key]
            
            # Update map: add (capacity[r], prefix[r]) for future matches
            # Note: we use prefix[r] (not prefix[r+1]) because when we check at position r,
            # we're looking for l where prefix[l+1] matches
            update_key = (capacity[r], prefix[r])
            freq_map[update_key] += 1
        
        return res

