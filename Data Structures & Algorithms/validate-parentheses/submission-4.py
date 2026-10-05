class Solution:
    def isValid(self, s: str) -> bool:
        parenthMap = {'(':')', '{':'}', '[':']'}
        stack = []
        charArr = list(s)
        for char in charArr:
            if char in parenthMap:
                stack.append(char)
            else:
                if len(stack) != 0:
                    top = stack.pop()
                    if parenthMap[top] != char:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False