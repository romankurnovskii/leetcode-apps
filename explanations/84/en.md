## Explanation

### Strategy (The "Why")

Given an array of integers `heights` representing the heights of bars in a histogram, we need to find the area of the largest rectangle in the histogram.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be up to $10^5$.
- **Value Range:** Heights are between $0$ and $10^4$.
- **Time Complexity:** $O(n)$ - Each bar is pushed and popped from the stack at most once.
- **Space Complexity:** $O(n)$ - The stack can contain at most $n$ elements.
- **Edge Case:** If all heights are the same, the maximum area is $height \times n$. If heights are in ascending order, process all at the end.

**1.2 High-level approach:**

The goal is to find the largest rectangle that can be formed in the histogram.

We use a stack to track bars in increasing order of height. When we encounter a bar shorter than the stack top, we calculate the area of rectangles ending at that bar and update the maximum.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each bar, find the largest rectangle with that bar as height. This takes $O(n^2)$ time.
- **Optimized Strategy (Stack):** Use a stack to efficiently find the left boundary for each bar. This takes $O(n)$ time.
- **Why it's better:** The stack approach reduces time complexity from $O(n^2)$ to $O(n)$ by maintaining bars in increasing order and calculating areas efficiently.

**1.4 Decomposition:**

1. Use a stack to store indices of bars in increasing order of height.
2. For each bar:
   - While stack is not empty and current bar is shorter than stack top:
     - Pop the stack top and calculate area with that bar as height.
     - Update maximum area.
   - Push current bar index.
3. After processing all bars, process remaining bars in stack.
4. Return maximum area.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $heights = [2,1,5,6,2,3]$

We initialize:
- `stack = []`
- `max_area = 0`

**2.2 Start Processing:**

We iterate through each bar.

**2.3 Trace Walkthrough:**

| i | heights[i] | stack Before | Action | Area Calculated | max_area | stack After |
|---|------------|--------------|--------|-----------------|----------|-------------|
| 0 | 2 | [] | Push | - | 0 | [0] |
| 1 | 1 | [0] | Pop 0, calc | $2 \times 1 = 2$ | 2 | [1] |
| 2 | 5 | [1] | Push | - | 2 | [1,2] |
| 3 | 6 | [1,2] | Push | - | 2 | [1,2,3] |
| 4 | 2 | [1,2,3] | Pop 3, calc | $6 \times 1 = 6$ | 6 | [1,2] |
| 4 | 2 | [1,2] | Pop 2, calc | $5 \times 2 = 10$ | 10 | [1] |
| 4 | 2 | [1] | Push | - | 10 | [1,4] |
| 5 | 3 | [1,4] | Push | - | 10 | [1,4,5] |

**After loop, process remaining:**
- Pop 5: area = $3 \times 1 = 3$, max_area = 10
- Pop 4: area = $2 \times 3 = 6$, max_area = 10
- Pop 1: area = $1 \times 6 = 6$, max_area = 10

**2.4 Final Result:**

The maximum area is 10 (rectangle with height 5 and width 2, from index 2 to 3).

**2.5 Return Result:**

We return 10, which is the area of the largest rectangle.

> **Note:** The key insight is that when we encounter a bar shorter than the stack top, all bars in the stack taller than the current bar can form rectangles ending at the current position. We calculate their areas and update the maximum.

