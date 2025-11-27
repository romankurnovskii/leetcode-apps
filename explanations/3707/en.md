## Explanation

### Strategy

**Constraints & Edge Cases**

  * **String Length:** The string can have 2 to 100 characters, so brute force is acceptable.
  * **Character Set:** Only lowercase English letters.
  * **Time Complexity:** We try all possible split positions ($n-1$ positions), and for each split we calculate scores in $O(n)$. Overall $O(n^2)$.
  * **Space Complexity:** $O(1)$ - we only need a few variables.
  * **Edge Case:** If the string has length 2, there's only one possible split position.

**High-level approach**
The problem asks us to determine if we can split the string into two non-empty substrings with equal scores.

  * The **score** of a string is the sum of character positions in the alphabet (a=1, b=2, ..., z=26).
  * We need to try all possible split positions and check if the left and right substrings have equal scores.
  * For a split at index $i$, the left substring is $s[0..i]$ and the right substring is $s[i+1..n-1]$.

**Brute force vs. optimized strategy**

  * **Brute Force:** Try all possible split positions (from 0 to $n-2$), calculate the score of both substrings for each split, and check if they're equal. This is $O(n^2)$.
  * **Optimized (Prefix Sum):** We could use prefix sums to calculate scores in $O(1)$ per split, reducing the overall complexity to $O(n)$. However, for the given constraints ($n \leq 100$), the brute force approach is acceptable and simpler to understand.

**Decomposition**

1.  **Iterate Split Positions:** Try all possible split positions from index 0 to $n-2$ (ensuring both substrings are non-empty).
2.  **Calculate Left Score:** For each split position, calculate the score of the left substring $s[0..i]$.
3.  **Calculate Right Score:** Calculate the score of the right substring $s[i+1..n-1]$.
4.  **Check Equality:** If the scores are equal, return `True`.
5.  **Return Result:** If no split produces equal scores, return `False`.

### Steps

1.  **Initialize**
    Get the length of the string $n$. We'll try all split positions from 0 to $n-2$.

2.  **Try Each Split Position**
    For each split position $i$ from 0 to $n-2$:
      * Left substring: $s[0..i]$ (indices 0 to $i$, inclusive)
      * Right substring: $s[i+1..n-1]$ (indices $i+1$ to $n-1$, inclusive)

3.  **Calculate Left Score**
    For the left substring $s[0..i]$, iterate through each character and sum their alphabet positions:
      * For character $c$, its position is $ord(c) - ord('a') + 1$
      * For example, 'a' = 1, 'b' = 2, 'z' = 26

4.  **Calculate Right Score**
    Similarly, for the right substring $s[i+1..n-1]$, calculate the sum of character positions.

5.  **Check and Return**
    If `left_score == right_score` for any split position, return `True`. If we've tried all splits and none work, return `False`.

**Example Walkthrough:**
For $s = "adcb"$:
  * Split at $i=0$: left="a" (score=1), right="dcb" (score=4+3+2=9) → not equal
  * Split at $i=1$: left="ad" (score=1+4=5), right="cb" (score=3+2=5) → **equal!** Return `True`

