## 3602. Hexadecimal and Hexatrigesimal Conversion [Easy]

https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion

## Description

You are given an integer `n`.

Return the concatenation of the **hexadecimal** representation of `n^2` and the **hexatrigesimal** representation of `n^3`.

A **hexadecimal** number is defined as a base-16 numeral system that uses the digits `0 – 9` and the uppercase letters `A - F` to represent values from 0 to 15.

A **hexatrigesimal** number is defined as a base-36 numeral system that uses the digits `0 – 9` and the uppercase letters `A - Z` to represent values from 0 to 35.

**Examples**

**Example 1:**
```tex
Input: n = 13

Output: "A91P1"

Explanation:
- n^2 = 13 * 13 = 169. In hexadecimal, 169 = (10 * 16) + 9 = "A9".
- n^3 = 13 * 13 * 13 = 2197. In hexatrigesimal, 2197 = (1 * 36^2) + (25 * 36) + 1 = "1P1".
- Concatenating both results gives "A9" + "1P1" = "A91P1".
```

**Example 2:**
```tex
Input: n = 36

Output: "5101000"

Explanation:
- n^2 = 36 * 36 = 1296. In hexadecimal, 1296 = (5 * 16^2) + (1 * 16) + 0 = "510".
- n^3 = 36 * 36 * 36 = 46656. In hexatrigesimal, 46656 = (1 * 36^3) + (0 * 36^2) + (0 * 36) + 0 = "1000".
- Concatenating both results gives "510" + "1000" = "5101000".
```

**Constraints**

```tex
1 <= n <= 1000
```

## Explanation

### Strategy

Let's break down the problem step by step:

- **Type:** Math, String conversion, Number bases
- **Given:** An integer `n` (1 ≤ n ≤ 1000)
- **Asked:** Return the concatenation of:
    - The hexadecimal (base-16, using 0-9 and A-F) representation of `n^2`
    - The hexatrigesimal (base-36, using 0-9 and A-Z) representation of `n^3`

#### What is hexadecimal?
- Base-16: digits 0-9, then A=10, B=11, ..., F=15
- Example: 169 in hex is 10*16 + 9 = "A9"

#### What is hexatrigesimal?
- Base-36: digits 0-9, then A=10, ..., Z=35
- Example: 2197 in base-36: 2197 // 36^2 = 1, remainder 25*36+1 = 1P1

#### Constraints/Edge Cases
- n is always positive and ≤ 1000, so n^2 and n^3 fit in standard integer types
- No negative numbers or zero

#### High-Level Plan
1. Compute n^2 and n^3
2. Convert n^2 to hexadecimal (uppercase)
3. Convert n^3 to base-36 (uppercase)
4. Concatenate the two strings and return

### Steps

Let's walk through an example: n = 13

1. Compute n^2 = 169, n^3 = 2197
2. Convert 169 to hexadecimal:
    - 169 // 16 = 10, remainder 9 → '9'
    - 10 // 16 = 0, remainder 10 → 'A'
    - So, hex: 'A9'
3. Convert 2197 to base-36:
    - 2197 // 36 = 61, remainder 1 → '1'
    - 61 // 36 = 1, remainder 25 → 'P'
    - 1 // 36 = 0, remainder 1 → '1'
    - So, base-36: '1P1'
4. Concatenate: 'A9' + '1P1' = 'A91P1'

> **Note:**
> - Python's `format(x, 'X')` gives uppercase hexadecimal.
> - For base-36, you can build the string by repeated division and mapping remainders to '0'-'9', 'A'-'Z'.

- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n)
