## 1431. Kids With the Greatest Number of Candies [Easy]

https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

## Description
There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `i`th kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return a boolean array `result` of length `n`, where `result[i]` is `true` if, after giving the `i`th kid all the `extraCandies`, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

**Examples**

```tex
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
```

**Constraints**

```tex
- n == candies.length
- 2 <= n <= 100
- 1 <= candies[i] <= 100
- 1 <= extraCandies <= 50
```

## Hint
For each kid, check if their candies plus `extraCandies` is at least as much as the current maximum.

## Explanation
First, you want to know the highest number of candies any kid currently has. This is important because you need a reference point to see if giving extra candies to a kid will make them "the greatest."

For each kid, you add the `extraCandies` to their current amount. You do this because you want to see if, after the bonus, they can reach or beat the current maximum. If they do, you mark them as `True` in our answer list; otherwise, False.

You only need to find the maximum once, and then just compare each kid's total to it. Don't need to recalculate the maximum for every kid. 