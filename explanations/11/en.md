## Explanation

### Strategy (The "Why")

Given an array `height` of $n$ non-negative integers representing the heights of vertical lines, we need to find two lines that together with the x-axis form a container that holds the most water.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be between $2$ and $10^5$.
- **Value Range:** Each height is between $0$ and $10^4$.
- **Time Complexity:** $O(n)$ - We use two pointers that each traverse the array at most once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for pointers.
- **Edge Case:** If all heights are the same, the maximum area is determined by the two endpoints.

**1.2 High-level approach:**

The goal is to find the maximum area of water that can be contained between two lines.

![Container With Most Water](https://assets.leetcode.com/uploads/2021/07/20/question_11.jpg)

We use two pointers starting at both ends. The area is determined by the width (distance between pointers) and the height (minimum of the two lines). We move the pointer with the smaller height inward, as moving the larger one cannot increase the area.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all pairs of lines, calculating the area for each. This takes $O(n^2)$ time.
- **Optimized Strategy (Two Pointers):** Start with pointers at both ends. Move the pointer with smaller height inward, as this is the only way to potentially find a larger area. This takes $O(n)$ time.
- **Why it's better:** The two-pointer approach reduces time complexity from $O(n^2)$ to $O(n)$ by eliminating unnecessary comparisons. Moving the smaller pointer is the only way to potentially increase the area.

**1.4 Decomposition:**

1. Initialize two pointers: `left = 0` and `right = len(height) - 1`.
2. Initialize `max_area = 0`.
3. While `left < right`:
   - Calculate current area: `width * min(height[left], height[right])`.
   - Update `max_area` if current area is larger.
   - Move the pointer with smaller height inward.
4. Return `max_area`.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $height = [1,8,6,2,5,4,8,3,7]$

We initialize:
- `left = 0`, `right = 8`
- `max_area = 0`

**2.2 Start Processing:**

We begin comparing areas.

**2.3 Trace Walkthrough:**

| Iteration | left | right | height[left] | height[right] | Area | Action |
|-----------|------|-------|--------------|---------------|------|--------|
| 1 | 0 | 8 | 1 | 7 | $8 \times 1 = 8$ | Move left |
| 2 | 1 | 8 | 8 | 7 | $7 \times 7 = 49$ | Move right |
| 3 | 1 | 7 | 8 | 3 | $6 \times 3 = 18$ | Move right |
| 4 | 1 | 6 | 8 | 8 | $5 \times 8 = 40$ | Move either |
| 5 | 2 | 6 | 6 | 8 | $4 \times 6 = 24$ | Move left |
| ... | ... | ... | ... | ... | ... | ... |

**2.4 Key Insight:**

- Initial: left=0 (height=1), right=8 (height=7), area=8
- After moving left: left=1 (height=8), right=8 (height=7), area=49 (larger!)
- The maximum area found is 49

**2.5 Return Result:**

We return 49, which is the maximum area of water that can be contained.

> **Note:** The key insight is that moving the pointer with the smaller height is the only way to potentially find a larger area. Moving the larger pointer would only decrease the width while the height is still limited by the smaller value.
