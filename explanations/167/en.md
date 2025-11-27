## Explanation

### Strategy (The "Why")

Given a 1-indexed array of integers `numbers` that is sorted in non-decreasing order, and a target integer, we need to find two numbers such that they add up to target. Return the indices of the two numbers (1-indexed).

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be between $2$ and $3 \times 10^4$.
- **Value Range:** Each number and target are between $-1000$ and $1000$.
- **Time Complexity:** $O(n)$ - We use two pointers that each traverse the array at most once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for pointers.
- **Edge Case:** There is exactly one solution, so we don't need to handle multiple solutions or no solution cases.

**1.2 High-level approach:**

The goal is to find two numbers that sum to the target in a sorted array.

![Two Sum II](https://assets.leetcode.com/uploads/2021/07/15/167_example_2.png)

We use two pointers: one at the start (left) and one at the end (right). Since the array is sorted, if the sum is too small, we move left forward. If the sum is too large, we move right backward.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all pairs of numbers, checking if they sum to target. This takes $O(n^2)$ time.
- **Optimized Strategy (Two Pointers):** Use two pointers starting at both ends. Move them based on whether the current sum is less than, equal to, or greater than the target. This takes $O(n)$ time.
- **Why it's better:** The two-pointer approach leverages the sorted property to eliminate half of the remaining possibilities at each step, reducing time from $O(n^2)$ to $O(n)$.

**1.4 Decomposition:**

1. Initialize two pointers: `left = 0` and `right = len(numbers) - 1`.
2. While `left < right`:
   - Calculate `current_sum = numbers[left] + numbers[right]`.
   - If `current_sum == target`, return `[left + 1, right + 1]` (1-indexed).
   - If `current_sum < target`, increment `left` (need larger sum).
   - If `current_sum > target`, decrement `right` (need smaller sum).
3. Return the indices (guaranteed to exist).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $numbers = [2,7,11,15]$, $target = 9$

We initialize:
- `left = 0`, `right = 3`

**2.2 Start Checking:**

We begin comparing sums.

**2.3 Trace Walkthrough:**

| Iteration | left | right | numbers[left] | numbers[right] | Sum | Comparison | Action |
|-----------|------|-------|---------------|----------------|-----|------------|--------|
| 1 | 0 | 3 | 2 | 15 | 17 | $17 > 9$ | Decrement right |
| 2 | 0 | 2 | 2 | 11 | 13 | $13 > 9$ | Decrement right |
| 3 | 0 | 1 | 2 | 7 | 9 | $9 == 9$ | **Found!** |

**2.4 Return Result:**

We return `[1, 2]` (1-indexed), which corresponds to values 2 and 7 that sum to 9.

**2.5 Why It Works:**

Since the array is sorted:
- If sum is too large, moving right backward decreases the sum.
- If sum is too small, moving left forward increases the sum.
- This guarantees we'll find the solution if it exists.

> **Note:** The sorted property is crucial. Without it, we'd need a hash map approach like in the original Two Sum problem. The two-pointer technique is more efficient for sorted arrays.
