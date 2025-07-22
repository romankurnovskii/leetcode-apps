## 605. Can Place Flowers [Easy]

https://leetcode.com/problems/can-place-flowers

## Description
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in **adjacent** plots.

Given an integer array `flowerbed` containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer `n`, return `true` if `n` new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and `false` otherwise.

**Examples**
```text
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
```

**Constraints**
```text
1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
```

## Explanation

### Strategy
- **Type:** Array, Greedy
- **Given:** An array `flowerbed` of 0s and 1s, and an integer `n`
- **Asked:** Can you plant `n` new flowers in the flowerbed without any two flowers being adjacent?

#### What does "adjacent" mean?
- No two flowers (1s) can be next to each other. You can only plant at a 0 if both neighbors (or edges) are 0.

Let's imagine the flowerbed as a row of garden plots. You want to plant new flowers, but you can't put them right next to each other. So, for each empty spot, you check the spots to the left and right. If both are empty (or if you're at the edge), you can plant a flower there.

You do this because it's the only way to guarantee you never break the "no neighbors" rule. By checking each spot, you make sure you don't miss any possible planting locations.

You keep a count of how many flowers you've planted. If you reach the required number, you can stop early and return True. This helps us avoid unnecessary work and makes our solution efficient.

> Check each empty plot and see if both neighbors are empty (or out of bounds).

#### High-Level Plan
1. For each plot in the flowerbed, check if it is empty (0) and both neighbors are empty (or out of bounds).
2. If so, plant a flower there (set to 1) and decrease `n`.
3. If at any point `n` reaches 0, return True.
4. If you finish the loop and haven't planted enough, return False.

### Steps

Let's walk through an example: flowerbed = [1,0,0,0,1], n = 1

1. Start at index 0: already planted (1), skip.
2. Index 1: empty, but left is 1, can't plant.
3. Index 2: empty, left is 0, right is 0, can plant. Plant and set to 1, n becomes 0.
4. Since n == 0, return True.

> **Note:**
> - Always check both neighbors (or treat out-of-bounds as 0).
> - Stop early if n == 0 for efficiency.

- **Time Complexity:** O(m), where m is the length of flowerbed
- **Space Complexity:** O(1)