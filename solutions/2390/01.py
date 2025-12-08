class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == '*':
                # Remove the closest non-star character to the left
                if stack:
                    stack.pop()
            else:
                # Push non-star characters onto the stack
                stack.append(char)
        
        # Convert stack to string
        res = ''.join(stack)
        return res
