class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split path by '/' and filter out empty strings
        parts = [p for p in path.split("/") if p]
        stack = []

        for part in parts:
            if part == ".":
                # Current directory, do nothing
                continue
            elif part == "..":
                # Parent directory, go up one level
                if stack:
                    stack.pop()
            else:
                # Valid directory or file name
                stack.append(part)

        # Construct result path
        res = "/" + "/".join(stack)
        return res
