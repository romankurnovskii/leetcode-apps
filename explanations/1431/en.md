## Hint

> For each kid, check if their candies plus extraCandies is at least as much as the current maximum.

## Explanation

  
First, we want to know the highest number of candies any kid currently has. This is important because we need a reference point to see if giving extra candies to a kid will make them "the greatest."

For each kid, we add the extraCandies to their current amount. We do this because we want to see if, after the bonus, they can reach or beat the current maximum. If they do, we mark them as `True` in our answer list; otherwise, `False`.

This approach is efficient because we only need to find the maximum once, and then just compare each kid's total to it. This saves us from recalculating the maximum for every kid, making our solution faster and cleaner. 