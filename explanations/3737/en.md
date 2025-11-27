# Problem 3737: Count Subarrays With Majority Element I

**Difficulty:** Medium  
**LeetCode Link:** https://leetcode.com/problems/count-subarrays-with-majority-element-i/

## Problem Description

You are given an integer array `nums` and an integer `target`.

Return the number of **subarrays** of `nums` in which `target` is the **majority element**.

The **majority element** of a subarray is the element that appears **strictly more than half** of the times in that subarray.

**Example 1:**

```
Input: nums = [1,2,2,3], target = 2
Output: 5
Explanation: Valid subarrays with target = 2 as the majority element:
- nums[1..1] = [2]
- nums[2..2] = [2]
- nums[1..2] = [2,2]
- nums[0..2] = [1,2,2]
- nums[1..3] = [2,2,3]

So there are 5 such subarrays.
```

**Example 2:**

```
Input: nums = [1,1,1,1], target = 1
Output: 10
Explanation: All 10 subarrays have 1 as the majority element.
```

**Example 3:**

```
Input: nums = [1,2,3], target = 4
Output: 0
Explanation: target = 4 does not appear in nums at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.
```

**Constraints:**

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^9`
- `1 <= target <= 10^9`

## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count all contiguous subarrays where the `target` element appears strictly more than half the times. For a subarray of length `n`, this means `target` must appear more than `n/2` times, which is equivalent to `2 * count(target) > length`.

**1.1 Constraints & Complexity:**

- **Input Size:** We have at most 1000 elements, allowing for a brute force $O(n^2)$ solution.
- **Time Complexity:** $O(n^2)$ where $n$ is the length of the array. We check all $O(n^2)$ possible subarrays, and for each subarray we count occurrences in $O(1)$ amortized time.
- **Space Complexity:** $O(1)$ as we only use a constant amount of extra space for counting.
- **Edge Case:** If `target` doesn't appear in the array at all, no subarray can have it as majority, so we return 0.

**1.2 High-level approach:**

The goal is to iterate through all possible subarrays and check if `target` is the majority element in each one. For each subarray, we count how many times `target` appears and verify if `2 * count > length`.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all possible subarrays by fixing start and end positions. For each subarray, count occurrences of `target` and check if it's majority. This is $O(n^2)$ time, which is acceptable given the constraint $n \leq 1000$.
- **Optimized Strategy:** The brute force approach is already optimal for this problem size. We can optimize by maintaining a running count as we extend subarrays, avoiding redundant counting.
- **Optimization:** Instead of recounting from scratch for each subarray, we maintain a running count that increments as we extend the subarray, reducing the constant factor.

**1.4 Decomposition:**

1. Initialize a result counter to 0.
2. For each possible starting position `i` in the array.
3. Initialize a count of `target` occurrences to 0 for the subarray starting at `i`.
4. For each ending position `j` starting from `i`, extend the subarray to include `nums[j]`.
5. If `nums[j] == target`, increment the count.
6. Calculate the subarray length: `j - i + 1`.
7. Check if `2 * count > length` (majority condition).
8. If true, increment the result counter.
9. Continue until all subarrays have been checked.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example input: `nums = [1, 2, 2, 3]`, `target = 2`.

- Initialize `res = 0`
- We'll check all subarrays starting from each position

**2.2 Start Checking:**

We begin with `i = 0` (first starting position) and `count = 0`.

**2.3 Trace Walkthrough:**

| Start (i) | End (j) | Subarray | Count of 2 | Length | 2×Count > Length? | Action | `res` |
|-----------|---------|----------|------------|--------|-------------------|--------|-------|
| 0         | 0       | [1]      | 0          | 1      | No (0 > 1?)       | Skip   | 0     |
| 0         | 1       | [1,2]    | 1          | 2      | No (2 > 2?)       | Skip   | 0     |
| 0         | 2       | [1,2,2]  | 2          | 3      | Yes (4 > 3)        | Add 1  | 1     |
| 0         | 3       | [1,2,2,3]| 2          | 4      | No (4 > 4?)       | Skip   | 1     |
| 1         | 1       | [2]      | 1          | 1      | Yes (2 > 1)        | Add 1  | 2     |
| 1         | 2       | [2,2]    | 2          | 2      | Yes (4 > 2)        | Add 1  | 3     |
| 1         | 3       | [2,2,3]  | 2          | 3      | Yes (4 > 3)        | Add 1  | 4     |
| 2         | 2       | [2]      | 1          | 1      | Yes (2 > 1)        | Add 1  | 5     |
| 2         | 3       | [2,3]    | 1          | 2      | No (2 > 2?)        | Skip   | 5     |
| 3         | 3       | [3]      | 0          | 1      | No (0 > 1?)        | Skip   | 5     |

**2.4 Increment and Loop:**

After processing all subarrays starting at position `i`, we move to the next starting position `i + 1` and repeat the process until all positions have been checked.

**2.5 Return Result:**

After processing all subarrays, `res = 5`, which is the number of subarrays where `target = 2` is the majority element.

