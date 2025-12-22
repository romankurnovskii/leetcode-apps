class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # If all elements are already equal, no operations needed
        if len(set(nums)) == 1:
            return 0
        
        # Otherwise, we can apply AND operation on the entire array
        # This will make all elements equal to the AND of all elements
        return 1

