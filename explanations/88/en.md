You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be *stored inside the array* `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

**Example 1:**

```text
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

**Example 2:**

```text
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
```

**Example 3:**

```text
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
```

**Constraints:**

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

**Follow up:** Can you come up with an algorithm that runs in `O(m + n)` time?

## Explanation

### Strategy

This is a **two-pointer array merging problem** that requires combining two sorted arrays into one sorted array. The key insight is that we need to merge the arrays in-place into `nums1`, which has extra space at the end to accommodate the merged result.

**Key observations:**
- Both input arrays are already sorted in non-decreasing order
- `nums1` has enough space (length `m + n`) to hold the merged result
- We need to merge from the end to avoid overwriting elements in `nums1` that we still need
- The zeros at the end of `nums1` are placeholders and should be ignored

**High-level approach:**
1. **Use three pointers**: One for the end of the merged array, one for the end of valid elements in `nums1`, and one for the end of `nums2`
2. **Compare and merge from the end**: Start from the largest elements and work backwards
3. **Fill the merged array**: Place the larger element at the end of the merged array
4. **Handle remaining elements**: If any elements remain in either array, copy them to the merged array

### Steps

Let's break down the solution step by step:

**Step 1: Set up pointers**
We need three pointers:
- `p1`: Points to the last valid element in `nums1` (at index `m - 1`)
- `p2`: Points to the last element in `nums2` (at index `n - 1`)
- `p`: Points to the last position in the merged array (at index `m + n - 1`)

**Step 2: Compare and merge from the end**
Starting from the end of both arrays:
- Compare `nums1[p1]` with `nums2[p2]`
- Place the larger element at `nums1[p]`
- Decrement the appropriate pointer

**Step 3: Continue until one array is exhausted**
- If `nums1[p1]` is larger, place it at `nums1[p]` and decrement `p1`
- If `nums2[p2]` is larger, place it at `nums1[p]` and decrement `p2`
- Decrement `p` after each placement

**Step 4: Handle remaining elements**
- If `nums2` still has elements, copy them to the beginning of `nums1`
- If `nums1` still has elements, they're already in the correct position

**Example walkthrough:**
Let's trace through the first example:

```text
nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

Initial state:
p1 = 2 (points to 3), p2 = 2 (points to 6), p = 5

Step 1: Compare 3 and 6
6 > 3, so place 6 at nums1[5]
nums1 = [1,2,3,0,0,6], p1 = 2, p2 = 1, p = 4

Step 2: Compare 3 and 5
5 > 3, so place 5 at nums1[4]
nums1 = [1,2,3,0,5,6], p1 = 2, p2 = 0, p = 3

Step 3: Compare 3 and 2
3 > 2, so place 3 at nums1[3]
nums1 = [1,2,3,3,5,6], p1 = 1, p2 = 0, p = 2

Step 4: Compare 2 and 2
2 == 2, so place 2 at nums1[2] (from nums2)
nums1 = [1,2,2,3,5,6], p1 = 1, p2 = -1, p = 1

Step 5: p2 is exhausted, copy remaining nums1 elements
nums1 = [1,2,2,3,5,6]
```

> **Note:** Merging from the end is crucial because it prevents overwriting elements in `nums1` that we still need to compare. If we merged from the beginning, we would lose the original elements in `nums1`.

**Time Complexity:** O(m + n) - we visit each element exactly once  
**Space Complexity:** O(1) - we modify the array in-place without extra space 