class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by '/' and filter out empty strings and '.'
        parts = [p for p in path.split('/') if p and p != '.']
        
        # Use a stack to build the canonical path
        stack = []
        
        for part in parts:
            if part == '..':
                # Go up one directory: pop if stack is not empty
                if stack:
                    stack.pop()
            else:
                # Valid directory or file name: push to stack
                stack.append(part)
        
        # Build the result path
        res = '/' + '/'.join(stack)
        return res
