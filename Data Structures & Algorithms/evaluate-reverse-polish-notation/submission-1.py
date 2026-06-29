class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','-','*','/']
        arr = []
        for s in tokens:
            if s not in operators:
                arr.append(s)
            else:
                num1 = int(arr.pop())
                num2 = int(arr.pop())
                if s == '+':
                    result = num1 + num2
                    arr.append(result)
                elif s == '-':
                    result = num2 - num1
                    arr.append(result)
                elif s == '*':
                    result = num1 * num2
                    arr.append(result)
                elif s == '/':
                    result = num2 / num1
                    arr.append(result)
        return int(arr[0])
            