class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        res = 0
        stack = []

        for r, val in enumerate(nums):
            # Pop elements that are <= current (they can form bowls with current)
            while stack and nums[stack[-1]] <= val:
                l = stack.pop()
                if r - l + 1 >= 3:
                    res += 1

            # Check if current element forms a bowl with stack top
            if stack and r - stack[-1] + 1 >= 3:
                res += 1

            stack.append(r)

        return res
