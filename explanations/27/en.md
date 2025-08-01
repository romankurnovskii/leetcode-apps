# 27. Remove Element

**Difficulty:** Easy  
**Link:** https://leetcode.com/problems/remove-element/

## Problem Description

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)**. The order of the elements may be changed. Then return *the number of elements in* `nums` *which are not equal to* `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

1. Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
2. Return `k`.

**Custom Judge:**

The judge will test your solution with the following code:

```
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be **accepted**.

**Example 1:**
```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**
```
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Constraints:**
- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

## Explanation

### Strategy

This is a **two-pointer array manipulation problem** that requires removing all occurrences of a specific value from an array in-place. The key insight is that we don't need to actually "remove" elements - we just need to move all non-target elements to the front of the array and return the count.

**Key observations:**
- We need to modify the array in-place without using extra space
- The order of elements can be changed
- We only care about the first `k` elements after removal
- We can use a two-pointer approach to overwrite elements efficiently

**High-level approach:**
1. **Use a slow pointer**: Points to the next position where we'll place a valid element
2. **Use a fast pointer**: Iterates through the array to find valid elements
3. **Copy valid elements**: When we find an element not equal to `val`, copy it to the slow pointer position
4. **Return the count**: The slow pointer position at the end gives us the count of valid elements

### Steps

Let's break down the solution step by step:

**Step 1: Initialize pointers**
- `slow`: Points to the next position where we'll place a valid element (starts at 0)
- `fast`: Iterates through the array to find elements (starts at 0)

**Step 2: Iterate through the array**
For each element at position `fast`:
- If `nums[fast] != val`, copy it to `nums[slow]` and increment `slow`
- If `nums[fast] == val`, skip it (just increment `fast`)

**Step 3: Return the result**
- The value of `slow` at the end gives us the count of elements not equal to `val`
- The first `slow` elements of the array contain all the valid elements

**Example walkthrough:**
Let's trace through the first example:

```
nums = [3,2,2,3], val = 3

Initial state:
slow = 0, fast = 0

Step 1: nums[0] = 3 == val
Skip 3, increment fast only
slow = 0, fast = 1

Step 2: nums[1] = 2 != val
Copy 2 to nums[0], increment both
nums = [2,2,2,3], slow = 1, fast = 2

Step 3: nums[2] = 2 != val
Copy 2 to nums[1], increment both
nums = [2,2,2,3], slow = 2, fast = 3

Step 4: nums[3] = 3 == val
Skip 3, increment fast only
slow = 2, fast = 4

Result: Return slow = 2
Final array: [2,2,_,_] (first 2 elements are valid)
```

> **Note:** The two-pointer approach is efficient because we only need one pass through the array. We don't need to actually remove elements - we just overwrite the positions where we want to keep elements.


**Time Complexity:** O(n) - we visit each element exactly once  
**Space Complexity:** O(1) - we modify the array in-place without extra space 