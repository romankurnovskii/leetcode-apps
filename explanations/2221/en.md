## Explanation

### Strategy

**Restate the problem**  
Repeatedly replace the array with pairwise sums mod 10 until one element remains; return it.

**1.1 Constraints & Complexity**  
- **Input Size:** `1 <= n <= 1000`.  
- **Time Complexity:** O(n²) in the direct simulation (each layer shrinks by 1).  
- **Space Complexity:** O(n) for the working array.  
- **Edge Case:** n=1 → return the single value.

**1.2 High-level approach**  
Simulate the reduction: build a new array of length-1 from `(nums[i]+nums[i+1]) % 10` until length=1.  
![Layered triangular reduction](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Same as direct simulation — O(n²), acceptable for n=1000.  
- **Optimized:** Binomial-coefficient mod 10 approach exists, but simulation suffices.

**1.4 Decomposition**  
1. While `len(nums) > 1`:  
   - Build `newNums` of size `len(nums)-1` with `(nums[i]+nums[i+1])%10`.  
   - Assign `nums = newNums`.  
2. Return `nums[0]`.

### Steps

**2.1 Initialization & Example Setup**  
Example: `nums = [1,2,3,4,5]`.

**2.2 Start Checking**  
Layer 1: `[3,5,7,9]` → mod 10: `[3,5,7,9]`  
Layer 2: `[8,2,6]`  
Layer 3: `[0,8]`  
Layer 4: `[8]`

**2.3 Trace Walkthrough**  
| Layer | Array state    |
|-------|----------------|
| 0     | [1,2,3,4,5]    |
| 1     | [3,5,7,9]      |
| 2     | [8,2,6]        |
| 3     | [0,8]          |
| 4     | [8]            |

**2.4 Increment and Loop**  
Repeat until a single value remains.

**2.5 Return Result**  
Return the last value (8 in the example).

