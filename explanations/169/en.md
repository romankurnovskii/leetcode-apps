## 169. Majority Element [Easy]
https://leetcode.com/problems/majority-element/

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `n / 2` times.

You may assume that the majority element always exists in the array.

**Examples**
<code>
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
</code>

**Constraints:**
<code>
n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
</code>

## Explanation
You are given an array of numbers, `nums`. The array has a special property: one number appears more than half the time (more than `n / 2` times, where `n` is the total number of elements in the array). Your goal is to find this "majority element". You are guaranteed that such an element always exists.

### Strategy
You are given an integer array `nums`.
The problem asks you to find the "majority element", which is the number that appears more than `n / 2` times.
This is an array problem, specifically one that involves counting or frequency.

**Constraints:**
* `n == nums.length`: Confirms `n` is the array length.
* `1 <= n <= 5 * 10^4`: The array size can be up to 50,000, suggesting an O(n) or O(n log n) solution is efficient enough.
* `-10^9 <= nums[i] <= 10^9`: Numbers can be large, but their values don't directly affect the counting strategy.
* "The majority element always exists": This is a crucial guarantee, meaning you don't have to handle cases where no majority element is found.

One straightforward approach is to count the occurrences of each number. A dictionary (hash map) is ideal for this, as it allows you to store key-value pairs where the key is the number and the value is its count.

Here's the general approach:
1.  Create an empty dictionary, say `counts`, to store the frequency of each number.
2.  Iterate through each number in the `nums` array.
3.  For each number:
    a.  Increment its count in the `counts` dictionary. If the number is encountered for the first time, initialize its count to 1.
    b.  Immediately check if the count for this number has exceeded `n / 2`.
    c.  If it has, this number is the majority element. Return it.
4.  Since the problem guarantees a majority element always exists, you will always find and return it within the loop.

### Steps
Let's use the example `nums = [2, 2, 1, 1, 1, 2, 2]`

1.  Determine `n`: `len(nums)` is 7. So `n = 7`.
    The majority element must appear more than `7 / 2 = 3.5` times, meaning at least 4 times.

2.  Initialize an empty dictionary: `counts = {}`

3.  Start iterating through `nums`:

    * **num = 2**
        * `counts` does not have `2`. Add `2` with count `1`. `counts = {2: 1}`.
        * `counts[2]` (1) is not greater than `3.5`.

    * **num = 2**
        * `counts` has `2`. Increment its count. `counts = {2: 2}`.
        * `counts[2]` (2) is not greater than `3.5`.

    * **num = 1**
        * `counts` does not have `1`. Add `1` with count `1`. `counts = {2: 2, 1: 1}`.
        * `counts[1]` (1) is not greater than `3.5`.

    * **num = 1**
        * `counts` has `1`. Increment its count. `counts = {2: 2, 1: 2}`.
        * `counts[1]` (2) is not greater than `3.5`.

    * **num = 1**
        * `counts` has `1`. Increment its count. `counts = {2: 2, 1: 3}`.
        * `counts[1]` (3) is not greater than `3.5`.

    * **num = 2**
        * `counts` has `2`. Increment its count. `counts = {2: 3, 1: 3}`.
        * `counts[2]` (3) is not greater than `3.5`.

    * **num = 2**
        * `counts` has `2`. Increment its count. `counts = {2: 4, 1: 3}`.
        * `counts[2]` (4) *is* greater than `3.5`!
        * Return `2`.

This method is efficient because dictionary operations (insertion, lookup, update) take average O(1) time. Since you iterate through the array once, the total time complexity is O(n). The space complexity is O(k) where k is the number of unique elements in `nums`. In the worst case (all elements are unique except the majority element), k could be O(n).

