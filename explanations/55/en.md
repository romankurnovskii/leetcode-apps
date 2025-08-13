You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` *if you can reach the last index, or* `false` *otherwise*.

**Example 1:**

```text
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**
```text
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

**Constraints:**
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Explanation

### Strategy

This is a **greedy algorithm problem** that requires determining if we can reach the last index. The key insight is to track the maximum reachable position and update it as we iterate through the array.

**Key observations:**
- We need to track the maximum position we can reach from any index
- If we can reach position i, we can reach any position up to i + nums[i]
- If we can't reach the current position, we can't reach the end
- We only need to check if we can reach the last index

**High-level approach:**
1. **Track maximum reachable position**: Keep track of the farthest position we can reach
2. **Iterate through array**: For each position, check if we can reach it
3. **Update maximum reach**: If we can reach current position, update maximum reach
4. **Check completion**: If we can reach the last position, return true

### Steps

Let's break down the solution step by step:

**Step 1: Initialize variables**
- `max_reach = 0`: Track the maximum position we can reach

**Step 2: Iterate through the array**
For each position `i`:
- Check if we can reach position `i`: `if i > max_reach, return false`
- Update maximum reach: `max_reach = max(max_reach, i + nums[i])`

**Step 3: Return result**
- If we complete the loop, return `true`

**Example walkthrough:**
Let's trace through the first example:

```text
nums = [2,3,1,1,4]

Initial state:
max_reach = 0

Step 1: i = 0
Can reach position 0? Yes (0 <= 0)
max_reach = max(0, 0 + 2) = 2

Step 2: i = 1
Can reach position 1? Yes (1 <= 2)
max_reach = max(2, 1 + 3) = 4

Step 3: i = 2
Can reach position 2? Yes (2 <= 4)
max_reach = max(4, 2 + 1) = 4

Step 4: i = 3
Can reach position 3? Yes (3 <= 4)
max_reach = max(4, 3 + 1) = 4

Step 5: i = 4
Can reach position 4? Yes (4 <= 4)
max_reach = max(4, 4 + 4) = 8

Result: Return true (can reach last position)
```

> **Note:** The greedy approach works because if we can reach position i, we can reach any position up to i + nums[i]. This means we only need to track the maximum reachable position, not the specific path.

**Time Complexity:** O(n) - we visit each element exactly once  
**Space Complexity:** O(1) - we only use a constant amount of extra space 