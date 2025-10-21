## 167. Two Sum II - Input Array Is Sorted [Medium]

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

## Description
Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index₁]` and `numbers[index₂]` where `1 ≤ index₁ < index₂ ≤ numbers.length`.

Return *the indices of the two numbers, *`index₁`* and *`index₂`*, **added by one** as an integer array *`[index₁, index₂]`* of length 2.*

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

**Examples**

```text
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index₁ = 1, index₂ = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index₁ = 1, index₂ = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index₁ = 1, index₂ = 2. We return [1, 2].
```

**Constraints**
```text
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution
```

## Explanation

### Strategy
Let's restate the problem: You're given a sorted array of numbers and a target sum. You need to find two different numbers in the array that add up to the target, and return their 1-indexed positions.

This is a **two-pointer problem** that takes advantage of the fact that the array is already sorted.

**What is given?** A sorted array of integers and a target sum.

**What is being asked?** Find two numbers that add up to the target and return their 1-indexed positions.

**Constraints:** The array is sorted, there's exactly one solution, and you must use only constant extra space.

**Edge cases:** 
- The array has at least 2 elements (guaranteed by constraints)
- All numbers are within a reasonable range (-1000 to 1000)
- There's exactly one solution (no need to handle multiple solutions)

**High-level approach:**
Since the array is sorted, we can use two pointers - one at the beginning and one at the end. We can then move these pointers based on whether the current sum is too small or too large compared to the target.

Think of it like this: if you're looking for two numbers that add up to a target, and the array is sorted, you can start with the smallest and largest numbers. If their sum is too small, you need a larger number, so move the left pointer right. If their sum is too large, you need a smaller number, so move the right pointer left.

**Decomposition:**
1. **Initialize pointers**: Place one pointer at the start and one at the end
2. **Calculate current sum**: Add the numbers at both pointer positions
3. **Compare with target**: 
   - If sum equals target, we found our answer
   - If sum is too small, move left pointer right
   - If sum is too large, move right pointer left
4. **Return result**: Convert to 1-indexed format

**Brute force vs. optimized strategy:**
- **Brute force**: Check every possible pair of numbers. This takes O(n²) time.
- **Optimized**: Use two pointers and take advantage of the sorted order. This takes O(n) time.

### Steps
Let's walk through the solution step by step using the first example: `numbers = [2,7,11,15]`, `target = 9`

**Step 1: Initialize pointers**
- `left = 0` (points to the first element: 2)
- `right = 3` (points to the last element: 15)

**Step 2: Calculate current sum**
- Current sum = `numbers[left] + numbers[right] = 2 + 15 = 17`

**Step 3: Compare with target**
- `17 > 9` (target), so the sum is too large
- We need a smaller number, so move the right pointer left
- `right = 2` (now points to 11)

**Step 4: Calculate new sum**
- Current sum = `numbers[left] + numbers[right] = 2 + 11 = 13`

**Step 5: Compare with target**
- `13 > 9` (target), so the sum is still too large
- Move the right pointer left again
- `right = 1` (now points to 7)

**Step 6: Calculate new sum**
- Current sum = `numbers[left] + numbers[right] = 2 + 7 = 9`

**Step 7: Found the solution!**
- `9 == 9` (target), so we found our answer
- The numbers are at positions `left = 0` and `right = 1`
- Convert to 1-indexed: `[1, 2]`

**Why this works:**
Since the array is sorted, when we move the left pointer right, we get larger numbers. When we move the right pointer left, we get smaller numbers. This allows us to efficiently search for the target sum by adjusting our search space.

> **Note:** The key insight is that since the array is sorted, we can use the two-pointer technique to efficiently find the target sum. This is much more efficient than checking every possible pair.

**Time Complexity:** O(n) - we visit each element at most once  
**Space Complexity:** O(1) - we only use a constant amount of extra space for the pointers
