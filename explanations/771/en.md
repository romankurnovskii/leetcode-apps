## 771. Jewels and Stones

You are given two strings:

* `jewels`: characters that represent types of stones that are jewels.
* `stones`: characters where each character is a stone you have.

Return **how many characters in `stones` are also in `jewels`**.

Letters are **case-sensitive**, so `"a"` is different from `"A"`.

### Example 1

**Input:** `jewels = "aA"`, `stones = "aAAbbbb"`
**Output:** `3`
**Explanation:** The stones `"a"`, `"A"`, `"A"` are jewels.

### Example 2

**Input:** `jewels = "z"`, `stones = "ZZ"`
**Output:** `0`

### Constraints

* `1 <= jewels.length, stones.length <= 50`
* `jewels` and `stones` consist of only English letters.
* All the characters of `jewels` are **unique**.

---

## Explanation

### Strategy

Think of `jewels` as an **“allowed list”** of special stone types, and `stones` as a **bag** of stones you own.

Your task is:
**for every stone in your bag, check if its type is in the allowed list. If yes, count it.**

* **What is given**

  * `jewels`: which letters are considered jewels
  * `stones`: the stones you have (each character is one stone)
* **What is asked**

  * total number of characters in `stones` that appear in `jewels`
* **Type of problem**

  * strings + counting + membership check (`in`)
* **Important detail**

  * Case-sensitive: `"a"` and `"A"` are different

High-level plan:

1. Start a counter at 0.
2. Look at each character in `stones` one by one.
3. If that character exists inside `jewels`, increment the counter.
4. Return the counter.

Guiding questions for beginners:

* “If I pick one stone from `stones`, is it one of the jewel types in `jewels`?”
* “How many times do I say ‘yes’ while scanning all stones?”

### Steps

We will follow the exact logic of your code:

```python
result = 0
for s in stones:
    if s in jewels:
        result += 1
return result
```

#### Step 1: Create a counter

We use `result` to store how many jewels we found so far.

* At the start: `result = 0`
* Why? Because before checking any stones, we found zero jewels.

#### Step 2: Scan every stone

`for x in stones:` means:

* Take stones one by one from left to right.
* Put the current stone’s character into `x`.

If `stones = "aAAbbbb"`, then `x` will be:
`'a'`, then `'A'`, then `'A'`, then `'b'`, `'b'`, `'b'`, `'b'`.

#### Step 3: Check if the stone is a jewel

`if x in jewels:` checks membership.

* If `jewels = "aA"`, then:

  * `'a' in "aA"` → True
  * `'A' in "aA"` → True
  * `'b' in "aA"` → False

If True, we do `result += 1`.

---

### Walkthrough Example 1 (very detailed)

**Input:**

* `jewels = "aA"`
* `stones = "aAAbbbb"`

Start: `result = 0`

| Current stone `x` | Is `x` in `jewels` ("aA")? | result after |
| ----------------- | -------------------------- | ------------ |
| `'a'`             | yes                        | 1            |
| `'A'`             | yes                        | 2            |
| `'A'`             | yes                        | 3            |
| `'b'`             | no                         | 3            |
| `'b'`             | no                         | 3            |
| `'b'`             | no                         | 3            |
| `'b'`             | no                         | 3            |

Return `3`.

---

### Extra examples

#### Example 3: Case sensitivity

* `jewels = "a"`
* `stones = "AaAa"`

Check each stone:

* `'A' in "a"` → False (uppercase is different)
* `'a' in "a"` → True

So only the lowercase `a` counts.

Result: `2` (there are two lowercase `a` characters)

#### Example 4: All stones are jewels

* `jewels = "abc"`
* `stones = "cba"`

Every character in `stones` is in `jewels`, so result is `3`.

#### Example 5: No matches

* `jewels = "x"`
* `stones = "aaaa"`

`'a' in "x"` is always False, so result is `0`.

---

> **Note:** Your solution uses `x in jewels` where `jewels` is a string. This is simple and readable for beginners. In the worst case, Python may scan through the whole `jewels` string to decide if `x` is present.

**Time Complexity:** `O(len(stones) * len(jewels))` (worst case)
**Space Complexity:** `O(1)`
