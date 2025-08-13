Given an integer array `nums`, return an array `res` such that `res[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time complexity and without using the division operation.

**Examples**
```text
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

**Constraints:**
```text
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
```


## Explanation
The problem asks you to create a new array where each element at index `i` is the product of all numbers in the original array `nums` *except* the number at index `i` itself. You need to do this efficiently (O(n) time) and without using division.

Consider an element `nums[i]`. The product of all other elements can be thought of as the product of all elements *to its left* multiplied by the product of all elements *to its right*.

For example, if `nums = [a, b, c, d]`:
* For `a`, the result is `(product of nothing to its left) * (b * c * d)`.
* For `b`, the result is `(a) * (c * d)`.
* For `c`, the result is `(a * b) * (d)`.
* For `d`, the result is `(a * b * c) * (product of nothing to its right)`.

This insight leads to a two-pass approach.

### Strategy
You are given an integer array `nums`.
The goal is to return a new array `res` where `res[i]` is the product of all elements in `nums` except `nums[i]`.
Constraints are: O(n) time complexity and no division allowed.
This is an array manipulation problem.

**Constraints Analysis:**
* `2 <= nums.length <= 10^5`: The array will always have at least two elements, simplifying edge cases for empty or single-element arrays. The size suggests that an `O(n^2)` solution (e.g., nested loops) would be too slow.
* `-30 <= nums[i] <= 30`: Values are relatively small, but products can still grow large. The problem guarantees the product fits in a 32-bit integer, so overflow isn't an issue for the final product, but intermediate products might be. Python integers handle arbitrary size, so this is less of a concern in Python than in languages with fixed-size integers.
* "without using the division operation": This is the key constraint, ruling out the most straightforward approach of calculating the total product and then dividing.
* "O(n) time complexity": This means you generally want to iterate through the array a constant number of times (e.g., once or twice).

The high-level plan is to calculate prefix products and suffix products separately, then combine them.

**Decomposition:**
1.  **First Pass (Prefix Products):** Iterate from left to right. For each `nums[i]`, calculate the product of all elements *before* `nums[i]`. Store these products in an array.
2.  **Second Pass (Suffix Products):** Iterate from right to left. For each `nums[i]`, calculate the product of all elements *after* `nums[i]`.
3.  **Combine:** For each `nums[i]`, the final result will be the product of its corresponding prefix product and suffix product.

To optimize space, you can combine the suffix product calculation with the final multiplication into a single backward pass, using the `res` array (which would already hold the prefix products) to store the intermediate and final results. This makes the space complexity O(1) if you don't count the output array.

### Steps
Let's use the example `nums = [1, 2, 3, 4]` to illustrate the optimized two-pass approach.

You'll need an output array `res` of the same size as `nums`, initialized with 1s.

`res = [1, 1, 1, 1]`

**Step 1: Calculate Prefix Products (Left-to-Right Pass)**
We'll iterate from the beginning of `nums`. `res[i]` will store the product of all elements *to the left* of `nums[i]`. We'll use a variable, let's call it `current_product_from_left`, to keep track of the running product.

* Initialize `current_product_from_left = 1`.

* **i = 0 (nums[0] = 1):**
    * `res[0]` should store the product of elements to the left of `nums[0]`. There are none, so it's 1.
    * `res[0] = current_product_from_left` which is `1`. So `res` is now `[1, 1, 1, 1]`.
    * Update `current_product_from_left`: `current_product_from_left = current_product_from_left * nums[0] = 1 * 1 = 1`.

* **i = 1 (nums[1] = 2):**
    * `res[1]` should store the product of elements to the left of `nums[1]`, which is `nums[0]`. This is `current_product_from_left` (which is `1`).
    * `res[1] = current_product_from_left` which is `1`. So `res` is now `[1, 1, 1, 1]`.
    * Update `current_product_from_left`: `current_product_from_left = current_product_from_left * nums[1] = 1 * 2 = 2`.

* **i = 2 (nums[2] = 3):**
    * `res[2]` should store the product of elements to the left of `nums[2]`, which is `nums[0] * nums[1]`. This is `current_product_from_left` (which is `2`).
    * `res[2] = current_product_from_left` which is `2`. So `res` is now `[1, 1, 2, 1]`.
    * Update `current_product_from_left`: `current_product_from_left = current_product_from_left * nums[2] = 2 * 3 = 6`.

* **i = 3 (nums[3] = 4):**
    * `res[3]` should store the product of elements to the left of `nums[3]`, which is `nums[0] * nums[1] * nums[2]`. This is `current_product_from_left` (which is `6`).
    * `res[3] = current_product_from_left` which is `6`. So `res` is now `[1, 1, 2, 6]`.
    * Update `current_product_from_left`: `current_product_from_left = current_product_from_left * nums[3] = 6 * 4 = 24`.

After this first pass, `res` contains the prefix products: `[1, 1, 2, 6]`.
`current_product_from_left` is now 24.

**Step 2: Calculate Suffix Products and Final Result (Right-to-Left Pass)**
Now, you'll iterate from the end of `nums` backwards. `res[i]` already holds the prefix product. You will multiply this by the product of all elements *to the right* of `nums[i]`. You'll use another variable, `current_product_from_right`, to keep track of this running product.

* Initialize `current_product_from_right = 1`.

* **i = 3 (nums[3] = 4):**
    * `res[3]` (current value 6) needs to be multiplied by the product of elements to the right of `nums[3]`. There are none, so it's `current_product_from_right` (which is `1`).
    * `res[3] = res[3] * current_product_from_right = 6 * 1 = 6`. So `res` is now `[1, 1, 2, 6]`.
    * Update `current_product_from_right`: `current_product_from_right = current_product_from_right * nums[3] = 1 * 4 = 4`.

* **i = 2 (nums[2] = 3):**
    * `res[2]` (current value 2) needs to be multiplied by the product of elements to the right of `nums[2]`, which is `nums[3]`. This is `current_product_from_right` (which is `4`).
    * `res[2] = res[2] * current_product_from_right = 2 * 4 = 8`. So `res` is now `[1, 1, 8, 6]`.
    * Update `current_product_from_right`: `current_product_from_right = current_product_from_right * nums[2] = 4 * 3 = 12`.

* **i = 1 (nums[1] = 2):**
    * `res[1]` (current value 1) needs to be multiplied by the product of elements to the right of `nums[1]`, which is `nums[2] * nums[3]`. This is `current_product_from_right` (which is `12`).
    * `res[1] = res[1] * current_product_from_right = 1 * 12 = 12`. So `res` is now `[1, 12, 8, 6]`.
    * Update `current_product_from_right`: `current_product_from_right = current_product_from_right * nums[1] = 12 * 2 = 24`.

* **i = 0 (nums[0] = 1):**
    * `res[0]` (current value 1) needs to be multiplied by the product of elements to the right of `nums[0]`, which is `nums[1] * nums[2] * nums[3]`. This is `current_product_from_right` (which is `24`).
    * `res[0] = res[0] * current_product_from_right = 1 * 24 = 24`. So `res` is now `[24, 12, 8, 6]`.
    * Update `current_product_from_right`: `current_product_from_right = current_product_from_right * nums[0] = 24 * 1 = 24`.

The loop finishes. The `res` array `[24, 12, 8, 6]` is the correct answer.

This method achieves O(n) time complexity because it involves two passes over the array. It achieves O(1) space complexity because the only additional space used is a couple of variables and the output array itself (which doesn't count towards auxiliary space as per common interview interpretations for this problem).
