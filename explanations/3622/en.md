## 3622. Check Divisibility by Digit Sum and Product [Easy]

[https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/)

You are given a positive integer `n`. Determine whether `n` is divisible by the sum of the following two values:
- The **digit sum** of `n` (the sum of its digits).
- The **digit product** of `n` (the product of its digits).

Return `true` if `n` is divisible by this sum; otherwise, return `false`.

**Example 1:**
```
Input: n = 99
Output: true
Explanation:
Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.
```

**Example 2:**
```
Input: n = 23
Output: false
Explanation:
Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is false.
```


**Constraints:**
```
1 <= n <= 10^6
```

## Understanding

The problem asks you to take a number `n` and perform a specific divisibility check. First, you need to calculate two values from its digits: the sum of all its digits and the product of all its digits. Then, you add these two results together to get a final `total_divisor`. The goal is to determine if the original number `n` is perfectly divisible by this `total_divisor`.

For example, if `n = 99`:
1.  **Digit Sum:** `9 + 9 = 18`
2.  **Digit Product:** `9 * 9 = 81`
3.  **Total Divisor:** `18 + 81 = 99`
4.  **Check:** Is `99` divisible by `99`? Yes. So, the result is `true`.


## Initial Thoughts

A straightforward way to approach this is to first get the digits of the number. For beginners, converting the number to a string is often the most intuitive method.

1.  Convert the integer `n` into a string. For `n = 123`, you get `"123"`.
2.  Initialize two variables, `digit_sum = 0` and `digit_product = 1`.
3.  Iterate through each character of the string.
4.  In each iteration, convert the character back to an integer.
5.  Add this integer to `digit_sum` and multiply it with `digit_product`.
6.  After the loop, you will have the final sum and product.
7.  Calculate `total_divisor = digit_sum + digit_product`.
8.  Finally, check if `n % total_divisor == 0`.

This approach works fine but involves converting between data types (integer to string and back). A more traditional and often more performant method uses pure arithmetic.


## Identifying the Pattern

The core of this problem is breaking down an integer into its component parts (its digits). This doesn't involve complex data structures or algorithms like searching or sorting.

> **Clues:** The problem requires you to operate on the digits of a number. This immediately points to a fundamental programming pattern for processing numbers.

**Primary Pattern: Digit Manipulation**

This pattern uses arithmetic operations, specifically the modulo (`%`) and integer division (`//`) operators, to isolate each digit of a number. It's a standard and efficient technique for solving problems that involve analyzing a number's digits.


## Strategy

The arithmetic strategy avoids string conversions and relies on a loop to extract digits one by one from the end of the number.

1.  Store the original value of `n` in a separate variable, say `original_n`, because the process will modify `n`.
2.  Initialize `digit_sum = 0` and `digit_product = 1`.
3.  Start a `while` loop that continues as long as your temporary number is greater than 0.
4.  Inside the loop:
    * Get the last digit: `digit = n % 10`.
    * Update the sum: `digit_sum += digit`.
    * Update the product: `digit_product *= digit`.
    * Remove the last digit: `n //= 10`.
5.  When the loop finishes, `n` will be 0, and you'll have the complete `digit_sum` and `digit_product`.
6.  Calculate the `total_divisor = digit_sum + digit_product`.
7.  Return the result of the check: `original_n % total_divisor == 0`.

> **Note:** The problem constraints state `1 <= n`, which guarantees the `total_divisor` will never be zero, so you don't have to worry about a division-by-zero error. The smallest possible divisor comes from `n=1`, where sum=1, product=1, and `total_divisor`=2.

### Steps

Let's trace this process with the example `n = 23`.

**Initial State:**
* `original_n = 23`
* `n = 23` (the value we will modify)
* `digit_sum = 0`
* `digit_product = 1`

| `n` (current value) | Loop Condition  | `digit = n % 10` | `digit_sum` | `digit_product` | `n //= 10` |
| :------------------ | :-------------- | :--------------- | :---------- | :-------------- | :--------- |
| `23`                | `23 > 0` (True) | `3`              | `0 + 3 = 3` | `1 * 3 = 3`     | `2`        |
| `2`                 | `2 > 0` (True)  | `2`              | `3 + 2 = 5` | `3 * 2 = 6`     | `0`        |
| `0`                 | `0 > 0` (False) | (Loop ends)      |             |                 |            |

**Final Calculations:**
* `digit_sum` is `5`.
* `digit_product` is `6`.
* `total_divisor = 5 + 6 = 11`.
* **Check:** Is `23 % 11 == 0`? No, the remainder is 1.
* The function returns `false`.
