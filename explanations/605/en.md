## Hint

> Check each empty plot and see if both neighbors are empty (or out of bounds).

## Explanation

Let's imagine the flowerbed as a row of garden plots. We want to plant new flowers, but we can't put them right next to each other. So, for each empty spot, we check the spots to the left and right. If both are empty (or if we're at the edge), we can plant a flower there.

We do this because it's the only way to guarantee we never break the "no neighbors" rule. By checking each spot, we make sure we don't miss any possible planting locations.

We keep a count of how many flowers we've planted. If we reach the required number, we can stop early and return `True`. This helps us avoid unnecessary work and makes our solution efficient.
