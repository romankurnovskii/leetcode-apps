# 189. Rotate Array

**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/rotate-array/

## Problem Description

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

**Example 1:**
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**
```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

**Follow up:**
- Try to come up with as many solutions as you can. There are at least **three** different ways to solve this problem.
- Could you do it in-place with `O(1)` extra space?

## Explanation

### Strategy

This is an **array rotation problem** that requires shifting elements to the right by `k` positions. The key insight is that rotating by `k` positions is equivalent to moving the last `k` elements to the front.

**Key observations:**
- Rotating by `k` positions moves the last `k` elements to the front
- If `k` is larger than the array length, we can use modulo to reduce it
- We can solve this using a three-step reversal approach
- The reversal approach works in-place with O(1) extra space

**High-level approach:**
1. **Normalize k**: Use `k % len(nums)` to handle cases where `k` is larger than array length
2. **Use three reversals**: 
   - Reverse the entire array
   - Reverse the first `k` elements
   - Reverse the remaining elements
3. **Result**: This gives us the rotated array

### Steps

Let's break down the solution step by step:

**Step 1: Normalize the rotation amount**
- Calculate `k = k % len(nums)` to handle cases where `k` exceeds array length
- If `k` is 0, no rotation is needed

**Step 2: Reverse the entire array**
- This moves the last `k` elements to the front (but in reverse order)

**Step 3: Reverse the first k elements**
- This corrects the order of the elements that were moved to the front

**Step 4: Reverse the remaining elements**
- This corrects the order of the elements that were shifted back

**Example walkthrough:**
Let's trace through the first example:

```
nums = [1,2,3,4,5,6,7], k = 3

Step 1: Normalize k
k = 3 % 7 = 3

Step 2: Reverse entire array
[1,2,3,4,5,6,7] → [7,6,5,4,3,2,1]

Step 3: Reverse first k elements (first 3)
[7,6,5,4,3,2,1] → [5,6,7,4,3,2,1]

Step 4: Reverse remaining elements (last 4)
[5,6,7,4,3,2,1] → [5,6,7,1,2,3,4]

Result: [5,6,7,1,2,3,4]
```

> **Note:** The three-reversal approach is elegant because it works in-place and has O(n) time complexity. The key insight is that reversing parts of the array in the right order gives us the desired rotation.

### Solution

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Normalize k
        
        if k == 0:
            return
        
        # Reverse the entire array
        self.reverse(nums, 0, n - 1)
        
        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        
        # Reverse the remaining elements
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        """Helper function to reverse a portion of the array"""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
```

**Time Complexity:** O(n) - we visit each element a constant number of times  
**Space Complexity:** O(1) - we modify the array in-place without extra space 