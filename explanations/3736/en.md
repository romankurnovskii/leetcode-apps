## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Array Size:** The array can have up to 100 elements, so we can use a simple approach.
  * **Value Range:** Each element is between 1 and 100.
  * **Time Complexity:** Finding the maximum takes $O(n)$, and calculating moves takes $O(n)$, so overall $O(n)$.
  * **Space Complexity:** $O(1)$ - we only need a few variables.
  * **Edge Case:** If all elements are already equal, the maximum equals all elements, so total moves is 0.

**High-level approach**
The problem asks us to find the minimum number of moves to make all elements equal, where each move increases a single element by 1.

  * Since we can only **increase** elements (not decrease), all elements must reach at least the **maximum value** in the array.
  * To minimize moves, we should make all elements equal to the maximum value (rather than a higher value).
  * For each element, the number of moves needed to reach the maximum is `max_val - element`.
  * The total moves is the sum of moves needed for all elements.

**Brute force vs. optimized strategy**

  * **Brute Force:** Try all possible target values and calculate moves for each. This would be inefficient.
  * **Optimized (Greedy):** Since we can only increase, the optimal target is the maximum value. Calculate moves for each element to reach this target. This is $O(n)$.

**Decomposition**

1.  **Find Maximum:** Identify the maximum value in the array.
2.  **Calculate Moves:** For each element, calculate how many moves are needed to reach the maximum value.
3.  **Sum Moves:** Sum all the individual moves to get the total.

### Steps

1.  **Find Maximum Value**
    Iterate through the array to find the maximum value. For example, in $[2,1,3]$, the maximum is 3.

2.  **Calculate Moves for Each Element**
    For each element $num$ in the array:
      * Calculate the difference: $max\_val - num$
      * This represents the number of moves needed to increase $num$ to $max\_val$
      * For $[2,1,3]$:
        * Element 2: $3 - 2 = 1$ move
        * Element 1: $3 - 1 = 2$ moves
        * Element 3: $3 - 3 = 0$ moves

3.  **Sum All Moves**
    Add up all the individual moves: $1 + 2 + 0 = 3$ total moves.

4.  **Return Result**
    Return the total number of moves.

