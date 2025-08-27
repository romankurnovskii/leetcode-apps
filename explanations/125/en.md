## 125. Valid Palindrome [Easy]
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

**Examples**
```tex
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
An empty string is a palindrome.
```

**Constraints:**
```tex
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
```

## Explanation
You're given a string `s`. Your task is to determine if it's a palindrome. A palindrome is a sequence that reads the same forwards and backwards. However, there are two special rules for this problem:
1.  You should ignore all non-alphanumeric characters (like spaces, commas, colons, etc.).
2.  You should treat uppercase and lowercase letters as the same (e.g., 'A' is the same as 'a').

So, "A man, a plan, a canal: Panama" should become "amanaplanacanalpanama" before checking if it's a palindrome.

### Strategy
You are given a string `s`.
The problem asks you to check if `s` is a palindrome after specific filtering and casing rules.
This is a string manipulation and two-pointer problem.

**Constraints:**
* `1 <= s.length <= 2 * 10^5`: The string can be quite long, so an O(n) solution is preferred. O(n log n) might also pass, but O(n^2) would be too slow.
* `s consists only of printable ASCII characters`: This simplifies character handling, no complex encodings.

The most robust and efficient strategy involves processing the string to meet the palindrome rules and then applying a two-pointer approach. You can either pre-process the entire string first, or filter characters on the fly while comparing. The "on-the-fly" method is often slightly more memory-efficient as it doesn't create a new full string immediately, but both are O(N) time and O(N) or O(1) space (depending on how you count auxiliary space for the cleaned string). The "on-the-fly" method often has better constant factors for space.

Let's focus on the "Two Pointers with On-the-Fly Filtering" strategy, as it's generally preferred for interviews due to its space efficiency and direct manipulation of the original string.

**Decomposition:**
1.  Initialize two pointers, `left` at the beginning of the string and `right` at the end.
2.  While `left` is less than `right`:
    a.  Move `left` inwards until it points to an alphanumeric character.
    b.  Move `right` inwards until it points to an alphanumeric character.
    c.  If `left` is still less than `right` (meaning both found valid characters):
        i.  Compare the characters at `left` and `right`, ignoring case.
        ii. If they don't match, return `false` (not a palindrome).
        iii. If they match, move `left` one step right and `right` one step left.
    d.  If `left` becomes `right` or `left` crosses `right`, the loop ends.
3.  If the loop completes, it means all compared alphanumeric characters matched, so return `true` (it's a palindrome).

### Steps
Let's use the example `s = "A man, a plan, a canal: Panama"`

1.  Initialize `left = 0`, `right = len(s) - 1` (which is `29`).
    `s[left]` is 'A', `s[right]` is 'a'.

2.  **Loop starts (`left < right` is `0 < 29` which is True):**

    * **Find alphanumeric `s[left]`:**
        * `s[0]` is 'A'. `s[0].isalnum()` is True. `left` stays `0`.
    * **Find alphanumeric `s[right]`:**
        * `s[29]` is 'a'. `s[29].isalnum()` is True. `right` stays `29`.
    * **Compare:**
        * `s[0].lower()` ('a') vs `s[29].lower()` ('a'). They match.
    * **Move pointers:** `left` becomes `1`, `right` becomes `28`.

3.  **Loop continues (`left < right` is `1 < 28` which is True):**

    * `s[1]` is ' '. `s[1].isalnum()` is False. `left` increments to `2`.
    * `s[2]` is 'm'. `s[2].isalnum()` is True. `left` stays `2`.
    * `s[28]` is 'm'. `s[28].isalnum()` is True. `right` stays `28`.
    * **Compare:**
        * `s[2].lower()` ('m') vs `s[28].lower()` ('m'). They match.
    * **Move pointers:** `left` becomes `3`, `right` becomes `27`.

4.  **Loop continues (`left < right` is `3 < 27` which is True):**

    * `s[3]` is 'a'. `left` stays `3`.
    * `s[27]` is 'a'. `right` stays `27`.
    * **Compare:** `s[3].lower()` ('a') vs `s[27].lower()` ('a'). Match.
    * **Move pointers:** `left` becomes `4`, `right` becomes `26`.

...This process repeats. Non-alphanumeric characters (spaces, commas, colons) will cause one of the inner `while` loops to advance a pointer. For example, if `s[left]` is a space, `left` will increment until it finds an alphanumeric character. The same happens for `right` moving inwards.

Eventually, if `s = "A man, a plan, a canal: Panama"`, all corresponding alphanumeric characters will match. The pointers will cross or meet (`left >= right`). When `left` is no longer less than `right`, the `while left < right` loop terminates.

At this point, since no mismatches were found, the function returns `true`.

Example: `s = "race a car"`
1.  Initialize `left = 0`, `right = 9`.
    `s[0]` is 'r', `s[9]` is 'r'.
2.  Loop:
    * `left=0` ('r'), `right=9` ('r'). Match. `left=1`, `right=8`.
    * `left=1` ('a'), `right=8` ('a'). Match. `left=2`, `right=7`.
    * `left=2` ('c'), `right=7` ('c'). Match. `left=3`, `right=6`.
    * `left=3` ('e'), `right=6` ('a'). **Mismatch!** ('e' != 'a'). Return `false`.

This approach is efficient because it processes each character at most a constant number of times (once by `left`, once by `right`). So, time complexity is O(n). Space complexity is O(1) because you're only using a couple of pointers and not creating new large data structures.
