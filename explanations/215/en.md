## Explanation

### Strategy (The "Why")

Given an integer array `nums` and an integer `k`, we need to find the $k$-th largest element in the array. Note that it is the $k$-th largest element in the sorted order, not the $k$-th distinct element.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be between $1$ and $10^5$.
- **Value Range:** Array elements are between $-10^4$ and $10^4$.
- **Time Complexity:** $O(n \log k)$ - We maintain a min heap of size $k$, and each insertion takes $O(\log k)$ time. We do this for $n$ elements.
- **Space Complexity:** $O(k)$ - We maintain a min heap of size $k$.
- **Edge Case:** If $k = 1$, we return the maximum element. If $k = n$, we return the minimum element.

**1.2 High-level approach:**

The goal is to find the $k$-th largest element without sorting the entire array.

![Kth Largest Element](https://assets.leetcode.com/uploads/2021/07/15/largest-kth.jpg)

We use a min heap of size $k$. The heap stores the $k$ largest elements seen so far. The top of the heap (minimum in the heap) is the $k$-th largest element overall.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Sort the entire array and return the element at index $n-k$. This takes $O(n \log n)$ time.
- **Optimized Strategy (Min Heap):** Maintain a min heap of size $k$ containing the $k$ largest elements. This takes $O(n \log k)$ time, which is better when $k << n$.
- **Why it's better:** When $k$ is much smaller than $n$, $O(n \log k)$ is significantly better than $O(n \log n)$. For example, if $k=10$ and $n=10^5$, we only need to maintain a heap of size 10 instead of sorting $10^5$ elements.

**1.4 Decomposition:**

1. Initialize an empty min heap.
2. Iterate through each number in the array.
3. If the heap has fewer than $k$ elements, add the number.
4. If the heap has $k$ elements and the current number is larger than the minimum (top) of the heap, replace the top with the current number.
5. After processing all numbers, return the top of the heap (which is the $k$-th largest).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [3,2,1,5,6,4]$, $k = 2$

We initialize:
- `heap = []` (min heap)

**2.2 Start Processing:**

We iterate through each number.

**2.3 Trace Walkthrough:**

| Number | Heap Size | Heap Before | Action | Heap After |
|--------|-----------|-------------|--------|------------|
| 3 | 0 | [] | Push 3 | [3] |
| 2 | 1 | [3] | Push 2 | [2, 3] |
| 1 | 2 | [2, 3] | Skip (1 < 2) | [2, 3] |
| 5 | 2 | [2, 3] | Replace 2 with 5 | [3, 5] |
| 6 | 2 | [3, 5] | Replace 3 with 6 | [5, 6] |
| 4 | 2 | [5, 6] | Skip (4 < 5) | [5, 6] |

**2.4 Final Result:**

After processing, the heap contains $[5, 6]$. The top (minimum) is 5, which is the 2nd largest element.

**2.5 Return Result:**

We return 5, which is the 2nd largest element in the array.

> **Note:** The key insight is that a min heap of size $k$ naturally maintains the $k$ largest elements. The minimum of these $k$ largest elements is the $k$-th largest element overall.

