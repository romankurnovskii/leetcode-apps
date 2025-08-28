def minOperations(nums):
    """
    Find the minimum number of operations to make the array continuous.
    
    Args:
        nums: List[int] - Array of integers
        
    Returns:
        int - Minimum number of operations needed
    """
    # Handle edge case
    if len(nums) <= 1:
        return 0
    
    # Sort the array to work with ordered elements
    nums.sort()
    
    # Remove duplicates to work with unique elements
    unique_nums = []
    for i, num in enumerate(nums):
        if i == 0 or num != nums[i-1]:
            unique_nums.append(num)
    
    n = len(unique_nums)
    min_operations = float('inf')
    
    # Try different window sizes
    for i in range(n):
        # For each starting position, find the longest window that can be made continuous
        left = unique_nums[i]
        
        # Binary search for the rightmost element that can be part of a continuous sequence
        # starting from left
        right = left + len(nums) - 1
        
        # Find how many elements in unique_nums fall within [left, right]
        # This gives us the size of the window that can be made continuous
        count = 0
        for j in range(i, n):
            if unique_nums[j] <= right:
                count += 1
            else:
                break
        
        # Calculate operations needed
        # We need to change (len(nums) - count) elements
        operations = len(nums) - count
        min_operations = min(min_operations, operations)
    
    return min_operations
