## Maximum Number of Vowels in a Substring of Given Length [Medium]
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

## Description

Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example:
```
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
```

Constraints:
```
1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= s.length
```

> **Hint:**  Use a sliding window to count vowels in each substring of length k.

### Explanation

We want to find the most vowels in any substring of length k. To do this efficiently, we use a sliding window: we count the vowels in the first window, then as we move the window, we subtract the letter that leaves and add the new letter that enters.

We do this because it lets us update our count in constant time, instead of recounting every window from scratch. This makes our solution much faster, especially for long strings.

By always keeping track of the current number of vowels, we can quickly find the maximum as we slide the window across the string. 