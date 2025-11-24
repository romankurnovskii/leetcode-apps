## Explanation

### Strategy

**Constraints & Edge Cases**
We are dealing with string lengths ($n$) and query counts ($q$) up to 100,000.

  * **Time Complexity:** A solution that loops through the substring for every query will be $O(n \cdot q)$, which is far too slow. We need an $O(1)$ solution per query.
  * **Large Numbers:** The resulting numbers can be massive. We must apply modulo $10^9 + 7$ at every addition or multiplication step.
  * **Zeros:** The problem asks us to ignore zeros. If a range contains only zeros, our logic needs to handle returning 0 gracefully.

**High-level approach**
We will use the **Prefix Sum** technique, adapted for string concatenation. Instead of just summing numbers, we will maintain a "rolling hash" or "prefix value" that represents the integer formed by the string up to index $i$. To get a specific substring's value, we take the total value up to the end of the range and mathematically "subtract" the prefix before the range.

**Brute force vs. optimized strategy**

  * **Brute Force:** For each query, slice the string `s[l:r+1]`, filter out '0', parse to int, and multiply. This involves heavy string manipulation inside a loop.
  * **Optimized:** Precompute three arrays: one for the concatenated value, one for the count of non-zero digits, and one for the simple sum of digits. We can then solve any query instantly using modular arithmetic.

**Decomposition**

1.  **Map the Data:** Create prefix arrays that track the state of the string (value, count, sum) at every index.
2.  **Precompute Powers:** Calculate powers of 10 beforehand so we can "shift" numbers left efficiently.
3.  **Query Logic:** For each query, use the prefix arrays to isolate the target number and calculate the final result.

### Steps

1.  **Initialize Prefix Arrays**
    We need three arrays of size $N+1$. We use $N+1$ to make 1-based indexing easier (index $i$ represents the state *after* processing character $i-1$).

      * `p_val`: The integer value of all non-zero digits concatenated so far.
      * `p_cnt`: The total count of non-zero digits encountered so far.
      * `p_sum`: The simple arithmetic sum of non-zero digits so far.

2.  **Build the Prefixes**
    Iterate through the string `s`.

      * If the character is `'0'`, the state doesn't change. Copy the values from index $i$ to $i+1$.
      * If it's a non-zero digit $d$:
          * Update sum: `new_sum = old_sum + d`.
          * Update count: `new_cnt = old_count + 1`.
          * Update value: Append the digit by shifting the old value left (multiply by 10) and adding $d$. Formula: `(old_val * 10 + d) % MOD`.

3.  **Precompute Powers of 10**
    To perform the "subtraction" logic later, we need to know what $10^k$ is for any $k$. Since we are working with modular arithmetic, we cannot just use `10 ** k` inside the loop (it's too slow). We precompute an array `pow10` where `pow10[k]` holds $10^k \pmod M$.

4.  **Calculate Query Results**
    For each query `[l, r]`:

      * **Step A (Simple Stats):** Calculate the number of non-zero digits (`cnt`) and their sum (`d_sum`) by subtracting the value at index $l$ from the value at index $r+1$.
      * **Step B (Extract Number):** We have the full prefix ending at `r` (`full`) and the prefix ending before `l` (`prev`). To isolate the middle part, we must subtract `prev` from `full`.
      * *Crucial Logic:* To align them correctly, `prev` must be shifted left by `cnt` positions.
      * Formula: `target = (full - (prev * pow10[cnt])) % MOD`.
      * **Step C:** Multiply `target` by `d_sum` and store it in `res`.
