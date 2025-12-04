## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= nums.length <= 1000`, `0 <= nums[i] < nums.length`.
- **Time Complexity:** O(n) where n is the length of nums - we iterate through the array once.
- **Space Complexity:** O(n) - we create a new array of the same size.
- **Edge Case:** All elements are distinct and form a valid permutation.

**1.2 High-level approach:**
The goal is to build an array where each element `ans[i] = nums[nums[i]]`. We iterate through the input array and use each element as an index to access another element.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - we need to access each element once, which is O(n) time.
- **Optimized Strategy:** Single pass through the array, building the result array directly.

**1.4 Decomposition:**
1. Create an empty result array.
2. Iterate through each index in the input array.
3. For each index `i`, access `nums[nums[i]]` and append it to the result.
4. Return the completed result array.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `nums = [0,2,1,5,3,4]`. We initialize `res = []`.

**2.2 Start Checking:**
We start at index 0 and process each element.

**2.3 Trace Walkthrough:**

| i | nums[i] | nums[nums[i]] | res |
|---|---------|---------------|-----|
| 0 | 0 | nums[0] = 0 | [0] |
| 1 | 2 | nums[2] = 1 | [0,1] |
| 2 | 1 | nums[1] = 2 | [0,1,2] |
| 3 | 5 | nums[5] = 4 | [0,1,2,4] |
| 4 | 3 | nums[3] = 5 | [0,1,2,4,5] |
| 5 | 4 | nums[4] = 3 | [0,1,2,4,5,3] |

**2.4 Increment and Loop:**
After processing each index, we move to the next index until we've processed all elements.

**2.5 Return Result:**
Return `res = [0,1,2,4,5,3]`, which is the built array.

