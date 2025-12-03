# Problem 3625: Find the Power of K-Size Subarrays I
**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

## Explanation

### Strategy (The "Why")

The problem asks us to find the "power" of all subarrays of size $k$. The power is the maximum element if all elements are consecutive and sorted in ascending order, otherwise $-1$.

**1.1 Constraints & Complexity:**

- **Input Constraints:** $1 \leq n \leq 500$, $1 \leq \text{nums}[i] \leq 10^5$, $1 \leq k \leq n$.
- **Time Complexity:** $O(n \times k)$ - We check $n-k+1$ subarrays, and each check takes $O(k)$ time.
- **Space Complexity:** $O(1)$ - We only use constant extra space (excluding output array).
- **Edge Case:** If $k=1$, each subarray has power equal to its single element.

**1.2 High-level approach:**

The goal is to check each subarray of size $k$ to see if it contains consecutive integers in ascending order. If so, return the maximum (which is the last element); otherwise return $-1$.

![Subarray Power](https://assets.leetcode.com/static_assets/others/subarray-power.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each subarray, check if it's consecutive and sorted by comparing adjacent elements. This takes $O(n \times k)$ time.
- **Optimized (Range Check):** For each subarray starting at index $i$, check if it equals `range(nums[i], nums[i] + k)`. This also takes $O(n \times k)$ but is cleaner.
- **Emphasize the optimization:** While complexity is the same, using Python's `range` comparison makes the code more readable and less error-prone.

**1.4 Decomposition:**

1. **Iterate Subarrays:** For each starting position $i$ from $0$ to $n-k$, extract subarray of size $k$.
2. **Check Consecutive:** Verify if subarray equals `list(range(subarray[0], subarray[0] + k))`.
3. **Calculate Power:** If consecutive, append maximum (last element); otherwise append $-1$.
4. **Return Result:** Return the result array.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `nums = [1,2,3,4,3,2,5]`, `k = 3`.

Initialize: `res = []`, `n = 7`

**2.2 Start Processing:**

Check subarray starting at index $0$: `[1,2,3]`.

**2.3 Trace Walkthrough:**

| i | Subarray | Expected | Match? | Power |
|---|----------|----------|--------|-------|
| 0 | [1,2,3] | [1,2,3] | Yes | 3 |
| 1 | [2,3,4] | [2,3,4] | Yes | 4 |
| 2 | [3,4,3] | [3,4,5] | No | -1 |
| 3 | [4,3,2] | [4,5,6] | No | -1 |
| 4 | [3,2,5] | [3,4,5] | No | -1 |

**2.4 Complete Processing:**

All $5$ subarrays processed: $2$ are consecutive (power = max), $3$ are not (power = -1).

**2.5 Return Result:**

The function returns `[3,4,-1,-1,-1]`.

> **Note:** A subarray is consecutive if it forms a sequence like `[a, a+1, a+2, ..., a+k-1]` where $a$ is the first element.

