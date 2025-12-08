## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to sort an array based on the "binary reflection" of each number. The binary reflection is obtained by reversing the binary digits (ignoring leading zeros) and interpreting the result as a decimal number.

**1.1 Constraints & Complexity:**
- Input size: `1 <= nums.length <= 100`, `1 <= nums[i] <= 10^9`
- **Time Complexity:** O(n log n) where n is the length of nums, due to sorting
- **Space Complexity:** O(n) for the sorted result
- **Edge Case:** If two numbers have the same binary reflection, the smaller original number should appear first

**1.2 High-level approach:**
We compute the binary reflection for each number, then sort the array using the reflection as the primary key and the original value as the secondary key.

![Binary reflection visualization](https://assets.leetcode.com/static_assets/others/binary-reflection.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Compute all reflections, sort, which is what we do - this is already optimal
- **Optimized Strategy:** Use Python's built-in sort with a custom key function, achieving O(n log n) time
- **Emphasize the optimization:** Using a tuple key (reflection, original) allows efficient sorting with tie-breaking

**1.4 Decomposition:**
1. Define a function to compute binary reflection: convert to binary, reverse, convert back to decimal
2. Sort the array using binary reflection as primary key
3. If two numbers have the same reflection, use original value as secondary key
4. Return the sorted array

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `nums = [4,5,4]`
- We need to compute binary reflections for each number

**2.2 Start Processing:**
We compute binary reflections for each number.

**2.3 Trace Walkthrough:**

| Original | Binary | Reversed Binary | Reflection | Sort Key |
|----------|--------|-----------------|------------|----------|
| 4 | 100 | 001 | 1 | (1, 4) |
| 5 | 101 | 101 | 5 | (5, 5) |
| 4 | 100 | 001 | 1 | (1, 4) |

**2.4 Increment and Loop:**
After computing all reflections, we sort by (reflection, original): (1,4), (1,4), (5,5).

**2.5 Return Result:**
The sorted array is `[4, 4, 5]` based on reflections 1, 1, 5, with original values used for tie-breaking.
