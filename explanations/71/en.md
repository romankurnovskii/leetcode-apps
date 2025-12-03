# Problem 71: Simplify Path
**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/simplify-path/

## Explanation

### Strategy (The "Why")

The problem asks us to transform an absolute Unix-style file path into its simplified canonical path. We need to handle special directory indicators: `.` (current directory), `..` (parent directory), and multiple consecutive slashes.

**1.1 Constraints & Complexity:**

- **Input Constraints:** $1 \leq \text{path.length} \leq 3000$. The path consists of English letters, digits, period `.`, slash `/`, or underscore `_`.
- **Time Complexity:** $O(n)$ - We split the path once ($O(n)$) and iterate through the parts once ($O(n)$), where $n$ is the length of the path.
- **Space Complexity:** $O(n)$ - We store the split parts and the stack, both of which can contain up to $O(n)$ elements in the worst case.
- **Edge Case:** When the path is `/../`, we cannot go above the root directory, so the result is `/`.

**1.2 High-level approach:**

The goal is to process the path components and build a canonical path by handling `.` (ignore), `..` (go up one level), and multiple slashes (treat as single slash). We use a stack to track the valid directory structure.

![Path simplification visualization](https://assets.leetcode.com/static_assets/others/simplify-path-example.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Manually parse character by character, building the result string while tracking the current depth. This requires complex state management and is error-prone.
- **Optimized (Stack-based):** Split the path by `/`, filter out empty strings and `.`, then use a stack to handle `..` (pop) and valid names (push). Finally, join the stack with `/`. This is clean, efficient, and easy to understand.
- **Emphasize the optimization:** By using a stack, we naturally handle nested directory structures and the `..` operation becomes a simple pop operation, making the logic straightforward and maintainable.

**1.4 Decomposition:**

1. **Split and Filter:** Split the path by `/` and remove empty strings (from multiple slashes) and `.` (current directory indicators).
2. **Process Components:** Iterate through each component.
3. **Handle Parent Directory:** If the component is `..`, pop from the stack (if not empty) to go up one level.
4. **Handle Valid Names:** If the component is a valid directory or file name, push it onto the stack.
5. **Build Result:** Join all stack elements with `/` and prepend `/` to create the canonical path.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `path = "/home/user/Documents/../Pictures"`.

We want to simplify this to `/home/user/Pictures`.

After splitting by `/` and filtering:
- `parts = ['home', 'user', 'Documents', '..', 'Pictures']`
- `stack = []` (initially empty)

**2.2 Start Processing:**

We iterate through each part in the `parts` list.

**2.3 Trace Walkthrough:**

| Part | Action | Stack After Processing | Explanation |
|------|--------|------------------------|-------------|
| `'home'` | Push | `['home']` | Valid directory name |
| `'user'` | Push | `['home', 'user']` | Valid directory name |
| `'Documents'` | Push | `['home', 'user', 'Documents']` | Valid directory name |
| `'..'` | Pop | `['home', 'user']` | Go up one level (remove `'Documents'`) |
| `'Pictures'` | Push | `['home', 'user', 'Pictures']` | Valid directory name |

**2.4 Building the Result:**

After processing all parts, the stack contains `['home', 'user', 'Pictures']`.

We join these with `/` to get `'home/user/Pictures'`, then prepend `/` to get the final result: `/home/user/Pictures`.

**2.5 Return Result:**

The function returns `/home/user/Pictures`, which is the simplified canonical path.

> **Note:** Sequences like `'...'` or `'....'` are treated as valid directory or file names, not as special indicators. Only `'.'` and `'..'` have special meaning.
