## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** Products array can have up to 1000 strings, each up to 3000 characters. SearchWord can be up to 1000 characters.
* **Time Complexity:** O(m * log m + n * m) where m is products length and n is searchWord length. Sorting takes O(m log m), and for each character we scan products.
* **Space Complexity:** O(m) for sorted products plus O(n * 3) for results.
* **Edge Case:** If no products match a prefix, return an empty list for that prefix.

**1.2 High-level approach:**

The goal is to suggest up to 3 products that have a common prefix with the search word as each character is typed. We sort products first, then for each prefix, find matching products.

![Prefix matching showing how products are filtered as each character is typed]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** For each prefix, scan all products and filter those starting with the prefix. This is O(n * m) where n is searchWord length.
* **Optimized (Sorting + Linear Scan):** Sort products once, then for each prefix, scan from the beginning and collect up to 3 matches. This is O(m log m + n * m).
* **Why it's better:** Sorting ensures we get lexicographically minimum products first, and we can stop after finding 3 matches.

**1.4 Decomposition:**

1. Sort the products array lexicographically.
2. For each character in searchWord:
   - Build the current prefix.
   - Scan products from the beginning.
   - Collect products that start with the prefix (up to 3).
   - Add to results.
3. Return the list of suggestion lists.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"

We initialize:
* Sort products: ["mobile","moneypot","monitor","mouse","mousepad"]
* `res = []`
* `prefix = ""`

**2.2 Start Checking/Processing:**

We iterate through each character in searchWord.

**2.3 Trace Walkthrough:**

| Char | prefix | Matching Products | Suggestions |
|------|--------|-------------------|-------------|
| 'm' | "m" | mobile, moneypot, monitor | ["mobile","moneypot","monitor"] |
| 'o' | "mo" | mobile, moneypot, monitor | ["mobile","moneypot","monitor"] |
| 'u' | "mou" | mouse, mousepad | ["mouse","mousepad"] |
| 's' | "mous" | mouse, mousepad | ["mouse","mousepad"] |
| 'e' | "mouse" | mouse, mousepad | ["mouse","mousepad"] |

**2.4 Increment and Loop:**

After processing each character, we append the suggestions list to results and continue.

**2.5 Return Result:**

After processing all characters, `res = [["mobile","moneypot","monitor"], ["mobile","moneypot","monitor"], ["mouse","mousepad"], ["mouse","mousepad"], ["mouse","mousepad"]]` is returned.

