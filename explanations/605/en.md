## 605. Can Place Flowers [Easy]

https://leetcode.com/problems/can-place-flowers

## Description
You have a long flowerbed in which some plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

**Examples**
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

**Constraints**
- 1 <= flowerbed.length <= 2 * 10^4
- flowerbed[i] is 0 or 1.
- There are no two adjacent flowers in the flowerbed.
- 0 <= n <= flowerbed.length

## Hint
Check each empty plot and see if both neighbors are empty (or out of bounds).

## Explanation
Let's imagine the flowerbed as a row of garden plots. We want to plant new flowers, but we can't put them right next to each other. So, for each empty spot, we check the spots to the left and right. If both are empty (or if we're at the edge), we can plant a flower there.

We do this because it's the only way to guarantee we never break the "no neighbors" rule. By checking each spot, we make sure we don't miss any possible planting locations.

We keep a count of how many flowers we've planted. If we reach the required number, we can stop early and return True. This helps us avoid unnecessary work and makes our solution efficient.

