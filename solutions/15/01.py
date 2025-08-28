def threeSum(nums):
    """
    Find all unique triplets in the array which gives the sum of zero.
    
    Args:
        nums: List[int] - Array of integers
        
    Returns:
        List[List[int]] - List of unique triplets that sum to zero
    """
    # Handle edge cases
    if len(nums) < 3:
        return []
    
    # Sort the array to enable two-pointer technique
    nums.sort()
    result = []
    
    # Iterate through each element as the first number in the triplet
    for i in range(len(nums) - 2):
        # Skip duplicates to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Use two pointers to find pairs that sum to -nums[i]
        left = i + 1
        right = len(nums) - 1
        target = -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                # Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers
                left += 1
                right -= 1
                
            elif current_sum < target:
                # Sum is too small, move left pointer right
                left += 1
            else:
                # Sum is too large, move right pointer left
                right -= 1
    
    return result
