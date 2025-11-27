# Problem 3678: Smallest Absent Positive Greater Than Average

**Difficulty:** Easy  
**LeetCode Link:** https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

## Problem Description

You are given an integer array `nums`.

Return the **smallest absent positive** integer in `nums` such that it is **strictly greater** than the **average** of all elements in `nums`.

The **average** of an array is defined as the sum of all its elements divided by the number of elements.

**Example 1:**

```
Input: nums = [3,5]
Output: 6
Explanation: The average of nums is (3 + 5) / 2 = 8 / 2 = 4. The smallest absent positive integer greater than 4 is 6.
```

**Example 2:**

```
Input: nums = [-1,1,2]
Output: 3
Explanation: The average of nums is (-1 + 1 + 2) / 3 = 2 / 3 = 0.667. The smallest absent positive integer greater than 0.667 is 3.
```

**Example 3:**

```
Input: nums = [4,-1]
Output: 2
Explanation: The average of nums is (4 + (-1)) / 2 = 3 / 2 = 1.50. The smallest absent positive integer greater than 1.50 is 2.
```

**Constraints:**

- `1 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`

## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the smallest positive integer that is both (1) not present in the array and (2) strictly greater than the average of all array elements.

**1.1 Constraints & Complexity:**

- **Input Size:** We have at most 100 elements, and each element is between -100 and 100.
- **Time Complexity:** $O(n)$ where $n$ is the number of elements. We calculate the average in $O(n)$ time, create a set in $O(n)$ time, and then iterate through candidates (which in worst case could be $O(n)$ if many consecutive numbers are present).
- **Space Complexity:** $O(n)$ for storing the set of numbers for fast lookup.
- **Edge Case:** If the average is negative or zero, we must start checking from 1 (the smallest positive integer) since the result must be positive.

**1.2 High-level approach:**

The goal is to compute the average, find the smallest integer greater than the average, and then increment until we find a positive integer that is not in the array.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Calculate average, then for each candidate starting from `floor(avg) + 1`, check if it's in the array by linear search. This is $O(n^2)$ time in worst case.
- **Optimized Strategy:** Calculate average, convert array to a set for $O(1)$ lookup, then check candidates starting from `floor(avg) + 1` (or 1 if average is negative/zero). This is $O(n)$ time and $O(n)$ space.
- **Optimization:** Using a set allows us to check membership in constant time, reducing the overall time complexity from $O(n^2)$ to $O(n)$.

**1.4 Decomposition:**

1. Calculate the average of all elements in the array.
2. Determine the starting candidate: the smallest integer strictly greater than the average (using `floor(average) + 1`).
3. If the candidate is less than 1 (negative or zero), set it to 1 since we need a positive integer.
4. Convert the array to a set for efficient membership testing.
5. Increment the candidate until we find a positive integer that is not in the set.
6. Return that integer.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example input: `nums = [3, 5]`.

- Average = $(3 + 5) / 2 = 8 / 2 = 4.0$
- Starting candidate = `int(4.0) + 1 = 4 + 1 = 5`
- Set of numbers: `{3, 5}`

**2.2 Start Checking:**

We begin with candidate `res = 5` and check if it's in the set.

**2.3 Trace Walkthrough:**

| Candidate | Is in Set? | Action |
|-----------|------------|--------|
| 5         | Yes (5 is in {3, 5}) | Increment: `res = 6` |
| 6         | No (6 is not in {3, 5}) | Return 6 |

**2.4 Increment and Loop:**

When a candidate is found in the set, we increment it by 1 and check again. This continues until we find a candidate that is not in the set.

**2.5 Return Result:**

After finding that 6 is not in the set, we return `res = 6`, which is the smallest absent positive integer greater than the average (4.0).
