class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        """
        For each index, find the maximum value reachable via jumps:
        - Forward only to strictly smaller
        - Backward only to strictly larger
        This partitions the array into components where min suffix to the right
        is >= max prefix to the left. Each component's max is answer for indices inside.
        """
        n = len(nums)
        prefix_max = [0] * n
        suffix_min = [0] * n

        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        res = [0] * n
        start = 0
        for i in range(n - 1):
            if prefix_max[i] <= suffix_min[i + 1]:
                # component [start, i]
                comp_max = max(nums[start : i + 1])
                for idx in range(start, i + 1):
                    res[idx] = comp_max
                start = i + 1

        # last component
        comp_max = max(nums[start:])
        for idx in range(start, n):
            res[idx] = comp_max

        return res
