## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity**

* **Input Size:** The path string can have length up to 3000 characters.
* **Time Complexity:** $O(n)$ where $n$ is the length of the path. We split the path and process each component once.
* **Space Complexity:** $O(n)$ for the stack storing path components.
* **Edge Case:** Paths like "/../" should simplify to "/". Paths with multiple slashes like "//" should become "/". Paths ending with "/" should have the trailing slash removed (except for root "/").

**1.2 High-level approach**

The goal is to simplify an absolute Unix path by resolving "." (current directory), ".." (parent directory), and multiple slashes. We use a stack to track the valid directory components.

![Stack-based path simplification showing how directories are pushed and popped]

**1.3 Brute force vs. optimized strategy**

* **Brute Force:** Use string manipulation to repeatedly find and replace patterns. This is error-prone and inefficient.
* **Optimized (Stack):** Split the path by "/", process each component: ignore ".", pop from stack for "..", push valid names. This is clean and efficient.

**1.4 Decomposition**

1. Split the path by "/" and filter out empty strings.
2. Use a stack to store valid directory/file names.
3. For each component:
   - If ".", ignore (current directory).
   - If "..", pop from stack if not empty (go up one level).
   - Otherwise, push to stack (valid name).
4. Join stack components with "/" and prepend "/".

### Steps (The "How")

**2.1 Initialization & Example Setup**

Let's use the example $path = "/home/user/Documents/../Pictures"$.

We initialize:
* Split path: `parts = ["home", "user", "Documents", "..", "Pictures"]`
* `stack = []` (empty stack)

**2.2 Start Checking/Processing**

We iterate through each component in `parts`.

**2.3 Trace Walkthrough**

| Component | stack (before) | Action | stack (after) |
|-----------|----------------|--------|---------------|
| "home" | [] | Push | ["home"] |
| "user" | ["home"] | Push | ["home", "user"] |
| "Documents" | ["home", "user"] | Push | ["home", "user", "Documents"] |
| ".." | ["home", "user", "Documents"] | Pop | ["home", "user"] |
| "Pictures" | ["home", "user"] | Push | ["home", "user", "Pictures"] |

**2.4 Increment and Loop**

For each `part` in `parts`:
1. If `part == "."`, continue (do nothing).
2. If `part == ".."`:
   - If `stack` is not empty, `stack.pop()`
3. Otherwise, `stack.append(part)`.

**2.5 Return Result**

After processing all components:
* `stack = ["home", "user", "Pictures"]`
* Join with "/": `"/home/user/Pictures"`
* Return `res = "/home/user/Pictures"`

This is the simplified canonical path.
