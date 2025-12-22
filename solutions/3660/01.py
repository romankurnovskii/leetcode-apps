class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        # Find connected components using prefix max and suffix min
        # A "cut" happens where all values to the left are <= all values to the right
        prefix_max = [0] * n
        suffix_min = [0] * n
        
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])
        
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])
        
        # Find all cuts (positions where we can't jump across)
        cuts = []
        for i in range(n - 1):
            if prefix_max[i] <= suffix_min[i + 1]:
                cuts.append(i)
        
        # For each position, find which component it belongs to
        # and the maximum value in that component
        component_max = {}
        
        start = 0
        for cut in cuts:
            # Component from start to cut (inclusive)
            max_val = max(nums[start:cut + 1])
            for i in range(start, cut + 1):
                component_max[i] = max_val
            start = cut + 1
        
        # Last component
        if start < n:
            max_val = max(nums[start:])
            for i in range(start, n):
                component_max[i] = max_val
        
        # Build result
        for i in range(n):
            res[i] = component_max[i]
        
        return res

