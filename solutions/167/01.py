def twoSum(numbers, target):
    """
    Find two numbers in the sorted array that add up to the target.
    
    Args:
        numbers: List[int] - Sorted array of integers (1-indexed)
        target: int - Target sum to find
        
    Returns:
        List[int] - 1-indexed positions of the two numbers that sum to target
    """
    # Initialize two pointers
    left = 0
    right = len(numbers) - 1
    
    # Use two-pointer technique since array is sorted
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            # Found the solution, return 1-indexed positions
            return [left + 1, right + 1]
        elif current_sum < target:
            # Sum is too small, move left pointer right to get larger numbers
            left += 1
        else:
            # Sum is too large, move right pointer left to get smaller numbers
            right -= 1
    
    # This line should never be reached since there's exactly one solution
    return []
