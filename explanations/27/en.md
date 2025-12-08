## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to remove all occurrences of a specific value from an array in-place, meaning we modify the original array without using extra space. The order of elements can be changed, and we only need to ensure the first k elements contain all non-target values.

**1.1 Constraints & Complexity:**
- Input size: `0 <= nums.length <= 100`, `0 <= nums[i] <= 50`, `0 <= val <= 100`
- **Time Complexity:** O(n) where n is the length of the array - we visit each element exactly once
- **Space Complexity:** O(1) - we modify the array in-place without using extra space
- **Edge Case:** If the array is empty or contains no elements equal to val, we return the original length

**1.2 High-level approach:**
We use a two-pointer technique where one pointer scans through the array to find valid elements, and another pointer tracks where to place them. This allows us to "remove" elements by overwriting them with valid elements.

![Two pointers moving through array](https://assets.leetcode.com/static_assets/others/two-pointers.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Create a new array, copy all non-target elements to it, then copy back. This requires O(n) extra space.
- **Optimized Strategy:** Use two pointers to overwrite elements in-place. This requires O(1) extra space and is more efficient.
- **Why it's better:** We avoid creating a new array, saving memory and making the solution more efficient.

**1.4 Decomposition:**
1. Initialize a slow pointer at position 0 to track where valid elements should be placed
2. Use a fast pointer to iterate through all elements in the array
3. For each element, check if it's not equal to the target value
4. If valid, copy it to the slow pointer position and advance the slow pointer
5. Return the slow pointer value as the count of valid elements

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `nums = [3,2,2,3]`, `val = 3`
- Initialize `slow = 0` (points to next position for valid elements)
- Initialize `fast = 0` (scans through the array)

**2.2 Start Checking:**
We begin iterating through the array with the fast pointer.

**2.3 Trace Walkthrough:**

| Step | fast | nums[fast] | nums[fast] == val? | Action | nums after | slow |
|------|------|------------|-------------------|--------|------------|------|
| Initial | 0 | 3 | Yes | Skip, increment fast | [3,2,2,3] | 0 |
| 1 | 1 | 2 | No | Copy to nums[0], increment both | [2,2,2,3] | 1 |
| 2 | 2 | 2 | No | Copy to nums[1], increment both | [2,2,2,3] | 2 |
| 3 | 3 | 3 | Yes | Skip, increment fast | [2,2,2,3] | 2 |
| End | 4 | - | - | Loop ends | [2,2,2,3] | 2 |

**2.4 Increment and Loop:**
After each iteration, we increment the fast pointer. If we found a valid element, we also increment the slow pointer.

**2.5 Return Result:**
Return `slow = 2`, which represents the number of elements not equal to val. The first 2 elements `[2,2]` are the valid elements.
