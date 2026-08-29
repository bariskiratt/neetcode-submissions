class Solution:
    def isValid(self, s: str) -> bool:
        openToClosed = {"(":")","{":"}","[":"]"}
        stack = []
        for c in s:
            if c in openToClosed:
                stack.append(c)
                continue
            if stack and c not in openToClosed and c!=openToClosed[stack[-1]]:
                return False
            elif stack:
                stack.pop()
            else:
                return False
        return True if not stack else False