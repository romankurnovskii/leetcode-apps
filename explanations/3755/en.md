## Explanation

### Strategy

**Constraints & Edge Cases**

  * **Array Size:** Typically up to $10^5$.
  * **Time Complexity:** Since we are looking for a subarray, a nested loop approach (Brute Force) would be $O(N^2)$, which is too slow. We need a linear $O(N)$ pass.
  * **Edge Case:** A valid subarray might start from the very beginning (index 0). We need to handle this by initializing our state tracking with a "dummy" start point.

**High-level approach**
We are looking for a subarray that satisfies two conditions simultaneously: `XOR sum == 0` and `Odd Count == Even Count`.
We can track the "state" of the array at every index using **Prefix Logic**. If the state at index `i` is identical to the state at index `j` (where `j < i`), then the subarray between them (`j+1` to `i`) has "zeroed out" the changes, satisfying our conditions.

**Brute force vs. optimized strategy**

  * **Brute Force:** Iterate through every possible starting point `i` and ending point `j`, calculate the XOR and count odds/evens. This is inefficient.
  * **Optimized:** We use a Hash Map (Dictionary) to store the **first time** we encounter a specific state. As we iterate, if we see that state again, the distance between the current index and the stored index is a candidate for the maximum length.

**Decomposition**

1.  **Track XOR:** Maintain a running XOR of all numbers seen so far.
2.  **Track Balance:** Maintain a running "balance" score. Add 1 for an odd number, subtract 1 for an even number. If the balance doesn't change between two indices, the number of odds and evens added in between must be equal.
3.  **Map States:** Store the tuple `(current_xor, current_balance)` in a dictionary mapping to its index.

### Steps

1.  **Initialize Variables**
    We need `curr_xor` (starts at 0) and `balance` (starts at 0).
    We create a dictionary `seen` to store the first index where a specific state occurred.

      * *Crucial Step:* Initialize `seen[(0, 0)] = -1`. This represents the state before we start reading the array. It ensures that if a valid subarray starts at index 0, we can calculate its length correctly (`current_index - (-1)`).

2.  **Iterate Through the Array**
    Loop through `nums` using the index `i` and the value `num`.

3.  **Update State**

      * Update `curr_xor` by XORing it with `num`.
      * Check if `num` is odd or even:
          * If **Odd**: Increment `balance` (+1).
          * If **Even**: Decrement `balance` (-1).
      * *Concept:* The specific value of `balance` doesn't matter (it could be -5 or +100). What matters is that `balance` at index `i` equals `balance` at index `j`. This proves that between `j` and `i`, the net change in odd/even ratio is zero.

4.  **Check Dictionary**
    Create a key: `state = (curr_xor, balance)`.

      * **If `state` is already in `seen`:** This means we have encountered this exact scenario before. The subarray between the previous occurrence and now is valid.
          * Calculate `length = i - seen[state]`.
          * Update our result `res` if this length is the new maximum.
      * **If `state` is NOT in `seen`:** This is the first time we've encountered this particular combination of XOR and Balance. Store it: `seen[state] = i`.