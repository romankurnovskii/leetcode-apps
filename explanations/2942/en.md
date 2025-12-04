## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= words.length <= 50`, `1 <= words[i].length <= 50`.
- **Time Complexity:** O(n*m) where n is the number of words and m is the average word length - we check each word and character.
- **Space Complexity:** O(k) where k is the number of words containing x - we store indices.
- **Edge Case:** No words contain the character, resulting in an empty array.

**1.2 High-level approach:**
The goal is to find all indices of words that contain the character `x`. We iterate through the words array and check if each word contains the character.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - we need to check each word once.
- **Optimized Strategy:** Use Python's `in` operator to check character membership in each word.

**1.4 Decomposition:**
1. Create an empty result list to store indices.
2. Iterate through words with their indices.
3. Check if the character `x` is in the current word.
4. If found, add the index to the result.
5. Return the list of indices.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `words = ["leet","code"]`, `x = "e"`. We initialize `res = []`.

**2.2 Start Checking:**
We check each word to see if it contains the character.

**2.3 Trace Walkthrough:**

| i | word | "e" in word? | res |
|---|------|--------------|-----|
| 0 | "leet" | Yes | [0] |
| 1 | "code" | Yes | [0,1] |

**2.4 Increment and Loop:**
After checking each word, we move to the next word until all words are processed.

**2.5 Return Result:**
Return `res = [0,1]`, which contains the indices of words containing the character "e".

