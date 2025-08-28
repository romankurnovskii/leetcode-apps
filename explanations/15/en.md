## 15. 3Sum [Medium]

https://leetcode.com/problems/3sum

## Description
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Examples**

```tex
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

**Constraints**
```tex
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
```

## Explanation

### Strategy
Let's restate the problem: You're given an array of integers and need to find all unique triplets that sum to zero. This is a classic **three-pointer problem** that builds upon the two-sum concept.

This is a **sorting + two-pointer problem** that requires careful handling of duplicates and efficient searching.

**What is given?** An array of integers that may contain duplicates.

**What is being asked?** Find all unique triplets that sum to zero, avoiding duplicate combinations.

**Constraints:** The array can be up to 3000 elements long, with values ranging from -100,000 to 100,000.

**Edge cases:** 
- Array with all zeros
- Array with many duplicates
- Array with no valid triplets
- Array with exactly 3 elements

**High-level approach:**
The solution involves three main steps:
1. **Sort the array**: This allows us to use two-pointer technique efficiently
2. **Fix one element**: Iterate through each unique element as the first number
3. **Two-pointer search**: Use two pointers to find pairs that sum to the negative of the fixed element

**Decomposition:**
1. **Sort the array**: Enables efficient two-pointer searching and helps avoid duplicates
2. **Iterate through unique elements**: Fix each element as the first number in the triplet
3. **Two-pointer search**: Use left and right pointers to find pairs that sum to the target
4. **Handle duplicates**: Skip duplicate elements to avoid duplicate triplets
5. **Return results**: Collect all valid triplets

**Brute force vs. optimized strategy:**
- **Brute force**: Check all possible combinations of three numbers. This takes O(n³) time.
- **Optimized**: Sort the array and use two-pointer technique for each fixed element. This takes O(n²) time.

### Steps
Let's walk through the solution step by step using the first example: `nums = [-1,0,1,2,-1,-4]`

**Step 1: Sort the array**
- Original: `[-1,0,1,2,-1,-4]`
- Sorted: `[-4,-1,-1,0,1,2]`

**Step 2: Fix first element and search for pairs**
- Fix `nums[0] = -4`
- Target for two-pointer search: `0 - (-4) = 4`
- Use two pointers: `left = 1`, `right = 5`
- `nums[left] + nums[right] = -1 + 2 = 1 < 4`, so move left pointer right
- `left = 2`, `nums[left] + nums[right] = -1 + 2 = 1 < 4`, so move left pointer right
- `left = 3`, `nums[left] + nums[right] = 0 + 2 = 2 < 4`, so move left pointer right
- `left = 4`, `nums[left] + nums[right] = 1 + 2 = 3 < 4`, so move left pointer right
- `left = 5`, but `left >= right`, so no valid pair found for `-4`

**Step 3: Fix next unique element**
- Fix `nums[1] = -1` (first occurrence)
- Target for two-pointer search: `0 - (-1) = 1`
- Use two pointers: `left = 2`, `right = 5`
- `nums[left] + nums[right] = -1 + 2 = 1 == 1`, found a triplet: `[-1,-1,2]`
- Move pointers: `left = 3`, `right = 4`
- `nums[left] + nums[right] = 0 + 1 = 1 == 1`, found another triplet: `[-1,0,1]`
- Continue until pointers cross

**Step 4: Skip duplicates**
- When moving to the next element, skip if it's the same as the previous one
- This prevents duplicate triplets

**Step 5: Continue for all elements**
- Repeat the process for each unique element
- Collect all valid triplets

**Why this works:**
By sorting the array, we can efficiently search for pairs using two pointers. For each fixed element `a`, we need to find pairs `b` and `c` such that `b + c = -a`. The two-pointer technique allows us to find these pairs in O(n) time for each fixed element, giving us an overall O(n²) solution.

> **Note:** The key insight is that sorting the array not only enables efficient searching but also helps us avoid duplicates by skipping identical elements.

**Time Complexity:** O(n²) - we iterate through each element and for each, we do a two-pointer search  
**Space Complexity:** O(1) - we only use a constant amount of extra space (excluding the output array)
