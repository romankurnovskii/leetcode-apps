## 11. Container With Most Water [Medium]

https://leetcode.com/problems/container-with-most-water/

## Description
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the i-th line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Examples:

```raw
Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Constraints:

- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
```

> **Hint:**  Use two pointers, one at each end, and move the pointer with the shorter line inward.

### Explanation

## Explanation
Imagine the array as a row of sticks of different heights. You want to pick two sticks that, together with the x-axis, can hold the most water. The area is determined by the shorter stick and the distance between them. Start with the two ends and move the pointer pointing to the shorter stick inward, always looking for a bigger area.

This approach is efficient because it checks all possible pairs in linear time, always keeping the best answer found so far.

