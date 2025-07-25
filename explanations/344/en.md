## 344. Reverse String [Easy]
https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

**Examples**
<code>
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
</code>

**Constraints:**
<code>
1 <= s.length <= 10^5
s[i] is a printable ASCII character.
</code>

## Explanation
You are given a string, but it's presented as a list of characters (e.g., `["h","e","l","l","o"]`). Your goal is to reverse the order of these characters within the *same* list. You cannot create a brand new list to store the reversed string; you must modify the original list directly. Also, you should do this using only a constant amount of extra memory (O(1) space).

### Strategy
You are given a list of characters `s`.
The problem asks you to reverse `s` in-place with O(1) extra memory.
This is an array manipulation problem, specifically an in-place reversal.

**Constraints:**
* `1 <= s.length <= 10^5`: The string can be quite long, so an O(n) solution is necessary.
* `s[i] is a printable ASCII character`: Simple character types.

The most efficient and constrained-compliant way to reverse an array (or list of characters) in-place is using the two-pointer technique.

**Decomposition:**
1.  Initialize two pointers: `left` at the very beginning of the list (index 0) and `right` at the very end of the list (index `len(s) - 1`).
2.  While `left` is less than `right`:
    a.  Swap the character at `s[left]` with the character at `s[right]`.
    b.  Move `left` one step to the right (`left += 1`).
    c.  Move `right` one step to the left (`right -= 1`).
3.  When `left` becomes equal to or greater than `right`, the pointers have met or crossed. This means all necessary swaps have been performed, and the string is reversed.

### Steps
Let's use the example `s = ["h","e","l","l","o"]`

1.  Initialize `left = 0`, `right = 4` (since `len(s)` is 5).
    `s` is `["h","e","l","l","o"]`

2.  **Loop starts (`left < right` is `0 < 4` which is True):**

    * **Swap `s[0]` and `s[4]`:**
        * `s[0]` ('h') becomes `s[4]` ('o').
        * `s[4]` ('o') becomes `s[0]` ('h').
        * `s` is now `["o","e","l","l","h"]`
    * **Move pointers:** `left` becomes `1`, `right` becomes `3`.

3.  **Loop continues (`left < right` is `1 < 3` which is True):**

    * **Swap `s[1]` and `s[3]`:**
        * `s[1]` ('e') becomes `s[3]` ('l').
        * `s[3]` ('l') becomes `s[1]` ('e').
        * `s` is now `["o","l","l","e","h"]`
    * **Move pointers:** `left` becomes `2`, `right` becomes `2`.

4.  **Loop ends:** Now, `left` (2) is *not* less than `right` (2) (`left < right` is `2 < 2` which is False). The loop terminates.

The array `s` is now `["o","l","l","e","h"]`, which is the reversed string.

This approach performs `n/2` swaps (approximately) for an array of length `n`. Each swap takes constant time. Thus, the time complexity is O(n). Since you only use two integer variables (`left` and `right`), the space complexity is O(1).
