## 345. Reverse Vowels of a String [Easy]

https://leetcode.com/problems/reverse-vowels-of-a-string

## Description
Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

**Examples**

```tex
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation: The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Input: s = "leetcode"
Output: "leotcede"
```

**Constraints**

```tex
1 <= s.length <= 3 * 10^5
s consist of printable ASCII characters.
```

## Explanation

### Strategy
- **Type:** String, Two Pointers
- **Given:** A string `s`
- **Asked:** Reverse only the vowels in `s`, keeping all other characters in their original positions

#### What does "reverse vowels" mean?
- Only the vowels ('a', 'e', 'i', 'o', 'u', both lowercase and uppercase) should be reversed in order. All other characters stay in place.

Ro reverse only the vowels in the string efficiently, you can use **two pointers**: one starting from the left, one from the right. You *move* each pointer until it finds a vowel. When both pointers are at vowels, you *swap* them.

You do this because it lets you reverse the vowels in-place, without affecting the other characters. Using two pointers is efficient and avoids unnecessary work, especially for long strings.

You keep moving the pointers toward each other, swapping vowels as you go, until they meet in the middle. This ensures every vowel is swapped exactly once, making the solution both correct and efficient.

#### High-Level Plan
1. Use two pointers: one starting from the left, one from the right.
2. Move each pointer until it finds a vowel.
3. When both pointers are at vowels, swap them.
4. Move the pointers toward each other and repeat until they meet.

### Steps

Let's walk through an example: s = "IceCreAm"

1. Vowels in s: ['I', 'e', 'e', 'A']
2. Start with pointers at the beginning and end.
3. Swap 'I' (start) with 'A' (end): "AceCreIm"
4. Move pointers inward, swap 'e' with 'e' (no visible change)
5. Continue until pointers meet
6. Result: "AceCreIm"

> **Note:**
> - Using two pointers is efficient and avoids unnecessary work, especially for long strings.
> - You only need to check for vowels and swap them; all other characters remain unchanged.

- **Time Complexity:** O(n), where n is the length of the string
- **Space Complexity:** O(n)