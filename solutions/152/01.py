class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Handle edge case
        if not nums:
            return 0

        # Initialize variables
        max_product = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Store previous values to avoid overwriting
            prev_max = curr_max
            prev_min = curr_min

            # Calculate new maximum and minimum products
            curr_max = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            curr_min = min(nums[i], nums[i] * prev_max, nums[i] * prev_min)

            # Update the overall maximum product
            max_product = max(max_product, curr_max)

        # Return the maximum product
        return max_product
