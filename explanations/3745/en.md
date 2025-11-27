## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Array Size:** The input array has length between 3 and 100, so we can use sorting without performance concerns.
  * **Value Range:** Each element can be between -100 and 100, including negative numbers.
  * **Time Complexity:** Sorting takes $O(n \log n)$ where $n$ is the array length. Since $n \leq 100$, this is very efficient.
  * **Space Complexity:** Sorting creates a new array, so $O(n)$ space.
  * **Edge Case:** When all elements are the same, we still need three distinct indices, but the expression value will be the same regardless of which three we choose.

**High-level approach**
The problem asks us to maximize the expression $a + b - c$ where $a$, $b$, and $c$ are chosen from distinct indices in the array.

  * To maximize $a + b - c$, we want to:
    * Maximize $a$ and $b$ (the terms being added)
    * Minimize $c$ (the term being subtracted, so subtracting a smaller value gives a larger result)
  * Since we need distinct indices, we can simply:
    * Choose the two largest values for $a$ and $b$
    * Choose the smallest value for $c$

**Brute force vs. optimized strategy**

  * **Brute Force:** Try all possible combinations of three distinct indices, calculate $a + b - c$ for each, and return the maximum. This would be $O(n^3)$.
  * **Optimized (Greedy with Sorting):** Sort the array once, then take the two largest and smallest values. This is $O(n \log n)$ and much more efficient.

**Decomposition**

1.  **Sorting:** Sort the array in descending order to easily access the largest values at the beginning and smallest at the end.
2.  **Select Values:** Choose the first two elements (largest and second largest) for $a$ and $b$, and the last element (smallest) for $c$.
3.  **Calculate Expression:** Return $a + b - c$.

### Steps

1.  **Sort the Array**
    Sort the array in descending order. For example, if `nums = [1,4,2,5]`, after sorting we get `[5,4,2,1]`.

2.  **Identify Optimal Values**
    After sorting:
      * The first element (`sorted_nums[0]`) is the largest value - use this for $a$
      * The second element (`sorted_nums[1]`) is the second largest value - use this for $b$
      * The last element (`sorted_nums[-1]`) is the smallest value - use this for $c$

3.  **Calculate Maximum Expression**
    Compute and return $a + b - c$. For `[5,4,2,1]`: $5 + 4 - 1 = 8$.

4.  **Handle Negative Numbers**
    The same logic works with negative numbers. For `[-2,0,5,-2,4]`, sorted: `[5,4,0,-2,-2]`. We get $5 + 4 - (-2) = 11$, which maximizes the expression by subtracting the smallest (most negative) value.

