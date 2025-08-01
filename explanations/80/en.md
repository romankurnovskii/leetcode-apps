# 80. Remove Duplicates from Sorted Array II

**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

## Problem Description

Given an integer array `nums` sorted in **non-decreasing order**, remove some duplicates **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** such that each unique element appears **at most twice**. The **relative order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` *after placing the final result in the first* `k` *slots of* `nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.

**Custom Judge:**

The judge will test your solution with the following code:

```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be **accepted**.

**Example 1:**
```
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**
```
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Constraints:**
- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in **non-decreasing** order.

## Explanation

### Strategy

This is a **two-pointer array manipulation problem** that requires removing duplicates from a sorted array while allowing each unique element to appear at most twice. This is a variation of the classic "remove duplicates" problem with a more lenient constraint.

**Key observations:**
- The array is sorted in non-decreasing order
- We can keep at most 2 occurrences of each unique element
- We need to maintain the relative order of elements
- We can use a two-pointer approach to efficiently remove excess duplicates

**High-level approach:**
1. **Use a slow pointer**: Points to the next position where we'll place a valid element
2. **Use a fast pointer**: Iterates through the array to find elements
3. **Track occurrences**: Keep track of how many times we've seen the current element
4. **Copy valid elements**: When we find a valid element (not exceeding 2 occurrences), copy it to the slow pointer position
5. **Return the count**: The slow pointer position at the end gives us the count of valid elements

### Steps

Let's break down the solution step by step:

**Step 1: Handle edge cases**
- If the array has less than 3 elements, return the length (no duplicates to remove)

**Step 2: Initialize pointers and counters**
- `slow`: Points to the next position where we'll place a valid element (starts at 2)
- `fast`: Iterates through the array to find elements (starts at 2)
- We start from index 2 because the first two elements are always valid

**Step 3: Iterate through the array**
For each element at position `fast`:
- If `nums[fast] != nums[slow-2]`, it's a new element or we haven't seen it twice yet
  - Copy it to `nums[slow]` and increment `slow`
- If `nums[fast] == nums[slow-2]`, we've already seen this element twice
  - Skip it (just increment `fast`)

**Step 4: Return the result**
- The value of `slow` at the end gives us the count of valid elements
- The first `slow` elements of the array contain all the valid elements in order

**Example walkthrough:**
Let's trace through the first example:

```
nums = [1,1,1,2,2,3]

Initial state:
slow = 2, fast = 2

Step 1: nums[2] = 1 == nums[0] = 1 (third occurrence)
Skip, increment fast only
slow = 2, fast = 3

Step 2: nums[3] = 2 != nums[0] = 1 (new element)
Copy 2 to nums[2], increment both
nums = [1,1,2,2,2,3], slow = 3, fast = 4

Step 3: nums[4] = 2 != nums[1] = 1 (second occurrence of 2)
Copy 2 to nums[3], increment both
nums = [1,1,2,2,2,3], slow = 4, fast = 5

Step 4: nums[5] = 3 != nums[2] = 2 (new element)
Copy 3 to nums[4], increment both
nums = [1,1,2,2,3,3], slow = 5, fast = 6

Result: Return slow = 5
Final array: [1,1,2,2,3,_]
```

> **Note:** The key insight is that we compare each element with the element two positions back in our result array. If they're different, it means we can include the current element (either it's new or we haven't seen it twice yet). If they're the same, we've already included this element twice.

**Time Complexity:** O(n) - we visit each element exactly once  
**Space Complexity:** O(1) - we modify the array in-place without extra space 