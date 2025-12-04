class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # First pass: mark indices to remove
        stack = []
        to_remove = set()
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        
        # Add remaining unmatched '(' to remove set
        to_remove.update(stack)
        
        # Second pass: build result string
        res = []
        for i, char in enumerate(s):
            if i not in to_remove:
                res.append(char)
        
        return ''.join(res)

