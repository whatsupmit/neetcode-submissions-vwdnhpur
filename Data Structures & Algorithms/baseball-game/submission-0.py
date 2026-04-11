class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "D":
                value = stack[-1]
                stack.append(value * 2)
            elif i == "C":
                stack.pop()
            elif i == "+":
                value1 = stack.pop()
                value0 = stack[-1]
                stack.append(value1)
                stack.append(value0 + value1)
            else:
                stack.append(int(i))

        return sum(stack)
