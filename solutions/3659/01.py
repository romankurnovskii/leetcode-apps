class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        # If total elements is not divisible by k, impossible
        if n % k != 0:
            return False

        num_groups = n // k

        # Count frequency of each element
        from collections import Counter

        freq = Counter(nums)

        # Each element can appear at most num_groups times
        # (once per group, since groups must have distinct elements)
        for count in freq.values():
            if count > num_groups:
                return False

        return True
