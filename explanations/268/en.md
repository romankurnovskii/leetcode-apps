## 268. Missing Number [Easy]
https://leetcode.com/problems/missing-number/

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

**Examples**
```tex
Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
```

**Constraints:**
```tex
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.
```

## Explanation
You are given an array `nums` which contains `n` distinct numbers. These numbers are supposed to be from the range `[0, n]`. This means if `n` is 3, the numbers should be `0, 1, 2, 3`. However, the array `nums` only has `n` numbers, implying exactly one number from this range is missing. Your task is to find that missing number.

### Strategy
You are given an integer array `nums`.
The problem asks you to find the single missing number in the range `[0, n]`, where `n` is the length of `nums`.
This is an array problem, specifically a search or finding a discrepancy problem.

**Constraints:**
* `n == nums.length`: This is important, it tells you the size of the range `[0, n]` is one more than the length of the array.
* `1 <= n <= 10^4`: The array size is reasonable, an O(n) or O(n log n) solution will work.
* `0 <= nums[i] <= n`: Numbers are within the expected range.
* `All the numbers of nums are unique`: This simplifies things; you don't need to worry about duplicate numbers *within* the given array.

The most intuitive way to think about this is that if you had all the numbers from `0` to `n`, their sum would be a certain value. If you then sum the numbers you actually have in `nums`, the difference between the "expected sum" and the "actual sum" will be the missing number. This approach is simple, efficient, and easy to understand.

### Steps
Let's use the example `nums = [3, 0, 1]`

1.  **Determine `n`:** The length of `nums` is 3. So, `n = 3`. This means the full range of numbers should be `[0, 1, 2, 3]`.

2.  **Calculate the expected sum:**
    The sum of numbers from `0` to `n` (which is `0` to `3`) is `0 + 1 + 2 + 3 = 6`.
    You can use the formula for the sum of an arithmetic series: $n * (n + 1) / 2$.
    For `n = 3`, `expected_sum = 3 * (3 + 1) / 2 = 3 * 4 / 2 = 12 / 2 = 6`.

3.  **Calculate the actual sum of numbers in `nums`:**
    Sum the elements in `nums = [3, 0, 1]`: `3 + 0 + 1 = 4`.

4.  **Find the missing number:**
    The missing number is the difference between the `expected_sum` and the `actual_sum`.
    `missing_number = expected_sum - actual_sum = 6 - 4 = 2`.

    The result `res` is `2`.

Let's try another example: `nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]`

1.  **Determine `n`:** The length of `nums` is 9. So, `n = 9`. The full range of numbers should be `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`.

2.  **Calculate the expected sum:**
    For `n = 9`, `expected_sum = 9 * (9 + 1) / 2 = 9 * 10 / 2 = 90 / 2 = 45`.

3.  **Calculate the actual sum of numbers in `nums`:**
    Sum the elements in `nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]`:
    `9 + 6 + 4 + 2 + 3 + 5 + 7 + 0 + 1 = 37`.

4.  **Find the missing number:**
    `missing_number = expected_sum - actual_sum = 45 - 37 = 8`.

    The result `res` is `8`.

This approach is efficient because calculating the sum of the range takes constant time (using the formula), and summing the array takes O(n) time. Therefore, the overall time complexity is O(n). The space complexity is O(1) as you only need a few variables to store sums and `n`.
