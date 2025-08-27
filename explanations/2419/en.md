## Description
You are given an integer array `nums` of size `n`.

Consider a **non-empty** subarray from `nums` that has the **maximum** possible **bitwise AND**.

- In other words, let `k` be the maximum value of the bitwise AND of **any** subarray of `nums`. Then, only subarrays with a bitwise AND equal to `k` should be considered.

Return the length of the longest such subarray. 

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A **subarray** is a contiguous sequence of elements within an array. 

```tex
Example 1:

Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation: 
The maximum possible bitwise AND of a subarray is 3. The longest subarray with that value is [3,3], so we return 2.

Example 2:
Input: nums = [1,2,3,4]
Output: 1 Explanation: The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.
```

```tex
Constraints: 1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
```

## Intuition

To maximize the AND of a subarray:

- The AND of elements can never be greater than any individual element.
- Hence, the **maximum bitwise AND** possible is just the maximum value in the array.

To find the longest subarray with this maximum AND:
- You must find the longest sequence of contiguous elements that are equal to this maximum value.

Why?

- Because ANDing the same maximum value repeatedly will still yield that value.
- As soon as a smaller number appears, the AND drops.

## Approach

1. Find the maximum value in the array `nums`.
2. Iterate through `nums`, and for each occurrence of the maximum:
    - Increase a counter `size`
    - Update `res` with the max of current length and `res`
3. If an element is **not equal to the max**, reset `size` to 0.
4. Return the final value of `res`.

This greedy scan ensures you only consider the longest run of maximum values.