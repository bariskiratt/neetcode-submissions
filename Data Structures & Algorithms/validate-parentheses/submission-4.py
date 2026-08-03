class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'(': ')', '{' : '}' , '[' : ']'}
        stack  = []
        for c in s:
            if c in closeToOpen:
                stack.append(c)
            elif stack and c == closeToOpen[stack[-1]]:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
