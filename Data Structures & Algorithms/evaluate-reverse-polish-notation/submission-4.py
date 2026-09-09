class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "*/+-":
                a , b = int(stack.pop()) , int(stack.pop())
                if i == '+':
                    stack.append(a + b)
                elif i == '*' :
                    stack.append(b * a)
                elif i == '-':                   
                    stack.append(b - a)
                else :
                    stack.append(b / a)
            else :
                stack.append(i)
        return int(stack[-1])
        