## 1957. Delete Characters to Make Fancy String [Easy]

https://leetcode.com/problems/delete-characters-to-make-fancy-string

[Editorial](https://leetcode.com/problems/delete-characters-to-make-fancy-string/editorial/)

## Description
A **fancy string** is a string where no **three** **consecutive** characters are equal.

Given a string `s`, delete the **minimum** possible number of characters from `s` to make it **fancy**.

Return the final string after the deletion. It can be shown that the answer will always be **unique**.

**Examples**

```tex
Input: s = "leeetcode"
Output: "leetcode"
Explanation: Remove an 'e' from the first group of 'e's to create "leetcode". No three consecutive characters are equal, so return "leetcode".

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation: Remove an 'a' from the first group of 'a's to create "aabaaaa". Remove two 'a's from the second group of 'a's to create "aabaa". No three consecutive characters are equal, so return "aabaa".

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
```

**Constraints**

```tex
1 <= s.length <= 10^5
s consists only of lowercase English letters.
```

## Explanation

### Strategy
- **Type:** String, Greedy, Two Pointers
- **Given:** A string `s` of lowercase English letters
- **Asked:** Delete the minimum number of characters so that no three consecutive characters are equal

#### What does "fancy string" mean?
- No three consecutive characters are the same. Two in a row is fine, but three or more is not allowed.


#### High-Level Plan
1. As you go through the string, keep a counter (let's call it `count`) that tracks how many times the current character has appeared in a row so far. Start `count` at 1 for the first character.
2. For each next character:
    - If it is the same as the previous character, increase `count` by 1.
    - If it is different, reset `count` to 1 (since it's a new character).
3. Only add the character to your result if `count` is less than or equal to 2. If `count` becomes 3 or more, skip adding it (this is how you "delete").
4. Repeat this for every character in the string.

> **Alternative:**
> Instead of a counter, you can also check the last two characters of your result string. If both are the same as the current character, skip adding it. Otherwise, add it.

### Steps

Let's walk through an example: s = "aaabaaaa"

1. Start with the first character: 'a' (count = 1)
2. Next 'a': count = 2 (keep)
3. Next 'a': count = 3 (skip)
4. Next 'b': new character, count = 1 (keep)
5. Next 'a': new character, count = 1 (keep)
6. Next 'a': count = 2 (keep)
7. Next 'a': count = 3 (skip)
8. Next 'a': count = 4 (skip)
9. Result: "aabaa"

> - This is a classic greedy pattern: always keep at most two consecutive identical characters.
> - You can use a counter or check the last two characters of the result to decide whether to add the next character.

