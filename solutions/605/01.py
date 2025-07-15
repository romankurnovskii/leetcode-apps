## Description

You have a flowerbed (list of plots) containing 0s and 1s, where 0 means empty and 1 means not empty. Flowers cannot be planted in adjacent plots. Given the flowerbed and a number n, return if n new flowers can be planted without violating the rule.

Example:
```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
```

Constraints:
```
- 1 <= flowerbed.length <= 2 * 10^4
- flowerbed[i] is 0 or 1.
- There are no two adjacent flowers in the flowerbed.
```

## Hint

> Check each empty plot and see if both neighbors are empty (or out of bounds).

## Explanation

Let's imagine the flowerbed as a row of garden plots. We want to plant new flowers, but we can't put them right next to each other. So, for each empty spot, we check the spots to the left and right. If both are empty (or if we're at the edge), we can plant a flower there.

We do this because it's the only way to guarantee we never break the "no neighbors" rule. By checking each spot, we make sure we don't miss any possible planting locations.

We keep a count of how many flowers we've planted. If we reach the required number, we can stop early and return `True`. This helps us avoid unnecessary work and makes our solution efficient.

## Solution
```python
def canPlaceFlowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            empty_left = (i == 0) or (flowerbed[i-1] == 0)
            empty_right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
            if empty_left and empty_right:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
    return count >= n
``` 