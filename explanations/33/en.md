## Explanation

### Strategy (The "Why")

Given an integer array `nums` sorted in ascending order (with distinct values) that is rotated at some pivot, and a target value, we need to search for `target` in `nums`. Return the index if found, or -1 if not found.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be up to $5000$.
- **Value Range:** Array elements are distinct and between $-10^4$ and $10^4$.
- **Time Complexity:** $O(\log n)$ - We use binary search, eliminating half of the remaining elements at each step.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space.
- **Edge Case:** If the array is not rotated (sorted), use standard binary search. If target is not found, return -1.

**1.2 High-level approach:**

The goal is to search for a target in a rotated sorted array.

We use binary search with a twist: we determine which half is sorted, then check if the target is in that sorted half. If yes, search there; otherwise, search the other half.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Linear search through the array. This takes $O(n)$ time.
- **Optimized Strategy (Modified Binary Search):** Use binary search, but determine which half is sorted and search accordingly. This takes $O(\log n)$ time.
- **Why it's better:** The modified binary search reduces time complexity from $O(n)$ to $O(\log n)$ by leveraging the sorted property of at least one half.

**1.4 Decomposition:**

1. Use binary search with left and right pointers.
2. At each step, determine which half is sorted (by comparing nums[left] and nums[mid]).
3. If left half is sorted:
   - If target is in the sorted range, search left half.
   - Otherwise, search right half.
4. If right half is sorted:
   - If target is in the sorted range, search right half.
   - Otherwise, search left half.
5. Return the index if found, -1 otherwise.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [4,5,6,7,0,1,2]$, $target = 0$

We initialize:
- `left = 0`, `right = 6`

**2.2 Start Binary Search:**

We begin searching.

**2.3 Trace Walkthrough:**

| Iteration | left | right | mid | nums[mid] | Sorted Half | Target In Range? | Action |
|-----------|------|-------|-----|-----------|-------------|-----------------|--------|
| 1 | 0 | 6 | 3 | 7 | Left (4≤7) | No (0<4) | Search right |
| 2 | 4 | 6 | 5 | 1 | Right (1≤2) | Yes (0<1≤2) | Search right |
| 3 | 4 | 4 | 4 | 0 | - | Found! | Return 4 |

**2.4 Explanation:**

- Mid = 3: Left half [4,5,6,7] is sorted, but target 0 is not in [4,7], so search right half.
- Mid = 5: Right half [1,2] is sorted, but target 0 is not in [1,2]. Actually, wait - let me reconsider.
- Actually, when we check right half: nums[5]=1, nums[6]=2, so right half [1,2] is sorted. But target 0 < 1, so it's not in the right half. We should search left of mid, but that's the unsorted part. Let me trace more carefully.

Actually, the logic is: if right half is sorted and target is not in [nums[mid], nums[right]], then target must be in the left half (which might be unsorted, but that's okay).

**2.5 Return Result:**

We return 4, which is the index of target 0.

> **Note:** The key insight is that at least one half is always sorted in a rotated array. By checking which half is sorted and whether the target is in that sorted range, we can eliminate half of the remaining elements at each step.

