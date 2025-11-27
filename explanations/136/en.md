## Explanation

### Strategy (The "Why")

Given a non-empty array of integers where every element appears twice except for one element which appears once, we need to find that single element.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be between $1$ and $3 \times 10^4$.
- **Value Range:** Each element is between $-3 \times 10^4$ and $3 \times 10^4$.
- **Time Complexity:** $O(n)$ - We iterate through the array once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for the result variable.
- **Edge Case:** If the array has only one element, that element is the answer.

**1.2 High-level approach:**

The goal is to find the single element that appears only once.

![Single Number](https://assets.leetcode.com/uploads/2021/03/15/screen-shot-2021-03-15-at-11-27-17-am.png)

We use the XOR (exclusive or) operation. The key property is that $a \oplus a = 0$ and $a \oplus 0 = a$. So XORing all numbers together will cancel out pairs, leaving only the single number.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Use a hash map to count occurrences of each number, then find the one with count 1. This takes $O(n)$ time and $O(n)$ space.
- **Optimized Strategy (XOR):** XOR all numbers together. Pairs cancel out, leaving only the single number. This takes $O(n)$ time and $O(1)$ space.
- **Why it's better:** The XOR approach uses $O(1)$ extra space instead of $O(n)$ for a hash map, while maintaining the same time complexity.

**1.4 Decomposition:**

1. Initialize result to 0.
2. Iterate through each number in the array.
3. XOR each number with the result.
4. Return the final result (which is the single number).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [2, 2, 1]$

We initialize:
- `res = 0`

**2.2 Start Processing:**

We iterate through each number.

**2.3 Trace Walkthrough:**

| Number | Operation | Result |
|--------|-----------|--------|
| 2 | $0 \oplus 2 = 2$ | 2 |
| 2 | $2 \oplus 2 = 0$ | 0 |
| 1 | $0 \oplus 1 = 1$ | 1 |

**2.4 Explanation:**

- First 2: $0 \oplus 2 = 2$ (stored)
- Second 2: $2 \oplus 2 = 0$ (cancels out)
- 1: $0 \oplus 1 = 1$ (the single number)

**2.5 Return Result:**

We return 1, which is the single number that appears only once.

> **Note:** XOR has the properties: $a \oplus a = 0$, $a \oplus 0 = a$, and XOR is commutative and associative. This means all pairs cancel out, leaving only the single element.

