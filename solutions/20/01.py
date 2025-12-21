class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                # Closing bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                # Opening bracket
                stack.append(char)

        return len(stack) == 0
