## 283. Move Zeroes [Easy]

https://leetcode.com/problems/move-zeroes

## Description
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

**Examples**
```text
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: nums = [0]
Output: [0]
```

**Constraints**

```text
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1
```

## Explanation

### Strategy

This is an array manipulation problem. You are given an array `nums` and need to modify it. The key constraints are maintaining the relative order of non-zero elements and performing the operation in-place.

Let\'s think about how you can achieve this without creating a separate array. Imagine you want to collect all the non-zero elements at the beginning of the array, preserving their order. Once you\'ve done that, the remaining spots at the end of the array must be filled with zeros.

A general approach would be to have a pointer that tracks where the next non-zero element should be placed. Let\'s call this pointer `insert_pos`. You\'ll iterate through the entire array with another pointer (let\'s say `current_pos`). If the element at `current_pos` is non-zero, you move it to `nums[insert_pos]` and then increment `insert_pos`. If it\'s a zero, you simply skip it. After iterating through the entire array, `insert_pos` will point to the first position that should be a zero. From `insert_pos` to the end of the array, you can then fill all elements with zeros.

> Use two pointers: one to keep track of the current position to place a non-zero, and one to iterate through the array.

### Steps

Let\'s walk through an example: `nums = [0, 1, 0, 3, 12]`

1.  Initialize `insert_pos = 0`. This pointer will keep track of where the next non-zero element should go.
2.  Iterate through the array with a `current_pos` pointer:
    * `current_pos = 0`, `nums[0] = 0`. This is a zero. You do nothing with `insert_pos`.
        `nums` remains `[0, 1, 0, 3, 12]`, `insert_pos = 0`.
    * `current_pos = 1`, `nums[1] = 1`. This is non-zero.
        You place `nums[current_pos]` (which is 1) at `nums[insert_pos]` (which is `nums[0]`).
        So, `nums[0] = 1`.
        Then, increment `insert_pos`. `insert_pos` becomes `1`.
        `nums` is now `[1, 1, 0, 3, 12]`. (Note: the `1` at `nums[1]` is effectively overwritten, but you will deal with the leftover numbers later).
    * `current_pos = 2`, `nums[2] = 0`. This is a zero. You do nothing.
        `nums` remains `[1, 1, 0, 3, 12]`, `insert_pos = 1`.
    * `current_pos = 3`, `nums[3] = 3`. This is non-zero.
        You place `nums[current_pos]` (which is 3) at `nums[insert_pos]` (which is `nums[1]`).
        So, `nums[1] = 3`.
        Then, increment `insert_pos`. `insert_pos` becomes `2`.
        `nums` is now `[1, 3, 0, 3, 12]`.
    * `current_pos = 4`, `nums[4] = 12`. This is non-zero.
        You place `nums[current_pos]` (which is 12) at `nums[insert_pos]` (which is `nums[2]`).
        So, `nums[2] = 12`.
        Then, increment `insert_pos`. `insert_pos` becomes `3`.
        `nums` is now `[1, 3, 12, 3, 12]`.

    The loop finishes. At this point, `insert_pos = 3`. The non-zero elements `1, 3, 12` are now at the beginning of the array in their correct relative order. The remaining elements from `insert_pos` to the end (`nums[3]` and `nums[4]`) might contain old values, which you now need to overwrite with zeros.

3.  Fill the remaining positions with zeros:
    Start a loop from `insert_pos` up to `len(nums) - 1`.
    * `insert_pos = 3`. `nums[3] = 0`.
        `nums` is now `[1, 3, 12, 0, 12]`.
    * `insert_pos = 4`. `nums[4] = 0`.
        `nums` is now `[1, 3, 12, 0, 0]`.

    The loop finishes. The array is now `[1, 3, 12, 0, 0]`, which is the desired output.

---

Let\'s consider another example: `nums = [1, 0, 1]`

1.  Initialize `insert_pos = 0`.
2.  Iterate through the array:
    * `current_pos = 0`, `nums[0] = 1`. Non-zero.
        `nums[0] = 1`. `insert_pos` becomes `1`.
        `nums` is `[1, 0, 1]`.
    * `current_pos = 1`, `nums[1] = 0`. Zero. Do nothing.
        `nums` is `[1, 0, 1]`, `insert_pos = 1`.
    * `current_pos = 2`, `nums[2] = 1`. Non-zero.
        `nums[insert_pos]` (which is `nums[1]`) = `nums[current_pos]` (which is 1).
        So, `nums[1] = 1`.
        Then, increment `insert_pos`. `insert_pos` becomes `2`.
        `nums` is now `[1, 1, 1]`.

    The loop finishes. At this point, `insert_pos = 2`.

3.  Fill the remaining positions with zeros:
    Start a loop from `insert_pos` up to `len(nums) - 1`.
    * `insert_pos = 2`. `nums[2] = 0`.
        `nums` is now `[1, 1, 0]`.

    The loop finishes. The array is now `[1, 1, 0]`.

---

> The two-pointer solution that uses swapping (the first community explanation) is often considered more elegant and efficient because it potentially reduces the number of write operations compared to the two-pass approach where non-zeros are first moved and then zeros are filled. However, both achieve the desired time complexity.

**Time Complexity:** The solution involves two passes over the array. The first loop iterates $N$ times (where $N$ is the length of `nums`), and the second `while` loop iterates at most $N$ times. Therefore, the time complexity is $O(N) + O(N) = O(N)$.

**Space Complexity:** You are modifying the array in-place and not using any additional data structures that grow with the input size. Thus, the space complexity is $O(1)$.
