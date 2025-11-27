## Explanation

### Strategy (The "Why")

Given an integer array `nums`, we need to find all unique triplets `[nums[i], nums[j], nums[k]]` such that $i \neq j$, $i \neq k$, $j \neq k$, and $nums[i] + nums[j] + nums[k] == 0$.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be between $3$ and $3000$.
- **Value Range:** Array elements are between $-10^5$ and $10^5$.
- **Time Complexity:** $O(n^2)$ - We sort the array in $O(n \log n)$, then for each element, we use two pointers which takes $O(n)$ time. Overall $O(n^2)$.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space (not counting the output array). The sorting is done in-place.
- **Edge Case:** If there are no triplets that sum to 0, return an empty list. We must avoid duplicate triplets.

**1.2 High-level approach:**

The goal is to find all unique triplets that sum to zero.

![3Sum](https://assets.leetcode.com/uploads/2020/01/15/3sum.jpg)

We sort the array first, then for each element, use two pointers to find pairs that sum to the negative of that element. This avoids duplicates naturally.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all triplets, checking if they sum to 0. This takes $O(n^3)$ time and requires additional work to avoid duplicates.
- **Optimized Strategy (Sort + Two Pointers):** Sort the array, then for each element, use two pointers to find pairs that sum to the target. This takes $O(n^2)$ time and naturally handles duplicates.
- **Why it's better:** The optimized approach reduces time complexity from $O(n^3)$ to $O(n^2)$ and makes duplicate handling straightforward by skipping duplicate values.

**1.4 Decomposition:**

1. Sort the array.
2. For each element at index $i$:
   - Skip duplicates for the first number.
   - Use two pointers (`left = i+1`, `right = n-1`) to find pairs that sum to $-nums[i]$.
   - If sum equals 0, add the triplet and skip duplicates for both pointers.
   - If sum is less than 0, move left pointer right.
   - If sum is greater than 0, move right pointer left.
3. Return all unique triplets.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [-1,0,1,2,-1,-4]$

After sorting: $[-4,-1,-1,0,1,2]$

**2.2 Start Processing:**

We iterate through each element as the first number.

**2.3 Trace Walkthrough:**

| i | nums[i] | left | right | Sum | Action | Triplet Found |
|---|---------|------|-------|-----|--------|---------------|
| 0 | -4 | 1 | 5 | $-4+(-1)+2=-3$ | Move left | No |
| 0 | -4 | 2 | 5 | $-4+(-1)+2=-3$ | Move left | No |
| 0 | -4 | 3 | 5 | $-4+0+2=-2$ | Move left | No |
| 0 | -4 | 4 | 5 | $-4+1+2=-1$ | Move left | No |
| 1 | -1 | 2 | 5 | $-1+(-1)+2=0$ | Found! | $[-1,-1,2]$ |
| 1 | -1 | 3 | 4 | $-1+0+1=0$ | Found! | $[-1,0,1]$ |
| 2 | -1 | 3 | 4 | Skip (duplicate of i=1) | - | - |

**2.4 Duplicate Handling:**

- When `i > 0` and `nums[i] == nums[i-1]`, we skip to avoid duplicate triplets.
- After finding a triplet, we skip duplicate values for both left and right pointers.

**2.5 Return Result:**

We return `[[-1,-1,2], [-1,0,1]]`, which are all unique triplets that sum to 0.

> **Note:** Sorting is crucial because it allows us to use two pointers and naturally skip duplicates. Without sorting, we'd need a hash map approach which is more complex and requires additional duplicate handling.
