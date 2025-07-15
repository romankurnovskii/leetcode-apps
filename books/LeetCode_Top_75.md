# LeetCode Top 75

Problem list from official https://leetcode.com/studyplan/leetcode-75/

## 1768. Merge Strings Alternately [Easy]
https://leetcode.com/problems/merge-strings-alternately

### Explanation

## Explanation

Iterate through both strings in parallel, appending one character from each to the result. If one string is longer, append the remaining characters at the end.

## Hint

Use a loop up to the length of the longer string, and check bounds for each string.

## Points

- Handles strings of different lengths.
- Time complexity: O(n), where n is the total length of both strings.
- The result alternates characters from each string as much as possible.

### Solution (Python)

```python
def mergeAlternately(word1, word2):
    res = []
    n1, n2 = len(word1), len(word2)
    for i in range(max(n1, n2)):
        if i < n1:
            res.append(word1[i])
        if i < n2:
            res.append(word2[i])
    return "".join(res)
```

## 1071. Greatest Common Divisor of Strings [Easy]
https://leetcode.com/problems/greatest-common-divisor-of-strings

### Explanation

## Explanation

To find the greatest common divisor (GCD) of two strings, we check if there is a string that can be concatenated multiple times to form both input strings. If str1 + str2 == str2 + str1, then such a string exists. The length of the GCD string is the greatest common divisor of the lengths of str1 and str2. We return the prefix of that length from either string.

## Hint

Check if concatenating the strings in both orders gives the same result. Use the GCD of the lengths to find the answer.

## Points

- If str1 + str2 != str2 + str1, there is no common divisor string.
- Use math.gcd to compute the length of the answer.
- Time complexity: O(n + m), where n and m are the lengths of the input strings.

### Solution (Python)

```python
def gcdOfStrings(str1, str2):
    # If concatenating in both orders gives the same result, there is a common divisor
    if str1 + str2 != str2 + str1:
        return ""
    # The GCD of the lengths gives the length of the common divisor
    from math import gcd

    length = gcd(len(str1), len(str2))
    return str1[:length]
```

## 1431. Kids With the Greatest Number of Candies [Easy]
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

### Explanation

## Explanation

First, find the maximum number of candies any kid currently has. Then, for each kid, check if giving them all the `extraCandies` would make their total at least as large as the current maximum. Return a list of booleans for each kid.

## Hint

Find the current maximum, then check each kid with `extraCandies` added.

## Points

- Time complexity: O(n), where n is the number of kids.
- The result is a list of booleans, one for each kid.
- Handles cases where multiple kids already have the maximum.

### Solution (Python)

```python
def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    return [c + extraCandies >= max_candies for c in candies]
```
