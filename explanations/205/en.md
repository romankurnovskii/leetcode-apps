## 205. Isomorphic Strings [Easy]

https://leetcode.com/problems/isomorphic-strings

## Description

Given two strings `s` and `t`, *determine if they are isomorphic*.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Examples**

```tex
Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
- Mapping 'e' to 'a'.
- Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true
```

**Constraints**
```tex
- 1 <= s.length <= 5 * 10^4
- t.length == s.length
- s and t consist of any valid ascii character
```

## Explanation

### Strategy
Let's restate the problem: You're given two strings of equal length, and you need to determine if they are isomorphic. Two strings are isomorphic if there's a one-to-one mapping between characters that can transform one string into the other.

This is a **hash table problem** that requires tracking character mappings in both directions to ensure the isomorphism property.

**What is given?** Two strings `s` and `t` of equal length.

**What is being asked?** Determine if the strings are isomorphic (can be transformed into each other via character replacement).

**Constraints:** The strings can be up to 50,000 characters long and contain any valid ASCII character.

**Edge cases:** 
- Empty strings
- Single character strings
- Strings with all identical characters
- Strings with complex character mappings

**High-level approach:**
The solution involves using two hash maps to track character mappings in both directions, ensuring that the mapping is consistent throughout both strings.

**Decomposition:**
1. **Check length equality**: If strings have different lengths, they can't be isomorphic
2. **Create mapping dictionaries**: Track character mappings from s to t and from t to s
3. **Iterate through characters**: Check each character pair for mapping consistency
4. **Verify isomorphism**: Ensure no conflicts in the mapping

**Brute force vs. optimized strategy:**
- **Brute force**: Try all possible character mappings. This is extremely inefficient.
- **Optimized**: Use hash tables to track mappings in a single pass. This takes O(n) time.

### Steps
Let's walk through the solution step by step using the first example: `s = "egg"`, `t = "add"`

**Step 1: Initialize mapping dictionaries**
- `s_to_t = {}` (maps characters from s to t)
- `t_to_s = {}` (maps characters from t to s)

**Step 2: Check first character pair**
- `s[0] = 'e'`, `t[0] = 'a'`
- Check if 'e' is already mapped: No
- Check if 'a' is already mapped: No
- Add mappings: `s_to_t['e'] = 'a'`, `t_to_s['a'] = 'e'`

**Step 3: Check second character pair**
- `s[1] = 'g'`, `t[1] = 'd'`
- Check if 'g' is already mapped: No
- Check if 'd' is already mapped: No
- Add mappings: `s_to_t['g'] = 'd'`, `t_to_s['d'] = 'g'`

**Step 4: Check third character pair**
- `s[2] = 'g'`, `t[2] = 'd'`
- Check if 'g' is already mapped: Yes, to 'd'
- Verify consistency: `s_to_t['g'] == 'd'` ✓
- Check if 'd' is already mapped: Yes, to 'g'
- Verify consistency: `t_to_s['d'] == 'g'` ✓

**Step 5: Result**
- All character pairs are consistent
- Strings are isomorphic: `true`

**Why this works:**
By maintaining mappings in both directions, we ensure that:
1. No character in `s` maps to multiple characters in `t`
2. No character in `t` is mapped to by multiple characters in `s`
3. The mapping is consistent throughout both strings

> **Note:** The key insight is using bidirectional mapping to ensure the isomorphism property. We need to check both that each character in s maps to exactly one character in t, and that each character in t is mapped to by exactly one character in s.

**Time Complexity:** O(n) - we visit each character once  
**Space Complexity:** O(k) - where k is the number of unique characters (bounded by ASCII character set)
