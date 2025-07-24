## 238. Product of Array Except Self [Medium]

https://leetcode.com/problems/product-of-array-except-self

## Description
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

**Examples**
```text
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

**Constraints**

```text
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.
```

### Strategy

The problem asks you to create a new array `res` where each `res[i]` is the product of all elements in the input array `nums` *except* for `nums[i]`. You have two crucial constraints: the algorithm must run in $O(N)$ time, and it must *not* use the division operation.

A naive approach might involve calculating the total product of all elements and then for each `res[i]`, dividing the total product by `nums[i]`. However, this is explicitly disallowed due to the "no division" rule. Even if allowed, it would run into issues if `nums[i]` is zero.

The optimal strategy involves a **two-pass approach** using constant extra space (excluding the output array `res`). The core idea is that for any `res[i]`, the product of all elements except `nums[i]` can be broken down into two parts:
1.  The product of all elements *to the left* of `nums[i]` (let\'s call this `left_product[i]`).
2.  The product of all elements *to the right* of `nums[i]` (let\'s call this `right_product[i]`).

So, `res[i] = left_product[i] * right_product[i]`.

You can calculate these two parts in two separate passes:

**Pass 1 (Left-to-Right):** You iterate from the beginning of the array. For each index `i`, you store the product of all elements encountered so far *before* `nums[i]` into `res[i]`. You start with an `initial_product` of `1`. For `res[0]`, the product to its left is `1`. For `res[1]`, it's `nums[0]`. For `res[2]`, it's `nums[0] * nums[1]`, and so on.

**Pass 2 (Right-to-Left):** You then iterate from the end of the array towards the beginning. You maintain a `current_right_product` (initialized to `1`). For each index `i`, you multiply the value already present in `res[i]` (which is `left_product[i]`) by `current_right_product`. After this multiplication, you update `current_right_product` by multiplying it with `nums[i]` (because `nums[i]` will now be to the left of the next position you process).

By the end of the second pass, each `res[i]` will correctly hold the product of elements to its left multiplied by the product of elements to its right, achieving the desired result without division and in $O(N)$ time and $O(1)$ extra space (if `res` array doesn't count as extra space, as per problem context).

### Steps

Let\'s walk through an example: `nums = [1,2,3,4]`
`n = 4`

1.  Initialize `res = [1, 1, 1, 1]` (an array of ones with the same length as `nums`).

2.  **First Pass (Left-to-Right): Calculate `left_products` into `res`.
    Initialize `left_product = 1`.

    * `i = 0`: 
        * `res[0] = left_product` (which is `1`). So `res = [1, 1, 1, 1]`.
        * `left_product = left_product * nums[0] = 1 * 1 = 1`.

    * `i = 1`: 
        * `res[1] = left_product` (which is `1`). So `res = [1, 1, 1, 1]`.
        * `left_product = left_product * nums[1] = 1 * 2 = 2`.

    * `i = 2`: 
        * `res[2] = left_product` (which is `2`). So `res = [1, 1, 2, 1]`.
        * `left_product = left_product * nums[2] = 2 * 3 = 6`.

    * `i = 3`: 
        * `res[3] = left_product` (which is `6`). So `res = [1, 1, 2, 6]`.
        * `left_product = left_product * nums[3] = 6 * 4 = 24`.

    After this pass, `res` is `[1, 1, 2, 6]`. This array currently holds the products of elements *to the left* of each index.

3.  **Second Pass (Right-to-Left): Incorporate `right_products` into `res`.
    Initialize `right_product = 1`.

    * `i = 3` (starts from `n-1`): 
        * `res[3] = res[3] * right_product` (which is `6 * 1 = 6`). So `res = [1, 1, 2, 6]`.
        * `right_product = right_product * nums[3] = 1 * 4 = 4`.

    * `i = 2`: 
        * `res[2] = res[2] * right_product` (which is `2 * 4 = 8`). So `res = [1, 1, 8, 6]`.
        * `right_product = right_product * nums[2] = 4 * 3 = 12`.

    * `i = 1`: 
        * `res[1] = res[1] * right_product` (which is `1 * 12 = 12`). So `res = [1, 12, 8, 6]`.
        * `right_product = right_product * nums[1] = 12 * 2 = 24`.

    * `i = 0`: 
        * `res[0] = res[0] * right_product` (which is `1 * 24 = 24`). So `res = [24, 12, 8, 6]`.
        * `right_product = right_product * nums[0] = 24 * 1 = 24`.

    The loop finishes.

4.  The final `res` array is `[24, 12, 8, 6]`, which is the correct output.


**Time Complexity:** The algorithm performs two separate passes over the `nums` array. Each pass iterates `N` times (where `N` is the length of `nums`). The operations within each loop are constant time ($O(1)$). Therefore, the total time complexity is $O(N) + O(N) = O(N)$.

**Space Complexity:** The problem statement specifies that the output array does not count as extra space. You only use a few additional variables (`n`, `left_product`, `right_product`, `i`), which take constant space. Therefore, the space complexity is $O(1)$.



