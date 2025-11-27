## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Number Range:** The input $n$ can be up to $10^9$, so we need to handle large numbers efficiently.
  * **Time Complexity:** Converting to string takes $O(\log n)$, and processing digits takes $O(\log n)$, so overall $O(\log n)$.
  * **Space Complexity:** $O(\log n)$ for the string and result array.
  * **Edge Case:** If $n$ is a single digit (1-9), it's already a base-10 component, so return $[n]$.

**High-level approach**
The problem asks us to express a number as a sum of base-10 components using the fewest components possible.

  * A **base-10 component** is the product of a single digit (1-9) and a non-negative power of 10 (e.g., $500 = 5 \times 10^2$, $30 = 3 \times 10^1$, $7 = 7 \times 10^0$).
  * To minimize the number of components, we need to use each nonzero digit exactly once.
  * We break down the number digit by digit, starting from the rightmost (ones place).
  * Each nonzero digit contributes one base-10 component: $digit \times 10^{position}$.

**Brute force vs. optimized strategy**

  * **Brute Force:** Try all possible combinations of base-10 components. This would be exponential and inefficient.
  * **Optimized (Digit-by-Digit Decomposition):** Process each digit position independently. Each nonzero digit at position $i$ contributes exactly one component: $digit \times 10^i$. This is optimal because we use each digit exactly once, minimizing the number of components.

**Decomposition**

1.  **Convert to String:** Convert the number to a string to access individual digits.
2.  **Process Digits:** Iterate through digits from right to left (ones place to highest place).
3.  **Calculate Components:** For each nonzero digit, calculate its base-10 component.
4.  **Collect Components:** Add each component to the result list.
5.  **Return Descending Order:** Reverse the list to return components in descending order.

### Steps

1.  **Convert to String**
    Convert the integer $n$ to a string to access individual digits. For example, $n = 537$ becomes `"537"`.

2.  **Process Digits from Right to Left**
    Iterate through the string from the rightmost digit (ones place) to the leftmost digit:
      * For $n = 537$:
        * Position 2 (rightmost): digit = 7
        * Position 1: digit = 3
        * Position 0 (leftmost): digit = 5

3.  **Calculate Power of 10**
    For each digit at position $i$ (0-indexed from right), the power of 10 is $len(s) - 1 - i$:
      * Rightmost digit (position 2): power = $3 - 1 - 2 = 0$ → $10^0 = 1$
      * Middle digit (position 1): power = $3 - 1 - 1 = 1$ → $10^1 = 10$
      * Leftmost digit (position 0): power = $3 - 1 - 0 = 2$ → $10^2 = 100$

4.  **Build Components**
    For each nonzero digit, calculate the component: $digit \times 10^{power}$:
      * Digit 7 at power 0: $7 \times 1 = 7$
      * Digit 3 at power 1: $3 \times 10 = 30$
      * Digit 5 at power 2: $5 \times 100 = 500$

5.  **Return in Descending Order**
    Since we processed from right to left, we collected components in ascending order. Reverse the list to get descending order: $[500, 30, 7]$.

