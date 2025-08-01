class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Handle edge cases
        if len(nums) <= 2:
            return len(nums)

        # Initialize slow pointer (start from index 2)
        slow = 2

        # Iterate through the array with fast pointer
        for fast in range(2, len(nums)):
            # If current element is different from element two positions back
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        # Return the count of valid elements
        return slow
