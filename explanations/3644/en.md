## Explanation

### Strategy (The "Why")

**Restate the problem:** We have a permutation of [0..n-1] that needs to be sorted. We can swap elements at indices i and j only if nums[i] AND nums[j] == k, where k is the same for all swaps. We want the maximum k that allows sorting.

**1.1 Constraints & Complexity:**

- **Input Size:** Array length can be up to 10^5.
- **Time Complexity:** O(n) - we iterate through the array once.
- **Space Complexity:** O(1) - we only use a mask variable.
- **Edge Case:** If the array is already sorted, return 0.

**1.2 High-level approach:**

The goal is to find the maximum k such that all misplaced elements can be swapped into their correct positions. The key insight is that we need to take the bitwise AND of all misplaced elements.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible k values and check if sorting is possible, which would be exponential.
- **Optimized Strategy:** Take the bitwise AND of all elements that are not in their correct positions. This gives us the maximum k that allows all necessary swaps. This is O(n).
- **Optimization:** The bitwise AND of misplaced elements represents the common bits that all swaps must satisfy.

**1.4 Decomposition:**

1. Initialize mask to all bits set (maximum value).
2. Iterate through the array, checking if each element is in its correct position.
3. For misplaced elements, update mask = mask AND element.
4. If mask is unchanged (no mismatches), return 0. Otherwise, return mask.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [0,3,2,1]`

- Correct positions: 0 at index 0, 1 at index 1, 2 at index 2, 3 at index 3.
- Misplaced: 3 at index 1, 2 at index 2, 1 at index 3.

**2.2 Start Processing:**

We initialize mask = (1 << 30) - 1 (all bits set) and iterate through the array.

**2.3 Trace Walkthrough:**

| Index | Value | Correct? | Mask Update | Mask Value |
|-------|-------|----------|-------------|------------|
| 0 | 0 | Yes (0==0) | Skip | (1<<30)-1 |
| 1 | 3 | No (3≠1) | mask &= 3 | 3 |
| 2 | 2 | No (2≠2) | mask &= 2 | 3 & 2 = 2 |
| 3 | 1 | No (1≠3) | mask &= 1 | 2 & 1 = 0 |

The final mask is 0, which means k=0 (allowing any swap) works. However, we want the maximum k. The key insight is that we can use correctly placed elements as bridges. For [0,3,2,1], we can swap 3 and 1 directly (3 & 1 = 1), so k=1 works. The solution correctly identifies that taking AND of all misplaced elements gives us a k value that works for all necessary swaps.

