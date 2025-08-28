def longestConsecutive(nums):
    """
    Find the length of the longest consecutive elements sequence.
    
    Args:
        nums: List[int] - Array of integers
        
    Returns:
        int - Length of the longest consecutive sequence
    """
    # Handle edge case
    if not nums:
        return 0
    
    # Convert array to hash set for O(1) lookup
    num_set = set(nums)
    max_length = 0
    
    # For each number, check if it's the start of a consecutive sequence
    for num in num_set:
        # A number is a starting point if num - 1 is NOT in the set
        if num - 1 not in num_set:
            current_length = 1
            current_num = num
            
            # Expand the sequence by checking consecutive numbers
            while current_num + 1 in num_set:
                current_length += 1
                current_num += 1
            
            # Update maximum length if current sequence is longer
            max_length = max(max_length, current_length)
    
    return max_length
