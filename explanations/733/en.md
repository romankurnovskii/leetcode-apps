## Explanation

### Strategy (The "Why")

Given an image represented as a 2D integer array, a starting pixel position $(sr, sc)$, and a new color, we need to perform a flood fill: change the color of the starting pixel and all connected pixels of the same color to the new color.

**1.1 Constraints & Complexity:**

- **Input Size:** The image dimensions $m \times n$ can be up to $50 \times 50$.
- **Value Range:** Image values and colors are between $0$ and $65535$.
- **Time Complexity:** $O(m \times n)$ - In the worst case, we visit every pixel in the image once.
- **Space Complexity:** $O(m \times n)$ - The recursion stack can be as deep as the number of pixels in the connected region. In the worst case (all pixels connected), this is $O(m \times n)$.
- **Edge Case:** If the starting pixel's color is already the new color, we return the image unchanged (to avoid infinite recursion).

**1.2 High-level approach:**

The goal is to fill a connected region of the same color with a new color.

![Flood Fill](https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg)

We use depth-first search (DFS) to explore all pixels connected to the starting pixel that have the same color. We change each visited pixel to the new color.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must traverse connected pixels. However, we could use BFS instead of DFS.
- **Optimized Strategy (DFS):** Use recursive DFS to explore the 4-directionally connected pixels. We check bounds and ensure we only fill pixels with the original color.
- **Why it's better:** DFS is simple and intuitive for this problem. We could also use BFS (iterative with a queue), which would have the same time complexity but might use less stack space for large regions.

**1.4 Decomposition:**

1. Store the original color of the starting pixel.
2. If the original color equals the new color, return the image unchanged.
3. Define a recursive DFS function that fills a pixel and recursively fills its 4 neighbors.
4. In the DFS function, check bounds and ensure the pixel has the original color before filling.
5. Start the DFS from the starting pixel position.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $image = [[1,1,1],[1,1,0],[1,0,1]]$, $sr = 1$, $sc = 1$, $color = 2$

The image:
```
1 1 1
1 1 0
1 0 1
```

We initialize:
- `original_color = image[1][1] = 1`
- Since $1 \neq 2$, we proceed with flood fill

**2.2 Start Flood Fill:**

We begin DFS from position $(1, 1)$.

**2.3 Trace Walkthrough:**

| Step | Position | Color | Action | Neighbors to Check |
|------|----------|-------|--------|-------------------|
| 1 | $(1,1)$ | 1 | Fill with 2 | $(0,1), (2,1), (1,0), (1,2)$ |
| 2 | $(0,1)$ | 1 | Fill with 2 | $(0,0), (0,2), (-1,1)$ (out of bounds) |
| 3 | $(0,0)$ | 1 | Fill with 2 | $(0,1), (-1,0)$ (out), $(1,0)$ |
| 4 | $(1,0)$ | 1 | Fill with 2 | $(0,0), (2,0), (1,-1)$ (out), $(1,1)$ (already filled) |
| 5 | $(2,0)$ | 1 | Fill with 2 | $(1,0), (3,0)$ (out), $(2,-1)$ (out), $(2,1)$ |
| 6 | $(2,1)$ | 0 | Skip (different color) | - |
| 7 | $(0,2)$ | 1 | Fill with 2 | $(0,1), (-1,2)$ (out), $(0,3)$ (out), $(1,2)$ |
| 8 | $(1,2)$ | 0 | Skip (different color) | - |

**2.4 Final Image:**

After flood fill:
```
2 2 2
2 2 0
2 0 1
```

**2.5 Return Result:**

We return the modified image with the connected region of color 1 filled with color 2.

> **Note:** The key is to check that we only fill pixels with the original color. Once we change a pixel's color, it won't match the original color anymore, which naturally prevents revisiting it and creates a base case for the recursion.

