## 1456. Maximum Number of Vowels in a Substring of Given Length [Medium]

https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

## Description
Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

**Examples**
```sh
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

**Constraints**
```text
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- 1 <= k <= s.length
```

## Explanation

### Strategy
The problem asks You to find the maximum number of vowel letters within any contiguous substring of a fixed length `k` in a given string `s`. Vowels are defined as \'a\', \'e\', \'i\', \'o\', \'u\'.

This is a classic **sliding window** problem, specifically for a *fixed-size window*. A naive approach would be to iterate through all possible substrings of length `k`, count the vowels in each, and then find the maximum. For a string of length `N`, there are `N - k + 1` such substrings. Counting vowels in each substring takes $O(k)$ time, leading to an overall $O(N * k)$ time complexity. This is inefficient for large strings.

The sliding window technique provides an optimal solution. You initialize a window of size `k` at the beginning of the string and calculate the count of vowels within this initial window. This count becomes our starting `current_vowel_count` and `max_vowel_count`.

Then, you "slide" this window one position to the right. When the window slides:
1.  The character at the `leftmost` position of the *previous* window effectively "leaves" the window. If this character was a vowel, you decrement our `current_vowel_count`.
2.  The character at the `new rightmost` position effectively "enters" the window. If this new character is a vowel, you increment our `current_vowel_count`.

By doing this, you update the vowel count for the new window in $O(1)$ time, instead of recounting from scratch. After each slide, you compare `current_vowel_count` with `max_vowel_count` and update `max_vowel_count` if `current_vowel_count` is greater. This process continues until the window has slid across the entire string.

> Use a sliding window to count vowels in each substring of length `k`.

### Steps

> The idea is to use a window of size `k` and slide it across the string `s`. Instead of counting the number of vowels in the entire window every time, we adjust the count by adding the new character and removing the leftmost character as the window slides.

Let\'s walk through an example: `s = "abciiidef"`, `k = 3`

1.  Define a set of vowels for quick lookup: `vowels = {\'a\', \'e\', \'i\', \'o\', \'u\'}`.

2.  Initialize:
    * `current_vowel_count = 0`
    * `max_vowel_count = 0`

3.  **Calculate initial window (first `k` characters):**
    * Substring: `"abc"`
    * `s[0] = 'a'` (vowel): `current_vowel_count = 1`
    * `s[1] = 'b'` (consonant)
    * `s[2] = 'c'` (consonant)
    * After the first window, `current_vowel_count = 1`.
    * Set `max_vowel_count = 1`.

4.  **Slide the window:** You will iterate from index `k` (which is 3) up to `len(s) - 1`.

    * **Iteration 1 (i = 3):**
        * Character leaving window: `s[i - k]` which is `s[0] = 'a'`. Is `'a'` in `vowels`? Yes. `current_vowel_count = 1 - 1 = 0`.
        * Character entering window: `s[i]` which is `s[3] = 'i'`. Is `'i'` in `vowels`? Yes. `current_vowel_count = 0 + 1 = 1`.
        * New window: `"bci"`. Current count: `1`. 
        * `max_vowel_count = max(1, 1) = 1`.

    * **Iteration 2 (i = 4):**
        * Character leaving window: `s[i - k]` which is `s[1] = 'b'`. Is `'b'` in `vowels`? No.
        * Character entering window: `s[i]` which is `s[4] = 'i'`. Is `'i'` in `vowels`? Yes. `current_vowel_count = 1 + 1 = 2`.
        * New window: `"cii"`. Current count: `2`.
        * `max_vowel_count = max(1, 2) = 2`.

    * **Iteration 3 (i = 5):**
        * Character leaving window: `s[i - k]` which is `s[2] = 'c'`. Is `'c'` in `vowels`? No.
        * Character entering window: `s[i]` which is `s[5] = 'i'`. Is `'i'` in `vowels`? Yes. `current_vowel_count = 2 + 1 = 3`.
        * New window: `"iii"`. Current count: `3`.
        * `max_vowel_count = max(2, 3) = 3`.

    * **Iteration 4 (i = 6):**
        * Character leaving window: `s[i - k]` which is `s[3] = 'i'`. Is `'i'` in `vowels`? Yes. `current_vowel_count = 3 - 1 = 2`.
        * Character entering window: `s[i]` which is `s[6] = 'd'`. Is `'d'` in `vowels`? No.
        * New window: `"iid"`. Current count: `2`.
        * `max_vowel_count = max(3, 2) = 3`.

    * **Iteration 5 (i = 7):**
        * Character leaving window: `s[i - k]` which is `s[4] = 'i'`. Is `'i'` in `vowels`? Yes. `current_vowel_count = 2 - 1 = 1`.
        * Character entering window: `s[i]` which is `s[7] = 'e'`. Is `'e'` in `vowels`? Yes. `current_vowel_count = 1 + 1 = 2`.
        * New window: `"def"`. Current count: `2`.
        * `max_vowel_count = max(3, 2) = 3`.

    * **Iteration 6 (i = 8):**
        * Character leaving window: `s[i - k]` which is `s[5] = 'i'`. Is `'i'` in `vowels`? Yes. `current_vowel_count = 2 - 1 = 1`.
        * Character entering window: `s[i]` which is `s[8] = 'f'`. Is `'f'` in `vowels`? No.
        * New window: `"efg"`. Current count: `1`.
        * `max_vowel_count = max(3, 1) = 3`.

5.  The loop finishes. The final `max_vowel_count` is `3`.

    The result (`res`) is `3`.

> By always keeping track of the current number of vowels, you can quickly find the maximum as you slide the window across the string. 

---

> This problem is a straightforward application of the fixed-size sliding window. The efficiency comes from incrementally updating the count rather than re-calculating it for each window, which is crucial for large input strings.

### Solution

```python
def maxVowels(s: str, k: int) -> int:
    vowels = {\'a\', \'e\', \'i\', \'o\', \'u\'}
    current_vowel_count = 0

    # 1. Calculate the vowel count for the initial window (first k characters)
    for i in range(k):
        if s[i] in vowels:
            current_vowel_count += 1
    
    max_vowel_count = current_vowel_count

    # 2. Slide the window across the rest of the string
    # The right pointer 'i' starts from k up to len(s) - 1
    for i in range(k, len(s)):
        # Remove the contribution of the character leaving the window
        # The character leaving is at index (i - k)
        if s[i - k] in vowels:
            current_vowel_count -= 1
        
        # Add the contribution of the new character entering the window
        # The new character entering is at index (i)
        if s[i] in vowels:
            current_vowel_count += 1
        
        max_vowel_count = max(max_vowel_count, current_vowel_count)
    
    res = max_vowel_count
    return res
```

**Time Complexity:** The solution involves two main parts: an initial loop to calculate the sum for the first window (which runs `k` times) and then a single loop to slide the window across the remaining `N - k` elements. Each step within the sliding loop takes constant time ($O(1)$) for vowel checks and updates. Therefore, the total time complexity is $O(k + (N - k)) = O(N)$, where $N$ is the length of the string `s`.

**Space Complexity:** You are using a `set` to store vowels and a few integer variables (`current_vowel_count`, `max_vowel_count`, `i`). The size of the `vowels` set is constant (5 elements), and the integer variables consume constant space. Thus, the space complexity is $O(1)$.
