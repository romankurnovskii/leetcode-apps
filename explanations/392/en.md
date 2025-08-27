## 392. Is Subsequence [Easy]

https://leetcode.com/problems/is-subsequence

## Description
Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

**Examples**
```tex
Input: s = "abc", t = "ahbgdc"
Output: true

Input: s = "axc", t = "ahbgdc"
Output: false
```

**Constraints**
```tex
- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- s and t consist only of lowercase English letters.
```

## Explanation

### Strategy

The problem asks you to determine if one string, `s`, is a **subsequence** of another string, `t`. A subsequence means that the characters of `s` appear in `t` in the *same relative order*, but not necessarily contiguously. For example, "ace" is a subsequence of "abcde" (you skip 'b' and 'd'), but "aec" is not because 'e' comes after 'c' in "aec" but before 'c' in "abcde". you are given two strings, `s` and `t`, consisting of lowercase English letters, and their lengths are constrained.

This is a string matching problem that can be efficiently solved using a **two-pointer approach**. The core idea is to use one pointer to traverse string `s` and another pointer to traverse string `t`. As you iterate through `t`, you look for characters that match the current character you are seeking in `s`. If you find a match, it means you\'ve successfully matched a character from `s`, so you advance the pointer for `s` to look for the next character in `s`. Regardless of a match, you always advance the pointer for `t` because you are scanning `t` from left to right.

If, by the time you finish traversing `t`, the pointer for `s` has successfully traversed all of `s` (meaning it has reached the end of `s`), then `s` is a subsequence of `t`. Otherwise, it is not.

> Use two pointers to check if you can match all characters of s in t in order.

### Steps

Let\'s walk through the example: `s = "abc"`, `t = "ahbgdc"`

1.  Initialize two pointers:
    * `ptr_s = 0` (pointing to the first character of `s`, 'a')
    * `ptr_t = 0` (pointing to the first character of `t`, 'a')

2.  Start a loop that continues as long as both pointers are within the bounds of their respective strings (`ptr_s < len(s)` and `ptr_t < len(t)`):

    * **Iteration 1:**
        * `s[ptr_s]` is `'a'`, `t[ptr_t]` is `'a'`. They match!
        * Increment `ptr_s`. `ptr_s` becomes `1`.
        * Increment `ptr_t`. `ptr_t` becomes `1`.
        * `s` is now `'[a]bc'`, `t` is now `'a[h]bgdc'`

    * **Iteration 2:**
        * `s[ptr_s]` is `'b'`, `t[ptr_t]` is `'h'`. They do not match.
        * Only increment `ptr_t`. `ptr_t` becomes `2`.
        * `s` is now `'a[b]c'`, `t` is now `'ah[b]gdc'`

    * **Iteration 3:**
        * `s[ptr_s]` is `'b'`, `t[ptr_t]` is `'b'`. They match!
        * Increment `ptr_s`. `ptr_s` becomes `2`.
        * Increment `ptr_t`. `ptr_t` becomes `3`.
        * `s` is now `'ab[c]'`, `t` is now `'ahb[g]dc'`

    * **Iteration 4:**
        * `s[ptr_s]` is `'c'`, `t[ptr_t]` is `'g'`. They do not match.
        * Only increment `ptr_t`. `ptr_t` becomes `4`.
        * `s` is now `'ab[c]'`, `t` is now `'ahbg[d]c'`

    * **Iteration 5:**
        * `s[ptr_s]` is `'c'`, `t[ptr_t]` is `'d'`. They do not match.
        * Only increment `ptr_t`. `ptr_t` becomes `5`.
        * `s` is now `'ab[c]'`, `t` is now `'ahbgd[c]'`

    * **Iteration 6:**
        * `s[ptr_s]` is `'c'`, `t[ptr_t]` is `'c'`. They match!
        * Increment `ptr_s`. `ptr_s` becomes `3`.
        * Increment `ptr_t`. `ptr_t` becomes `6`.
        * `s` is now `'abc[]'`, `t` is now `'ahbgdc[]'`

3.  The loop terminates because `ptr_t` (`6`) is now equal to `len(t)` (`6`).

4.  After the loop, check if `ptr_s` has reached the end of `s`. In this case, `ptr_s` is `3`, and `len(s)` is `3`. Since `ptr_s == len(s)`, `s` is a subsequence of `t`.

    The result (`res`) is `True`.

Let\'s consider another example: `s = "axc"`, `t = "ahbgdc"`

1.  Initialize `ptr_s = 0`, `ptr_t = 0`.
2.  Loop:

    * **Iteration 1:**
        * `s[0]` is `'a'`, `t[0]` is `'a'`. Match!
        * `ptr_s = 1`, `ptr_t = 1`.

    * **Iteration 2:**
        * `s[1]` is `'x'`, `t[1]` is `'h'`. No match.
        * `ptr_t = 2`.

    * **Iteration 3:**
        * `s[1]` is `'x'`, `t[2]` is `'b'`. No match.
        * `ptr_t = 3`.

    * **Iteration 4:**
        * `s[1]` is `'x'`, `t[3]` is `'g'`. No match.
        * `ptr_t = 4`.

    * **Iteration 5:**
        * `s[1]` is `'x'`, `t[4]` is `'d'`. No match.
        * `ptr_t = 5`.

    * **Iteration 6:**
        * `s[1]` is `'x'`, `t[5]` is `'c'`. No match.
        * `ptr_t = 6`.

3.  Loop terminates because `ptr_t` (`6`) is equal to `len(t)` (`6`).
4.  Check `ptr_s == len(s)`. `ptr_s` is `1`, `len(s)` is `3`. Since `1 != 3`, `s` is NOT a subsequence of `t`.

    The result (`res`) is `False`.

> **Note:** This two-pointer approach is optimal for this problem. It processes each character of `t` at most once and each character of `s` at most once. This makes it very efficient, especially when `t` is much longer than `s`.

**Time Complexity:** The solution involves iterating through string `t` at most once. In the worst case, both pointers will traverse their entire strings. Therefore, the time complexity is $O(\text{len}(t))$. Since $len(s) \le len(t)$, this can also be expressed as $O(M+N)$ where $M = len(s)$ and $N = len(t)$, but since $N$ dominates, it simplifies to $O(N)$.

**Space Complexity:** you are only using a few variables for pointers, which take constant space. Thus, the space complexity is $O(1)$.
