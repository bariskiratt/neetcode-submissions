class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(val1+val2)
            elif token == "*":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(val1*val2)
            elif token == "-":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(val1-val2)
            elif token == "/":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(int(val1/val2))
            else:
                stack.append(token)
        return int(stack[-1])