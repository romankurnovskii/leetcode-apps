## Explanation

### Strategy (The "Why")

Given an array of integers `heights` representing the heights of bars in a histogram, we need to find the largest rectangle area that can be formed.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length can be between $1$ and $10^5$.
- **Value Range:** Bar heights are between $0$ and $10^4$.
- **Time Complexity:** $O(n)$ - Each bar is pushed and popped from the stack at most once.
- **Space Complexity:** $O(n)$ - The stack can contain at most $n$ elements.
- **Edge Case:** If all bars have the same height, the maximum area is $height \times n$. If the array is in ascending order, the maximum area involves the last bar.

**1.2 High-level approach:**

The goal is to find the largest rectangle that can be formed in a histogram.

We use a stack to track bars in increasing order of height. When we encounter a bar shorter than the stack top, we calculate the area that can be formed using the stack top as the minimum height, then pop from the stack.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each bar, find the largest rectangle with that bar as the minimum height. This takes $O(n^2)$ time.
- **Optimized Strategy (Stack):** Use a stack to efficiently find the left and right boundaries for each bar. This takes $O(n)$ time.
- **Why it's better:** The stack approach reduces time complexity from $O(n^2)$ to $O(n)$ by processing each bar at most twice (once when pushing, once when popping).

**1.4 Decomposition:**

1. Use a stack to store indices of bars in increasing order of height.
2. For each bar:
   - While the stack is not empty and current bar is shorter than stack top:
     - Pop from stack and calculate area using popped bar as minimum height.
     - Update maximum area.
   - Push current bar index to stack.
3. After processing all bars, process remaining bars in the stack.
4. Return maximum area.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $heights = [2,1,5,6,2,3]$

We initialize:
- `stack = []`
- `max_area = 0`

**2.2 Start Processing:**

We begin processing bars.

**2.3 Trace Walkthrough:**

| i | heights[i] | stack Before | Action | Area Calculated | max_area |
|---|------------|--------------|--------|-----------------|----------|
| 0 | 2 | [] | Push 0 | - | 0 |
| 1 | 1 | [0] | Pop 0, calc area | $2 \times 1 = 2$ | 2 |
| 1 | 1 | [] | Push 1 | - | 2 |
| 2 | 5 | [1] | Push 2 | - | 2 |
| 3 | 6 | [1,2] | Push 3 | - | 2 |
| 4 | 2 | [1,2,3] | Pop 3, calc | $6 \times 1 = 6$ | 6 |
| 4 | 2 | [1,2] | Pop 2, calc | $5 \times 2 = 10$ | 10 |
| 4 | 2 | [1] | Push 4 | - | 10 |
| ... | ... | ... | ... | ... | ... |

**2.4 Maximum Area:**

The maximum area found is 10 (using bars at indices 2 and 3 with height 5 as minimum).

**2.5 Return Result:**

We return 10, which is the largest rectangle area.

> **Note:** The key insight is that when we encounter a bar shorter than the stack top, all bars in the stack that are taller can form rectangles ending at the current position. The width of such a rectangle is determined by the position of the previous shorter bar (stack top after popping).

