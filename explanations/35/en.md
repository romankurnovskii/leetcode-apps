## 35. Search Insert Position [Easy]
https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

**Examples**
```tex
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
```

**Constraints:**
```tex
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
```

## Explanation
You're given a list of distinct numbers, `nums`, that's already sorted from smallest to largest. You also have a `target` number. Your job is to find the `target` in the list. If you find it, you should give its position (index). If the `target` isn't in the list, you need to tell where it *would* be if you inserted it to keep the list sorted. You need to do this efficiently, in `O(log n)` time.

### Strategy
You are given a sorted array of distinct integers `nums` and a `target` value.
The problem asks for the index of `target` if found, or its insertion position if not found. The requirement for `O(log n)` runtime complexity strongly suggests using **Binary Search**.

**Constraints Analysis:**
* `1 <= nums.length <= 10^4`: Typical range for binary search.
* `nums contains distinct values sorted in ascending order`: Perfect conditions for binary search.
* The problem implicitly asks for the "first greater than or equal to" element if the target is not exactly found.

The core idea of binary search applies here. We'll repeatedly divide the search space in half. The main difference from a standard "find element" binary search is what happens when the `target` is not found. When the loop ends (`left > right`), the `left` pointer will be at the correct insertion point for the `target`.

* If `target` is found: return its index.
* If `target` is not found: The loop `while left <= right` will terminate when `left` is greater than `right`. At this point, `left` indicates the index where the `target` should be inserted to maintain the sorted order. This is because `left` always moves to `mid + 1` when `nums[mid] < target`, meaning it searches for a larger or equal value. `right` always moves to `mid - 1` when `nums[mid] > target`, meaning it searches for a smaller or equal value. When `left` crosses `right`, `left` will point to the first element greater than `target`, or `len(nums)` if `target` is greater than all elements.

**Decomposition:**
1.  Initialize two pointers: `left` to 0 (the first index) and `right` to `len(nums) - 1` (the last index).
2.  Start a loop that continues as long as `left` is less than or equal to `right`.
3.  Inside the loop:
    a.  Calculate the `mid` index: `mid = left + (right - left) // 2`. (This avoids potential overflow if `left + right` were huge, though less critical in Python).
    b.  Compare `nums[mid]` with `target`:
        i.  If `nums[mid] == target`, you found it! Return `mid`.
        ii. If `nums[mid] < target`, the `target` must be in the right half (or is greater than all elements). Update `left = mid + 1`. This makes `left` potentially the insertion point.
        iii. If `nums[mid] > target`, the `target` must be in the left half. Update `right = mid - 1`. This also makes `left` the candidate for insertion point if no exact match is found (because `right` moves before `left` in this case).
4.  If the loop finishes (meaning `left > right`), the `target` was not found. The `left` pointer now holds the correct index where the `target` should be inserted. Return `left`.

### Steps
Let's use the example `nums = [1, 3, 5, 6]`, `target = 2`

1.  Initialize `left = 0`, `right = 3`.
    `nums` is `[1, 3, 5, 6]`

2.  **Loop 1 (`left <= right` is `0 <= 3`, True):**
    * `mid = 0 + (3 - 0) // 2 = 1`.
    * `nums[mid]` is `nums[1] = 3`.
    * `3 > 2` (i.e., `nums[mid] > target`).
    * Target is in the left half. Update `right = mid - 1 = 1 - 1 = 0`.
    * Current search space: `left = 0`, `right = 0`. (Effectively `[1]`)

3.  **Loop 2 (`left <= right` is `0 <= 0`, True):**
    * `mid = 0 + (0 - 0) // 2 = 0`.
    * `nums[mid]` is `nums[0] = 1`.
    * `1 < 2` (i.e., `nums[mid] < target`).
    * Target is in the right half. Update `left = mid + 1 = 0 + 1 = 1`.
    * Current search space: `left = 1`, `right = 0`.

4.  **Loop 3 (`left <= right` is `1 <= 0`, False):**
    * The condition `left <= right` is no longer met. The loop terminates.
    * Return `left`, which is `1`.

This result `1` is correct: if `2` were inserted into `[1, 3, 5, 6]`, it would go at index 1: `[1, 2, 3, 5, 6]`.

Let's trace `nums = [1, 3, 5, 6]`, `target = 7`

1.  Initialize `left = 0`, `right = 3`.

2.  **Loop 1 (`0 <= 3`, True):**
    * `mid = 1`. `nums[1] = 3`.
    * `3 < 7`. `left = 1 + 1 = 2`.
    * `left = 2`, `right = 3`. (Effectively `[5, 6]`)

3.  **Loop 2 (`2 <= 3`, True):**
    * `mid = 2 + (3 - 2) // 2 = 2`.
    * `nums[2] = 5`.
    * `5 < 7`. `left = 2 + 1 = 3`.
    * `left = 3`, `right = 3`. (Effectively `[6]`)

4.  **Loop 3 (`3 <= 3`, True):**
    * `mid = 3 + (3 - 3) // 2 = 3`.
    * `nums[3] = 6`.
    * `6 < 7`. `left = 3 + 1 = 4`.
    * `left = 4`, `right = 3`.

5.  **Loop 4 (`4 <= 3`, False):**
    * Loop terminates.
    * Return `left`, which is `4`.

This is also correct: `7` would be inserted at index 4 (the end of the array): `[1, 3, 5, 6, 7]`.

This binary search approach has a time complexity of `O(log n)` because it halves the search space in each iteration. The space complexity is `O(1)` as it uses a constant amount of extra memory for pointers.
