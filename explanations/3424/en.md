## 3424. Minimum Cost to Make Arrays Identical [Medium]

https://leetcode.com/problems/minimum-cost-to-make-arrays-identical

## Description

You are given two integer arrays `arr` and `brr` of length `n`, and an integer `k`. You can perform the following operations on `arr` any number of times:

- Split `arr` into any number of **contiguous** subarrays and rearrange these subarrays in any order. This operation has a fixed cost of `k`.
- Choose any element in `arr` and add or subtract a positive integer `x` to it. The cost of this operation is `x`.

Return the **minimum** total cost to make `arr` **equal** to `brr`.

**Examples**

**Example 1:**

Input: arr = [-7,9,5], brr = [7,-2,-5], k = 2

Output: 13

Explanation:
- Split `arr` into two contiguous subarrays: `[-7]` and `[9, 5]` and rearrange them as `[9, 5, -7]`, with a cost of 2.
- Subtract 2 from element `arr[0]`. The array becomes `[7, 5, -7]`. The cost of this operation is 2.
- Subtract 7 from element `arr[1]`. The array becomes `[7, -2, -7]`. The cost of this operation is 7.
- Add 2 to element `arr[2]`. The array becomes `[7, -2, -5]`. The cost of this operation is 2.

The total cost to make the arrays equal is 2 + 2 + 7 + 2 = 13.

**Example 2:**

Input: arr = [2,1], brr = [2,1], k = 0

Output: 0

Explanation:
Since the arrays are already equal, no operations are needed, and the total cost is 0.

**Constraints**

```tex
1 <= arr.length == brr.length <= 10^5
0 <= k <= 2 * 10^10
-10^5 <= arr[i] <= 10^5
-10^5 <= brr[i] <= 10^5
```
## Explanation

### Strategy

Let's restate the problem:
- We have two arrays, `arr` and `brr`, and a cost `k` for rearranging contiguous subarrays of `arr`.
- We can also change any element in `arr` to any value (at a cost equal to the absolute difference).
- Our goal is to make `arr` exactly equal to `brr` with the minimum total cost.

**Type:** Array, Greedy, Sorting

**What is being asked?**
- Make `arr` and `brr` identical, using the allowed operations, at the lowest possible cost.

**What is given?**
- Two arrays of equal length, and a rearrangement cost `k`.

**Constraints/Edge Cases:**
- Arrays can be large (up to 10^5 elements).
- Rearrangement can be done any number of times, but each time costs `k`.
- Changing elements is always possible, but can be expensive if values are far apart.

**High-Level Plan:**
- There are two main strategies:
  1. Change each element in place (no rearrangement).
  2. Rearrange `arr` (using the split operation) to best match `brr`, then change elements as needed.
- Rearranging allows us to sort both arrays and match smallest-to-smallest, largest-to-largest, minimizing the sum of differences. But we must pay the rearrangement cost `k`.
- We want the minimum of these two approaches.

### Steps

1. **Calculate the cost without rearrangement:**
   - For each index, compute `abs(arr[i] - brr[i])` and sum up.
2. **Calculate the cost with rearrangement:**
   - Sort both arrays.
   - For each index, compute `abs(sorted_arr[i] - sorted_brr[i])` and sum up.
   - Add the rearrangement cost `k`.
3. **Return the minimum of the two costs.**

**Example Walkthrough:**

Suppose `arr = [-7,9,5]`, `brr = [7,-2,-5]`, `k = 2`.

- Cost without rearrangement:
  - abs(-7 - 7) = 14
  - abs(9 - -2) = 11
  - abs(5 - -5) = 10
  - Total = 14 + 11 + 10 = 35

- Cost with rearrangement:
  - Sort arr: [-7, 5, 9]
  - Sort brr: [-5, -2, 7]
  - abs(-7 - -5) = 2
  - abs(5 - -2) = 7
  - abs(9 - 7) = 2
  - Total = 2 + 7 + 2 = 11
  - Add rearrangement cost: 11 + 2 = 13

- Minimum cost = min(35, 13) = 13

> **Note:** Rearrangement is only worth it if the cost saved by optimal matching exceeds the rearrangement cost `k`.
