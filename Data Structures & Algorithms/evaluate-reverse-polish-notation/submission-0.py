class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+","-","*","/"]
        value1 = 0
        value2 = 0

        for item in tokens:
            if item not in operators:
                stack.append(int(item))
            else:
                value2 = stack.pop()
                value1 = stack.pop()
                if item == "+":
                    result = value1 + value2
                    stack.append(result)
                elif item == "-":
                    result = value1 - value2
                    stack.append(result)
                elif item == "*":
                    result = value1 * value2
                    stack.append(result)
                elif item == "/":
                    result = int(value1 / value2)
                    stack.append(result)

        return stack[0] 