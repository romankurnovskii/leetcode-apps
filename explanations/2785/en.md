## Explanation

### Strategy

**Constraints & Edge Cases**

* **String Length:** The string s has length 1-10^5, consisting of uppercase and lowercase English letters.
* **Time Complexity:** We need to extract vowels (O(n)), sort them (O(k log k) where k is number of vowels), and rebuild the string (O(n)). **Time Complexity: O(n + k log k)** where k is the number of vowels, **Space Complexity: O(n)** for storing vowels and result.
* **Edge Case:** If there are no vowels, return the original string unchanged.

**High-level approach**

The problem asks us to sort vowels in non-decreasing ASCII order while keeping consonants in their original positions.

**Brute force vs. optimized strategy**

* **Brute Force:** For each vowel position, find the next smallest vowel to place there. This would be O(n²) time.
* **Optimized:** Extract all vowels, sort them, then replace vowels in order. This is O(n + k log k) where k is the number of vowels.

**Decomposition**

1. **Identify Vowels:** Create a set of vowels (both uppercase and lowercase).
2. **Extract and Sort:** Collect all vowels from the string and sort them by ASCII value.
3. **Rebuild String:** Traverse the original string, replacing vowels with sorted vowels in order.

### Steps

1. **Initialization & Example Setup**
   Let's use `s = "lEetcOde"` as our example.
   - Define vowels set: `{'a','e','i','o','u','A','E','I','O','U'}`.
   - Initialize `vowel_list = []` and `res = []`.

2. **Extract Vowels**
   - Traverse s: 'l' (consonant), 'E' (vowel), 'e' (vowel), 't' (consonant), 'c' (consonant), 'O' (vowel), 'd' (consonant), 'e' (vowel).
   - `vowel_list = ['E', 'e', 'O', 'e']`.
   - Sort: `['E', 'O', 'e', 'e']` (ASCII: E=69, O=79, e=101, e=101).

3. **Trace Walkthrough**

| Index | Character | Is Vowel? | Sorted Vowel | Result So Far |
|-------|-----------|-----------|---------------|---------------|
| 0     | 'l'       | No        | -             | "l"           |
| 1     | 'E'       | Yes       | 'E' (idx 0)   | "lE"          |
| 2     | 'e'       | Yes       | 'O' (idx 1)   | "lEO"         |
| 3     | 't'       | No        | -             | "lEOt"        |
| 4     | 'c'       | No        | -             | "lEOtc"       |
| 5     | 'O'       | Yes       | 'e' (idx 2)   | "lEOtce"      |
| 6     | 'd'       | No        | -             | "lEOtced"     |
| 7     | 'e'       | Yes       | 'e' (idx 3)   | "lEOtcede"    |

4. **Rebuild String**
   - Use index `vowel_idx = 0` to track position in sorted vowel list.
   - For each character: if vowel, append `vowel_list[vowel_idx]` and increment; otherwise append original character.

5. **Return Result**
   Return `''.join(res)` = `"lEOtcede"`.
