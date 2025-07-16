## 739. Daily Temperatures [Medium]

https://leetcode.com/problems/daily-temperatures

## Description
Given an array of integers temperatures representing the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the i-th day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

## Examples

**Example 1**
Input:
temperatures = [73,74,75,71,69,72,76,73]
Output:
[1,1,4,2,1,1,0,0]

**Example 2**
Input:
temperatures = [30,40,50,60]
Output:
[1,1,1,0]

**Example 3**
Input:
temperatures = [30,60,90]
Output:
[1,1,0]

## Constraints
```
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
```

## Explanation

**Intuition**

We need to find, for each day, how many days must pass until a warmer temperature occurs. If no such day exists, the answer is 0 for that day. This is a classic "next greater element" problem, efficiently solved with a monotonic stack.

**Approach**

1. Initialize an empty stack to keep track of indices of unresolved days (days for which we haven't found a warmer temperature yet).
2. Iterate through the temperatures array:
   - For each day, while the stack is not empty and the current temperature is higher than the temperature at the index on top of the stack:
     - Pop the index from the stack and set answer[pop_index] = current_index - pop_index.
   - Push the current day's index onto the stack.
3. After processing all days, any indices left in the stack do not have a warmer day in the future, so their answer remains 0.

