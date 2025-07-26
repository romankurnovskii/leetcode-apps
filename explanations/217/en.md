## 217. Contains Duplicate [Easy]
https://leetcode.com/problems/contains-duplicate/

## Description
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

**Examples**
```text
Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

**Constraints:**

```text
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
```


## Explanation
To determine if an array contains any duplicate values, you need to check if any number appears more than once. If every number is unique, then there are no duplicates.

### Strategy
You are given an array of integers, `nums`.
The problem asks you to return `true` if any value appears at least twice in `nums`, and `false` otherwise.
This is an array problem, specifically checking for uniqueness or duplicates.

**Constraints:**
* The length of `nums` is between 1 and 10^5.
* The values in `nums` can range from -10^9 to 10^9.

A simple way to detect duplicates is to keep track of all the numbers you've seen so far. If you encounter a number that you've already seen, then you've found a duplicate. If you go through the entire array without encountering any number you've already seen, then all elements are distinct.

To efficiently keep track of seen numbers, a hash set (or simply a "set" in Python) is a perfect data structure. Sets allow for very fast (average O(1) time) checking if an element exists within them and fast adding of new elements.

Here's the general approach:
1.  Create an empty set to store the numbers you encounter.
2.  Go through each number in the `nums` array.
3.  For each number:
    a.  Check if this number is already in your set.
    b.  If it is, you've found a duplicate! Immediately return `true`.
    c.  If it's not, add this number to your set so you remember that you've seen it.
4.  If you finish checking all numbers in the `nums` array and haven't returned `true` yet, it means no duplicates were found. So, return `false`.

### Steps

Let's walk through an example: `nums = [1, 2, 3, 1]`

1.  Initialize an empty set, let's call it `seen_numbers`.
    `seen_numbers = {}` (representing an empty set)

2.  Start iterating through `nums`:

    * **First number: `1`**
        * Is `1` in `seen_numbers`? No, it's empty.
        * Add `1` to `seen_numbers`.
        * `seen_numbers = {1}`

    * **Second number: `2`**
        * Is `2` in `seen_numbers`? No.
        * Add `2` to `seen_numbers`.
        * `seen_numbers = {1, 2}`

    * **Third number: `3`**
        * Is `3` in `seen_numbers`? No.
        * Add `3` to `seen_numbers`.
        * `seen_numbers = {1, 2, 3}`

    * **Fourth number: `1`**
        * Is `1` in `seen_numbers`? Yes, it is!
        * Since you found a duplicate, you can immediately stop and return `true`.

Let's consider another example: `nums = [1, 2, 3, 4]`

1.  Initialize `seen_numbers = {}`

2.  Start iterating through `nums`:

    * **First number: `1`**
        * Is `1` in `seen_numbers`? No.
        * Add `1` to `seen_numbers`.
        * `seen_numbers = {1}`

    * **Second number: `2`**
        * Is `2` in `seen_numbers`? No.
        * Add `2` to `seen_numbers`.
        * `seen_numbers = {1, 2}`

    * **Third number: `3`**
        * Is `3` in `seen_numbers`? No.
        * Add `3` to `seen_numbers`.
        * `seen_numbers = {1, 2, 3}`

    * **Fourth number: `4`**
        * Is `4` in `seen_numbers`? No.
        * Add `4` to `seen_numbers`.
        * `seen_numbers = {1, 2, 3, 4}`

3.  You have finished iterating through all numbers in `nums`. Since you never returned `true` inside the loop, it means no duplicates were found. Therefore, return `false`.

This approach ensures that you only store unique elements and can quickly check for existence, making it very efficient.
