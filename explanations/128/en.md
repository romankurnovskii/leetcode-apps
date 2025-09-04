## 128. Longest Consecutive Sequence [Medium]

https://leetcode.com/problems/longest-consecutive-sequence

## Description
Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

You must write an algorithm that runs in `O(n)` time.

**Examples**

```tex
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3
```

**Constraints**
```tex
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
```

## Explanation

### Strategy
Let's restate the problem: You're given an unsorted array of integers, and you need to find the length of the longest sequence of consecutive integers. The challenge is to do this in O(n) time, which means we can't sort the array (as sorting takes O(n log n) time).

This is a **hash table problem** that requires finding sequences of consecutive numbers efficiently by using the properties of consecutive sequences.

**What is given?** An unsorted array of integers that can be very large (up to 100,000 elements).

**What is being asked?** Find the length of the longest sequence of consecutive integers.

**Constraints:** The array can be up to 100,000 elements long, with values ranging from -10⁹ to 10⁹.

**Edge cases:** 
- Empty array
- Array with single element
- Array with all identical elements
- Array with no consecutive sequences

**High-level approach:**
The solution involves using a hash set to quickly check if numbers exist, then for each number, expanding in both directions to find the complete consecutive sequence.

**Decomposition:**
1. **Convert array to hash set**: For O(1) lookup time
2. **Find sequence starting points**: Look for numbers that are the start of a consecutive sequence
3. **Expand sequences**: For each starting point, expand in both directions to find the complete sequence
4. **Track maximum length**: Keep track of the longest sequence found

**Brute force vs. optimized strategy:**
- **Brute force**: Sort the array and find consecutive sequences. This takes O(n log n) time.
- **Optimized**: Use hash set and expand sequences from starting points. This takes O(n) time.

### Steps
Let's walk through the solution step by step using the first example: `nums = [100,4,200,1,3,2]`

**Step 1: Convert array to hash set**
- `nums = [100,4,200,1,3,2]`
- `num_set = {100, 4, 200, 1, 3, 2}`

**Step 2: Find sequence starting points**
- For each number, check if it's the start of a consecutive sequence
- A number is a starting point if `num - 1` is NOT in the set
- Starting points: `[100, 200, 1]` (because 99, 199, and 0 are not in the set)

**Step 3: Expand sequences from starting points**
- **Starting point 100**: 
  - Check if 101 exists: No
  - Sequence length: 1
- **Starting point 200**: 
  - Check if 201 exists: No
  - Sequence length: 1
- **Starting point 1**: 
  - Check if 2 exists: Yes
  - Check if 3 exists: Yes
  - Check if 4 exists: Yes
  - Check if 5 exists: No
  - Sequence: [1, 2, 3, 4]
  - Sequence length: 4

**Step 4: Track maximum length**
- Maximum sequence length found: 4
- Result: 4

**Why this works:**
By identifying starting points (numbers that don't have a predecessor in the set), we ensure that we only expand each sequence once. This gives us O(n) time complexity because:
1. We visit each number at most twice (once when checking if it's a starting point, once when expanding sequences)
2. Each number is part of at most one sequence
3. The total work is bounded by O(n)

> **Note:** The key insight is identifying starting points of consecutive sequences and expanding from there. This avoids redundant work and ensures O(n) time complexity.

**Time Complexity:** O(n) - we visit each number at most twice  
**Space Complexity:** O(n) - we need to store the hash set
