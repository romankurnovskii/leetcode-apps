def summaryRanges(nums):
    """
    Create a summary of ranges from a sorted array of unique integers.
    
    Args:
        nums: List[int] - Sorted array of unique integers
        
    Returns:
        List[str] - List of range strings
    """
    # Handle edge case
    if not nums:
        return []
    
    result = []
    start = 0
    
    # Traverse array looking for consecutive sequences
    for i in range(1, len(nums)):
        # Check if current number is consecutive to previous
        if nums[i] != nums[i-1] + 1:
            # Break in sequence, format the range
            if start == i - 1:
                # Single number
                result.append(str(nums[start]))
            else:
                # Range of numbers
                result.append(f"{nums[start]}->{nums[i-1]}")
            
            # Start new range
            start = i
    
    # Handle the final range
    if start == len(nums) - 1:
        # Single number
        result.append(str(nums[start]))
    else:
        # Range of numbers
        result.append(f"{nums[start]}->{nums[-1]}")
    
    return result
