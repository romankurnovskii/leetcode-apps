class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        prefix = [0] * (n + 1)

        # Build prefix sum
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        res = 1

        # For each possible target value (each element in sorted array)
        for i in range(n):
            target = nums[i]

            # Binary search for the longest subarray ending at i
            # where we can make all elements equal to target
            left, right = 0, i + 1

            while left < right:
                mid = (left + right) // 2
                start = i - mid + 1

                # Cost to make elements from start to i equal to target
                # Sum of (target - nums[j]) for j from start to i
                cost = target * mid - (prefix[i + 1] - prefix[start])

                if cost <= k:
                    res = max(res, mid)
                    left = mid + 1
                else:
                    right = mid

        return res
