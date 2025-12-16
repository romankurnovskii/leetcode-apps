## Explanation

### Strategy

**Constraints & Edge Cases**

* **Array Length:** n can be 1 to 10^4. The array is defined as `arr[i] = 2*i + 1`, so it contains odd numbers: [1, 3, 5, 7, ...].
* **Time Complexity:** We iterate through at most n/2 elements to calculate operations. **Time Complexity: O(n)**, **Space Complexity: O(1)**.
* **Edge Case:** If n=1, the array is already equal ([1]), so operations = 0.

**High-level approach**

The problem asks for the minimum operations to make all array elements equal. Since we can only transfer 1 from one element to another, the target value must be the average of all elements. For an array of odd numbers starting from 1, the average is n.

**Brute force vs. optimized strategy**

* **Brute Force:** Simulate the operations step by step. This would be very slow.
* **Optimized:** Calculate the target value (which is n), then for each element less than target, calculate how many operations are needed to bring it to target. Since elements are symmetric, we only need to process half the array.

**Decomposition**

1. **Calculate Target:** The target value is n (the average).
2. **Count Operations:** For each element less than target, add (target - element) to the result.
3. **Return:** Since operations are symmetric, we can stop at the middle.

### Steps

1. **Initialization & Example Setup**
   Let's use `n = 3` as our example.
   - Array: `arr = [1, 3, 5]` (indices 0, 1, 2).
   - Target: `target = n = 3`.

2. **Calculate Operations**
   - Element at index 0: `current = 2*0 + 1 = 1`, needs `3 - 1 = 2` operations.
   - Element at index 1: `current = 2*1 + 1 = 3`, already equal to target.
   - We can stop here since elements are symmetric.

3. **Trace Walkthrough**

| Index i | current = 2*i+1 | target | Operations Needed | Running Total |
|---------|-----------------|--------|-------------------|---------------|
| 0       | 1               | 3      | 3 - 1 = 2         | 2             |
| 1       | 3               | 3      | 0 (stop)          | 2             |

4. **Mathematical Insight**
   For n=3: operations = (3-1) = 2.
   For n=6: operations = (6-1) + (6-3) + (6-5) = 5 + 3 + 1 = 9.

5. **Return Result**
   Return the total operations: 2 for n=3.
