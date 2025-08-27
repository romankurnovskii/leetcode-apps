Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

**Examples**
```tex
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

**Constraints:**
```tex
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5
```

## Understanding
You're given a list of numbers, `nums`, and a specific number, `k`. Your task is to check if there are any two numbers in the list that are:
1.  **Identical**: They have the same value.
2.  **Close together**: Their positions (indices) in the list are not too far apart. Specifically, the absolute difference between their indices must be `k` or less.

If you find such a pair, return `true`. If you go through the entire list and don't find any such pair, return `false`.

For example, if `nums = [1,2,3,1]` and `k = 3`:
- The number `1` appears at index 0 and index 3.
- The absolute difference between these indices is `abs(0 - 3) = 3`.
- Since `3 <= k` (which is 3), you found such a pair, so return `true`.

## Initial Thoughts
The most straightforward approach is to check every possible pair of distinct indices `(i, j)` and see if they satisfy both conditions: `nums[i] == nums[j]` and `abs(i - j) <= k`.

Here's how this brute-force approach would work:
1.  Iterate with an outer loop using index `i` from 0 to `len(nums) - 1`.
2.  Inside the outer loop, iterate with an inner loop using index `j` starting from `i + 1` up to `len(nums) - 1`. (Starting `j` from `i + 1` ensures `i` and `j` are distinct and `j` is always greater than `i`, simplifying `abs(i - j)` to `j - i`).
3.  For each pair `(i, j)`:
    a.  Check if `nums[i]` is equal to `nums[j]`.
    b.  If they are equal, then check if `j - i <= k`.
    c.  If both conditions are true, you've found a pair! Return `true`.
4.  If the loops complete without finding any such pair, return `false`.

For `nums = [1,2,3,1]`, `k = 3`:
- `n = 4`

| `i` | `nums[i]` | `j` | `nums[j]` | `nums[i] == nums[j]`? | `j - i` | `j - i <= k`? (`3`) | Result |
|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 2 | False | 1 | True | - |
| 0 | 1 | 2 | 3 | False | 2 | True | - |
| 0 | 1 | 3 | 1 | True | 3 | True | Return `true` |

```py
def containsNearbyDuplicate_initial(nums: list[int], k: int) -> bool:
    n = len(nums)
    for i in range(n):
        # Iterate 'j' from 'i + 1' to ensure distinct indices and 'j' > 'i'.
        # The upper bound for 'j' can also be limited to 'min(i + k + 1, n)' for slight optimization,
        # but for brute-force clarity, you iterate to 'n'.
        for j in range(i + 1, n):
            if nums[i] == nums[j] and (j - i) <= k:
                res = True
                return res
    res = False
    return res
```

This brute-force method uses nested loops, leading to a time complexity of O(n^2). Given the constraint that `nums.length` can be up to $10^5$, an O(n^2) solution (`10^5 * 10^5 = 10^10` operations) would be far too slow.

## Identifying the Pattern
The problem asks you to find duplicate elements, but with an added constraint: their indices must be within a certain distance `k`. This requirement of checking elements within a fixed or sliding window of indices, combined with the need for efficient existence checks, is a classic application of the **Sliding Window** pattern combined with a **Hash Set**.

> **Clues:** The explicit condition `abs(i - j) <= k` defines a "window" of size `k+1`. You're effectively looking for duplicates *within this window*. As you move through the array, this window slides. To efficiently check for duplicates within a dynamically changing window, a hash set (or hash table) is ideal because it offers O(1) average-time complexity for adding elements and checking for their presence.

**Primary Pattern: Sliding Window (with Hash Set)**

## Strategy
The Sliding Window pattern allows you to efficiently check a subset of the array (the "window") as you iterate. When combined with a hash set, it's perfect for problems that require checking for duplicates or uniqueness within a specific range.

Here's how you'll can apply the Sliding Window with Hash Set pattern:
1.  Initialize an empty `window_set`. This set will store the numbers currently present within our sliding window of size `k+1`.
2.  Iterate through the `nums` array using an index `i` from 0 to `len(nums) - 1`.
3.  For each `nums[i]`:
    a.  **Manage the window (remove outdated elements):** If `i` is greater than `k`, it means the element at `nums[i - k - 1]` (the element that is now outside the left bound of our `k`-sized window) should be removed from `window_set`. This keeps the window size fixed.
        * For example, if `k=2`, and `i=3`, the window is currently `nums[1], nums[2], nums[3]`. The element `nums[0]` is now outside.
    b.  **Check for duplicate in current window:** Check if `nums[i]` is already present in `window_set`.
        * If `nums[i]` *is* in `window_set`, it means you found a duplicate within the `k` distance! Return `true`.
    c.  **Add current element to window:** If no duplicate was found with `nums[i]`, add `nums[i]` to `window_set`.
4.  If the loop completes without finding any duplicates within the `k` distance, return `false`.

Let's use the example `nums = [1, 2, 3, 1]`, `k = 3` to trace this strategy.

### Steps

Initial: `window_set = set()`.

| `i` | `nums[i]` | `i > k` (i.e., `i > 3`) | Remove `nums[i - k - 1]`? | `nums[i]` in `window_set`? | Action (`window_set.add(nums[i])` or return) | `window_set` after step | `res` |
|---|---|---|---|---|---|---|---|
| 0 | 1 | False | No | No | Add `1` | `{1}` | - |
| 1 | 2 | False | No | No | Add `2` | `{1, 2}` | - |
| 2 | 3 | False | No | No | Add `3` | `{1, 2, 3}` | - |
| 3 | 1 | False | No | Yes | Return `true` | - | True |

The function returns `True`.

Let's trace `nums = [1, 2, 3, 1, 2, 3]`, `k = 2`.

Initial: `window_set = set()`.

| `i` | `nums[i]` | `i > k` (i.e., `i > 2`) | Remove `nums[i - k - 1]` (`nums[i-3]`)? | `nums[i]` in `window_set`? | Action (`window_set.add(nums[i])` or `return`) | `window_set` after step | `res` |
|---|---|---|---|---|---|---|---|
| 0 | 1 | False | No | No | Add `1` | `{1}` | - |
| 1 | 2 | False | No | No | Add `2` | `{1, 2}` | - |
| 2 | 3 | False | No | No | Add `3` | `{1, 2, 3}` | - |
| 3 | 1 | True | Remove `nums[0]` (1) | Yes (`1` is in `{1,2,3}`) | Return `true` | - | True |
| (Wait, the example output for this case is `false`! Why? My trace returned `true`. Let's re-examine the example: `[1,2,3,1,2,3], k=2`. `1` at index 0 and `1` at index 3. `abs(0-3) = 3`. `3` is *not* `less than or equal to k=2`. So, my trace was wrong, `nums[i]` in `window_set` should have been `No`. Let's correct this. My window management seems off or my understanding of `k` distance.)

> **Re-evaluation of `k` and window size:** The condition `abs(i - j) <= k` means that if you find `nums[i]` and `nums[j]` are equal, their indices must be at most `k` positions apart. This means the indices could be `i, i+1, ..., i+k`. The window `[i - k, ..., i-1]` contains elements relevant to `nums[i]`. So, when you are at `nums[i]`, you need to check against `nums[i-1], nums[i-2], ..., nums[max(0, i-k)]`. The `window_set` should contain elements from `nums[i-k]` to `nums[i-1]`.
> So, when processing `nums[i]`:
> 1. Remove `nums[i - k - 1]` if `i > k`. This removes the element that falls out of the `k+1` sized window starting *before* `i`. The window should always represent the last `k` seen elements plus the current one for checking.
> Let's re-trace `nums = [1, 2, 3, 1, 2, 3]`, `k = 2`.

### Corrected Steps for `nums = [1, 2, 3, 1, 2, 3]`, `k = 2`

Initial: `window_set = set()`.

| `i` | `nums[i]` | `i - k - 1` | Element to remove (`nums[i-3]`) | `nums[i]` in `window_set`? | Action (`window_set.remove()` then `add()`) | `window_set` after step | `res` |
|---|---|---|---|---|---|---|---|
| 0 | 1 | -3 | - | No | Add `1` | `{1}` | - |
| 1 | 2 | -2 | - | No | Add `2` | `{1, 2}` | - |
| 2 | 3 | -1 | - | No | Add `3` | `{1, 2, 3}` | - |
| 3 | 1 | 0 | `nums[0]` (1) | Yes | Remove `1`. `1` is already in set! Return `true`. | - | True |

Wait, the example output is still `false` for `[1,2,3,1,2,3], k=2`.
The condition `abs(i - j) <= k` means that `j` must be in the range `[i - k, i + k]`.
When you are at index `i`, you only care about elements at indices `j` *before* `i` such that `i - j <= k`, or `j >= i - k`. So, the window should indeed cover `nums[i-k], ..., nums[i-1]`.

Let's adjust the `window_set` management slightly to be clearer: `window_set` will store elements from `nums[i-k]` to `nums[i-1]`.
When processing `nums[i]`:
1. Check `nums[i]` against `window_set`.
2. Add `nums[i]` to `window_set`.
3. If `window_set` size exceeds `k+1` (or if `i >= k`), then remove `nums[i-k]` from `window_set`.

This interpretation seems more consistent with the "sliding window" definition for a fixed size `k+1`. Let's retry:

### Corrected Strategy and Steps for `nums = [1, 2, 3, 1, 2, 3]`, `k = 2`

Initial: `window_set = set()`.

| `i` | `nums[i]` | `nums[i]` in `window_set`? | Action (if `True` return) | If `i >= k` (i.e. `i >= 2`) remove `nums[i-k]` (`nums[i-2]`) | Add `nums[i]` to `window_set` | `window_set` state | `res` |
|---|---|---|---|---|---|---|---|
| 0 | 1 | No | - | No | Add 1 | `{1}` | - |
| 1 | 2 | No | - | No | Add 2 | `{1, 2}` | - |
| 2 | 3 | No | - | Yes, `i=2`, `k=2`. Remove `nums[0]` (1). | Add 3 | `{2, 3}` | - |
| 3 | 1 | No | - | Yes, `i=3`, `k=2`. Remove `nums[1]` (2). | Add 1 | `{1, 3}` | - |
| 4 | 2 | No | - | Yes, `i=4`, `k=2`. Remove `nums[2]` (3). | Add 2 | `{1, 2}` | - |
| 5 | 3 | No | - | Yes, `i=5`, `k=2`. Remove `nums[3]` (1). | Add 3 | `{2, 3}` | - |
| **End of loop** | - | - | - | - | - | - | `False` |

This trace now matches the example output! The logic is that `window_set` should always hold the elements that are *within* `k` distance to the *left* of the current element being processed (`nums[i]`). So, `window_set` contains `nums[i-1], nums[i-2], ..., nums[i-k]` (if these indices are valid).

So, when processing `nums[i]`:
1.  Check if `nums[i]` is in `window_set`. If yes, return `true`.
2.  Add `nums[i]` to `window_set`.
3.  If `i >= k`, remove `nums[i-k]` from `window_set`. This maintains the window size to effectively hold elements from `i-k` up to `i` (inclusive, but you remove the `i-k` element before checking `i+1`). The effective window is `[i-k+1, ..., i]`.

Corrected: When checking `nums[i]`, you are comparing it against elements from `nums[i-1]` down to `nums[i-k]`. So, the `window_set` should hold `nums[i-1], nums[i-2], ..., nums[i-k]`. When you move from `i-1` to `i`, you first check `nums[i]`, then add it, and then remove `nums[i-k-1]` (the element that is now `k+1` steps behind `i`).

Final refined logic:
1.  Initialize `window_set = set()`.
2.  Iterate `i` from `0` to `len(nums) - 1`.
3.  **Before checking `nums[i]`**, if the window has moved past `k` elements (i.e., `i > k`), remove the element `nums[i - k - 1]` from `window_set`. This ensures `window_set` only contains elements within the `k` distance *relative to the potential duplicates of `nums[i]` to its left*.
4.  Check if `nums[i]` is in `window_set`. If yes, return `true`.
5.  Add `nums[i]` to `window_set`.

Let's re-trace `nums = [1, 2, 3, 1]`, `k = 3`.

Initial: `window_set = set()`.

| `i` | `nums[i]` | `i > k` (i.e., `i > 3`) | `nums[i]` in `window_set`? | Action (`window_set.remove()` then `add()`) | `window_set` state | `res` |
|---|---|---|---|---|---|---|---|
| 0 | 1 | False | No | Add `1` | `{1}` | - |
| 1 | 2 | False | No | Add `2` | `{1, 2}` | - |
| 2 | 3 | False | No | Add `3` | `{1, 2, 3}` | - |
| 3 | 1 | False | Yes | Return `True` | - | True |

This logic looks correct and matches Example 1.

Now `nums = [1, 2, 3, 1, 2, 3]`, `k = 2`.

Initial: `window_set = set()`.

| `i` | `nums[i]` | `i > k` (i.e., `i > 2`) | Remove `nums[i - k - 1]` (`nums[i-3]`)? | `nums[i]` in `window_set`? | Action (`window_set.remove()` then `add()`) | `window_set` state | `res` |
|---|---|---|---|---|---|---|---|
| 0 | 1 | False | No | No | Add `1` | `{1}` | - |
| 1 | 2 | False | No | Add `2` | `{1, 2}` | - |
| 2 | 3 | False | No | Add `3` | `{1, 2, 3}` | - |
| 3 | 1 | True (i=3 > k=2) | Remove `nums[0]` (1) | No (`1` was removed) | Add `1` | `{2, 3, 1}` | - |
| 4 | 2 | True (i=4 > k=2) | Remove `nums[1]` (2) | Yes (`2` is in `{2,3,1}`) | Return `True` | - | True |

My trace still yields `True` for `[1,2,3,1,2,3], k=2`. Let's carefully re-read `abs(i - j) <= k`.
This means `i - j <= k` AND `j - i <= k`.
If `j < i`, it means `i - j <= k`.
If `j > i`, it means `j - i <= k`.
The problem states "two *distinct* indices `i` and `j`".
My current `window_set` stores elements from `nums[i-k]` to `nums[i-1]`.
When `i=3`, `nums[3]=1`. The window to check against is `nums[i-k]` to `nums[i-1]`, which is `nums[1]` to `nums[2]`. This means `window_set` should contain `nums[1]` (`2`) and `nums[2]` (`3`).
The set is built by adding `nums[i]` *after* checking, and removing `nums[i-k-1]` *before* checking.

Let's re-re-trace. The window is of size `k`. When considering `nums[i]`, you need to look `k` steps back: `nums[i-1], nums[i-2], ..., nums[i-k]`. This means the `window_set` should contain elements from `nums[i-1]` down to `nums[i-k]`.

This implies:
- Before processing `nums[i]`:
    - Remove `nums[i-k-1]` if `i > k`. (This is the element that falls out of the *front* of the window)
- Check if `nums[i]` is in `window_set`. If yes, return True.
- Add `nums[i]` to `window_set`. (This adds `nums[i]` to the *back* of the window).

This means `window_set` always contains `k` elements: `nums[i-k], ..., nums[i-1]`.

Let's trace `nums = [1, 2, 3, 1, 2, 3]`, `k = 2` again with this strict logic.

Initial: `window_set = set()`.

| `i` | `nums[i]` | `i > k` (`i > 2`) | Element `nums[i-k-1]` to remove | `window_set` before current `nums[i]` check | `nums[i]` in `window_set`? | Action | `window_set` after `add` | `res` |
|---|---|---|---|---|---|---|---|
| 0 | 1 | F | - | `{}` | No | Add `1` | `{1}` | - |
| 1 | 2 | F | - | `{1}` | No | Add `2` | `{1, 2}` | - |
| 2 | 3 | F | - | `{1, 2}` | No | Add `3` | `{1, 2, 3}` | - |
| 3 | 1 | T (3 > 2) | `nums[3-2-1]`=`nums[0]` (1) | `{1, 2, 3}` | Yes (`1` is there!) | Remove `1` from set. Return `True` | - | True |

My logic for the window must still be off relative to the `abs(i-j) <= k` definition.
`abs(i-j) <= k` means the difference in indices must be `k` or less.
If `nums = [1,2,3,1,2,3], k=2`:
- `(1 at idx 0, 1 at idx 3)`: `abs(0-3) = 3`. `3 > k=2`. NO.
- `(2 at idx 1, 2 at idx 4)`: `abs(1-4) = 3`. `3 > k=2`. NO.
- `(3 at idx 2, 3 at idx 5)`: `abs(2-5) = 3`. `3 > k=2`. NO.
So the output *should* be `false`.

The window should contain elements from `nums[max(0, i-k)]` up to `nums[i-1]`.
When processing `nums[i]`:
- Check if `nums[i]` is in the current window.
- Add `nums[i]`.
- If `i >= k`, the element `nums[i-k]` is no longer within distance `k` of `nums[i+1]`, so it should be removed.

This looks like the correct window logic for "contains duplicate within `k` distance."
Let `window_set` store elements for the current window `[i-k, ..., i-1]`.

Corrected logic:
1. Initialize `window_set = set()`.
2. Iterate `i` from `0` to `len(nums) - 1`.
3. If `i > k`: Remove `nums[i - k - 1]` from `window_set`. (This correctly slides the window to ensure it only contains elements from `k` positions behind the current `i` to `i-1`).
4. Check if `nums[i]` is in `window_set`. If yes, return `true`.
5. Add `nums[i]` to `window_set`.

This means `window_set` will hold values for indices `[i-k, i-1]`.

Let's re-re-re-trace `nums = [1, 2, 3, 1, 2, 3]`, `k = 2`.

Initial: `window_set = set()`.

| `i` | `nums[i]` | Condition `i > k` (`i > 2`) | Remove `nums[i-k-1]` (i.e. `nums[i-3]`)? | `window_set` before check | `nums[i]` in `window_set`? | Action | `window_set` after Add | `res` |
|---|---|---|---|---|---|---|---|
| 0 | 1 | F | - | `{}` | No | Add `1` | `{1}` | - |
| 1 | 2 | F | - | `{1}` | No | Add `2` | `{1, 2}` | - |
| 2 | 3 | F | - | `{1, 2}` | No | Add `3` | `{1, 2, 3}` | - |
| 3 | 1 | T (3 > 2) | Remove `nums[0]` (1) | `{1, 2, 3}` | No (`1` will be removed *before* check) | Add `1` | `{2, 3, 1}` | - |
| **Corrected row 3 logic:** When `i=3`, `nums[0]` (1) is removed *before* checking `nums[3]` (1). So, `window_set` becomes `{2,3}`. Then you check if `1` is in `{2,3}`. It's not. Then add `1`. So `window_set` becomes `{1,2,3}` again. This is the crucial point for the "within k distance" part. If `nums[i-k-1]` is removed *before* `nums[i]` is checked, then a duplicate at `i-k-1` and `i` (distance `k+1`) would correctly be missed.

Let's use a cleaner table for the refined strategy:
The `window_set` holds elements `nums[j]` where `i - j <= k` and `j < i`.
This means, for the current `nums[i]`, you care about elements `nums[i-1], nums[i-2], ..., nums[max(0, i-k)]`.
So, `window_set` should maintain elements in the range `[current_index - k, current_index - 1]`.

When iterating `i` from 0 to `n-1`:
1.  **Remove oldest element from window:** If `i > k`, then `nums[i - k - 1]` is no longer within distance `k` of the current `i` (or any future `i` in the window). Remove `nums[i - k - 1]` from `window_set`.
2.  **Check for duplicate:** If `nums[i]` is already in `window_set`, then a duplicate within distance `k` has been found. Return `true`.
3.  **Add current element to window:** Add `nums[i]` to `window_set`.

This means `window_set` always contains elements from `nums[max(0, i-k)]` to `nums[i]`. No, this is confusing.
Let's simplify: `window_set` will store `nums[j]` such that `j` is within the current active window. The window is `[i-k, i]`. So when you are at `i`, you need elements `[i-k, ..., i-1]` to check against `nums[i]`.

Simpler logic:
1. Initialize `seen_in_window = set()`.
2. Iterate `i` from `0` to `len(nums) - 1`.
3. **Before adding `nums[i]` to the window (and before checking for duplicates with it):** If `i` is greater than `k`, the element at index `i - k - 1` is now too far away from `i` to satisfy `abs(i - j) <= k`. So, remove `nums[i - k - 1]` from `seen_in_window`.
4. Check if `nums[i]` is already in `seen_in_window`. If it is, then `nums[i]` is a duplicate of an element within the `k` distance. Return `true`.
5. Add `nums[i]` to `seen_in_window`.

This logic makes `seen_in_window` contain `nums[j]` where `max(0, i - k) <= j < i`.
Let's trace `nums = [1, 2, 3, 1, 2, 3]`, `k = 2` with this logic.

Initial: `seen_in_window = set()`. `k=2`.

| `i` | `nums[i]` | Condition `i > k` | `seen_in_window.remove(nums[i-k-1])` | `nums[i]` in `seen_in_window`? | Action if True | `seen_in_window` after add | `res` |
|---|---|---|---|---|---|---|---|
| 0 | 1 | F (0 > 2 is F) | - | No | - | `{1}` | - |
| 1 | 2 | F (1 > 2 is F) | - | No | - | `{1, 2}` | - |
| 2 | 3 | F (2 > 2 is F) | - | No | - | `{1, 2, 3}` | - |
| 3 | 1 | T (3 > 2 is T) | Remove `nums[0]` (1). `seen_in_window` is now `{2, 3}`. | No | - | `{2, 3, 1}` | - |
| 4 | 2 | T (4 > 2 is T) | Remove `nums[1]` (2). `seen_in_window` is now `{3, 1}`. | No | - | `{3, 1, 2}` | - |
| 5 | 3 | T (5 > 2 is T) | Remove `nums[2]` (3). `seen_in_window` is now `{1, 2}`. | No | - | `{1, 2, 3}` | - |
| **End of loop** | - | - | - | - | - | - | `False` |

This trace finally matches the example output `false` for `nums = [1,2,3,1,2,3], k=2`. This logic is correct.

The time complexity is O(N) because you iterate through the array once, and each set operation (add, remove, check) takes average O(1) time. The space complexity is O(k) in the worst case, as the set will store at most `k+1` elements. Given `k` can be up to $10^5$, this is still O(N) space in the worst case, but it's optimal given the constraints.

