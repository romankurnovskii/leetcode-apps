## 1071. Greatest Common Divisor of Strings [Easy]

https://leetcode.com/problems/greatest-common-divisor-of-strings

## Description
For two strings `s` and `t`, we say "t divides s" if and only if `s = t + t + ... + t` (i.e., t is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.

**Examples**
```tex
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Input: str1 = "LEET", str2 = "CODE"
Output: ""
```

**Constraints**
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of English uppercase letters.

> Try to find the greatest common divisor (GCD) of the lengths of the two strings, and check if the substring of that length divides both strings.

## Explanation

### Strategy
Let's restate the problem: Given two strings, find the largest string that can be repeated to form both strings exactly. This is a string manipulation problem with a mathematical twist (using the greatest common divisor, or GCD).

- **What is given?** Two strings, `str1` and `str2`.
- **What is being asked?** Find the largest string x such that both str1 and str2 are made by repeating x some number of times.
- **Constraints:** Both strings are non-empty, up to 1000 characters, and only contain uppercase English letters.
- **Edge cases:** If the strings cannot be built from the same repeating substring, the answer is an empty string.

Suppose you have two strings, and you want to find the biggest chunk that can be repeated to make both strings. Think of it like finding the biggest building block that fits perfectly into **both**.

First, you check if both strings can be built by repeating the same substring, because if they can't, there's no **common divisor** string. You do this by comparing `str1 + str2` and `str2 + str1` — if they're not the same, it means the order of repetition doesn't match, so no common divisor exists. This check is important because it quickly rules out impossible cases, saving you time and effort.

Next, you use the greatest common divisor (GCD) of the lengths of the two strings. You do this because the largest possible repeating substring must fit evenly into both strings, and the GCD gives you the largest length that divides both. This is a mathematical shortcut that ensures you only check the most promising candidate.

Finally, you take the substring of that length from the start of either string and check if repeating it forms both strings. This works because if a substring can build both strings by repetition, it must be the answer. 

**High-level plan:**
1. If `str1 + str2 != str2 + str1`, there is no common divisor string. Return "".
2. Otherwise, the answer is the substring of length gcd(len(str1), len(str2)) from the start of either string.

> Try to find the greatest common divisor (GCD) of the lengths of the two strings, and check if the substring of that length divides both strings.

### Steps
1. **Check for a valid repeating pattern:**
   - Concatenate `str1 + str2` and `str2 + str1`. If they are not equal, it means the two strings cannot be built from the same repeating substring. For example:
     - `str1 = "ABCABC", str2 = "ABC"` → `"ABCABCABC" == "ABCABCABC"` (valid)
     - `str1 = "LEET", str2 = "CODE"` → `"LEETCODE" != "CODELEET"` (invalid)

2. **Find the GCD of the lengths:**
   - If the pattern is valid, compute the greatest common divisor (GCD) of the lengths of str1 and str2. This gives the largest possible length for the repeating substring.
   - Example: `str1 = "ABABAB"` (length 6), `str2 = "ABAB"` (length 4). GCD(6, 4) = 2.

3. **Extract the substring:**
   - Take the substring of length GCD from the start of either string. This is the candidate for the greatest common divisor string.
   - Example: `str1 = "ABABAB", str2 = "ABAB"`. GCD = 2, so substring = "AB".

4. **Return the result:**
   - If the above checks pass, return the substring. Otherwise, return an empty string.

> The key insight is that if two strings are made by repeating the same substring, their concatenations in both orders must be equal. This is a quick way to check for a common divisor string.
