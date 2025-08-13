A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

- For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`: `[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]`.

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the **next permutation** of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

- For example, the next permutation of `arr = [1,2,3]` is `[1,3,2]`.
- Similarly, the next permutation of `arr = [2,3,1]` is `[3,1,2]`.
- While the next permutation of `arr = [3,2,1]` is `[1,2,3]` because `[3,2,1]` does not have a lexicographical larger rearrangement.

Given an array of integers `nums`, *find the next permutation of* `nums`.

The replacement must be **in place** and use only constant extra memory.

**Examples**
```text
Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
```

**Constraints:**
```text
1 <= nums.length <= 100
0 <= nums[i] <= 100
```

**Primary Pattern: Array Manipulation**

## Understanding

You're given an array of numbers and need to find the next permutation in lexicographic order. Think of it like finding the next "word" in alphabetical order when all possible arrangements of the numbers are listed.

For example, if you have [1,2,3], the permutations in order are: [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]. So the next permutation after [1,2,3] is [1,3,2].

If you're already at the last permutation (like [3,2,1]), you wrap around to the first one ([1,2,3]).

## Strategy

### Identifying the Pattern

**Primary Pattern: Array Manipulation**

The clues that point to array manipulation are:
- You need to rearrange elements in an array to find the next lexicographic order
- The problem requires in-place modification of the array
- You need to understand the mathematical pattern of how permutations work
- The solution involves finding specific positions in the array and swapping elements

This is a classic array manipulation problem that requires understanding the mathematical properties of permutations and implementing a specific algorithm to find the next one.

### Steps

**Logic:** The key insight is that to find the next permutation, you need to:

1. Find the first decreasing element from the right (this is where we can make a change)
2. Find the smallest element on the right that is larger than this element
3. Swap these two elements
4. Reverse the suffix to get the smallest possible arrangement

**High-level approach:**
- Work from right to left to find the first decreasing element
- Find the next larger element to swap with
- Reverse the remaining elements to get the smallest possible suffix
- Handle the edge case where no next permutation exists

**Implementation steps:**
1. Find the first decreasing element from the right (i)
2. If no such element exists, reverse the entire array
3. Find the smallest element on the right of i that is larger than nums[i]
4. Swap nums[i] with this element
5. Reverse the subarray from i+1 to the end

> **Note:** The algorithm works because we want the smallest possible increase that creates a larger permutation. By finding the rightmost decreasing element and swapping it with the next larger element, then reversing the suffix, we get the lexicographically next permutation.
