class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "*/+-":
                if i == '+':
                    temp = int(stack[-1]) + int(stack[-2])
                elif i == '*' :
                    temp = int(stack[-1]) * int(stack[-2])
                elif i == '-':
                    temp = int(stack[-2]) - int(stack[-1])
                else :
                    temp = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(temp)
            else :
                stack.append(i)
        return int(stack[-1])