## Explanation

### Strategy

**Constraints & Edge Cases**

* **Array Size:** nums has length 1-1000, with values 0-9. We repeatedly reduce the array until only one element remains.
* **Time Complexity:** We perform n-1 iterations, and each iteration processes the current array. Total operations are roughly O(n²). **Time Complexity: O(n²)**, **Space Complexity: O(n)** for the new array.
* **Edge Case:** If nums has only one element, return that element directly.

**High-level approach**

The problem asks us to repeatedly create a new array where each element is `(nums[i] + nums[i+1]) % 10`, until only one element remains. This is similar to computing a triangular sum.

**Brute force vs. optimized strategy**

* **Brute Force:** This is what we do - simulate the process step by step. There's no more efficient way for this problem.
* **Optimized:** We can optimize space by reusing the array, but the time complexity remains the same.

**Decomposition**

1. **Iterate:** While array length > 1, create a new array.
2. **Compute Pairs:** For each adjacent pair, compute `(nums[i] + nums[i+1]) % 10`.
3. **Update:** Replace nums with the new array.
4. **Return:** When length is 1, return that element.

### Steps

1. **Initialization & Example Setup**
   Let's use `nums = [1,2,3,4,5]` as our example.

2. **First Iteration**
   - Create new array: `[(1+2)%10, (2+3)%10, (3+4)%10, (4+5)%10]`
   - `= [3, 5, 7, 9]`
   - Update: `nums = [3,5,7,9]`

3. **Trace Walkthrough**

| Iteration | nums | New Array Calculation | Result |
|-----------|------|----------------------|--------|
| 0         | [1,2,3,4,5] | [(1+2)%10, (2+3)%10, (3+4)%10, (4+5)%10] | [3,5,7,9] |
| 1         | [3,5,7,9]   | [(3+5)%10, (5+7)%10, (7+9)%10] | [8,2,6] |
| 2         | [8,2,6]     | [(8+2)%10, (2+6)%10] | [0,8] |
| 3         | [0,8]       | [(0+8)%10] | [8] |

4. **Continue Until One Element**
   - Keep iterating until `len(nums) == 1`.

5. **Return Result**
   Return `nums[0] = 8`.
