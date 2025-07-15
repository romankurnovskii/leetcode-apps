## Explanation

First, find the maximum number of candies any kid currently has. Then, for each kid, check if giving them all the `extraCandies` would make their total at least as large as the current maximum. Return a list of booleans for each kid.

## Hint

Find the current maximum, then check each kid with `extraCandies` added.

## Points

- Time complexity: `O(n)`, where `n` is the number of kids.
- The result is a list of booleans, one for each kid.
- Handles cases where multiple kids already have the maximum.
