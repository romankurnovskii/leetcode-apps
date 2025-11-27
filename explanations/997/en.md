## Explanation

### Strategy (The "Why")

In a town of $n$ people labeled from 1 to $n$, there is a judge. The judge trusts nobody, and everybody (except the judge) trusts the judge. Given an array `trust` where `trust[i] = [a, b]` means person `a` trusts person `b`, we need to find the judge.

**1.1 Constraints & Complexity:**

- **Input Size:** $n$ can be between $1$ and $1000$, and `trust.length` can be up to $10^4$.
- **Value Range:** People are labeled from 1 to $n$.
- **Time Complexity:** $O(n + t)$ where $t$ is the length of `trust`. We iterate through `trust` once and then through all people once.
- **Space Complexity:** $O(n)$ - We use two arrays of size $n+1$ to count trusts.
- **Edge Case:** If $n = 1$ and `trust` is empty, person 1 is the judge. If there's no judge (multiple people or nobody satisfies the conditions), return -1.

**1.2 High-level approach:**

The goal is to find the person who is trusted by everyone else and trusts nobody.

We count two things for each person: how many people they trust, and how many people trust them. The judge trusts nobody (count = 0) and is trusted by everyone else (count = $n-1$).

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each person, check if they trust nobody and if everyone else trusts them. This takes $O(n \times t)$ time.
- **Optimized Strategy (Counting):** Count trusts in one pass, then check each person's counts. This takes $O(n + t)$ time.
- **Why it's better:** The counting approach reduces time complexity by processing the trust array once instead of checking each person against all trust relationships.

**1.4 Decomposition:**

1. Create two arrays: one to count how many people each person trusts, another to count how many people trust each person.
2. Iterate through the `trust` array, updating both counts.
3. For each person from 1 to $n$, check if they trust nobody and are trusted by $n-1$ people.
4. If such a person is found, return their label. Otherwise, return -1.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $n = 3$, $trust = [[1,3],[2,3]]$

We initialize:
- `trusting_count = [0, 0, 0, 0]` (indices 0-3, person 0 unused)
- `trust_count = [0, 0, 0, 0]`

**2.2 Start Counting:**

We iterate through the trust array.

**2.3 Trace Walkthrough:**

**Phase 1: Count trusts**

| Trust pair | trusting_count | trust_count |
|------------|----------------|-------------|
| [1,3] | [0,1,0,0] | [0,0,0,1] |
| [2,3] | [0,1,1,0] | [0,0,0,2] |

**Phase 2: Check each person**

| Person | trusting_count[i] | trust_count[i] | Is Judge? |
|--------|-------------------|-----------------|-----------|
| 1 | 1 | 0 | No (trusts someone) |
| 2 | 1 | 0 | No (trusts someone) |
| 3 | 0 | 2 | **Yes!** (trusts nobody, trusted by 2 = n-1) |

**2.4 Explanation:**

- Person 3 trusts nobody (trusting_count[3] = 0) ✓
- Person 3 is trusted by 2 people (trust_count[3] = 2 = n-1) ✓
- Therefore, person 3 is the judge.

**2.5 Return Result:**

We return 3, which is the label of the judge.

> **Note:** The key insight is that the judge has two distinct properties: they trust nobody (outgoing trust count = 0) and everyone else trusts them (incoming trust count = n-1). By counting both directions, we can identify the judge efficiently.

