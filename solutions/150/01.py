class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                # Pop two operands
                b = stack.pop()
                a = stack.pop()
                
                # Perform operation
                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                else:  # token == '/'
                    res = int(a / b)  # Truncate towards zero
                
                stack.append(res)
            else:
                # It's a number
                stack.append(int(token))
        
        return stack[0]

