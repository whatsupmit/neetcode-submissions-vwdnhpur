class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
                continue
            elif i == "}":
                if len(stack) == 0 or stack[-1] != "{":
                    return False
            elif i == ")":
                if len(stack) == 0 or stack[-1] != "(":
                    return False
            else: # i == "]":
                print(i, stack)
                if len(stack) == 0 or stack[-1] != "[":
                    return False
            stack.pop()
        return len(stack) == 0
            