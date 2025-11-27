## Explanation

### Strategy (The "Why")

Given a string `s`, we need to reverse only the vowels ('a', 'e', 'i', 'o', 'u' in both lowercase and uppercase) while keeping all other characters in their original positions.

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be up to $3 \times 10^5$.
- **Value Range:** The string consists of printable ASCII characters.
- **Time Complexity:** $O(n)$ - We iterate through the string once with two pointers.
- **Space Complexity:** $O(n)$ - We convert the string to a list for in-place modification.
- **Edge Case:** If there are no vowels, the string remains unchanged. If there's only one vowel, it stays in place.

**1.2 High-level approach:**

The goal is to reverse the order of vowels in a string.

![Reverse Vowels](https://assets.leetcode.com/uploads/2021/08/04/vowels.jpg)

We use two pointers starting at both ends. We find vowels from both sides and swap them, continuing until the pointers meet.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Extract all vowels, reverse them, then reconstruct the string. This requires multiple passes.
- **Optimized Strategy (Two Pointers):** Use two pointers to find vowels from both ends and swap them in-place. This takes one pass.
- **Why it's better:** The two-pointer approach is more efficient and processes the string in a single pass, swapping vowels as we find them.

**1.4 Decomposition:**

1. Convert string to a list for in-place modification.
2. Create a set of vowels for $O(1)$ lookup.
3. Initialize two pointers at both ends.
4. While `left < right`:
   - Move left pointer until it finds a vowel.
   - Move right pointer until it finds a vowel.
   - Swap the vowels.
   - Move both pointers inward.
5. Convert the list back to a string and return.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $s = "hello"$

We initialize:
- `s_list = ['h', 'e', 'l', 'l', 'o']`
- `vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}`
- `left = 0`, `right = 4`

**2.2 Start Processing:**

We begin searching for vowels from both ends.

**2.3 Trace Walkthrough:**

| Step | left | right | s_list[left] | s_list[right] | Action |
|------|------|-------|---------------|----------------|--------|
| 1 | 0 | 4 | 'h' (not vowel) | 'o' (vowel) | Move left to 1 |
| 2 | 1 | 4 | 'e' (vowel) | 'o' (vowel) | Swap: 'o' and 'e' |
| 3 | 2 | 3 | 'l' (not vowel) | 'l' (not vowel) | left >= right, exit |

After swap: `s_list = ['h', 'o', 'l', 'l', 'e']`

**2.4 Final Result:**

We convert back to string: `"holle"`

**2.5 Return Result:**

We return `"holle"`, which has vowels 'e' and 'o' reversed from the original "hello".

> **Note:** The two-pointer technique efficiently finds and swaps vowels from both ends. We skip non-vowel characters by moving the pointers until we find vowels, then swap and continue.
