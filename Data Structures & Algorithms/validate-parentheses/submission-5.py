class Solution:
    def isValid(self, s: str) -> bool:
        validMap = {'[':']', '(':')', '{':'}'}
        stack = list()
        for p in s:
            if p in validMap.keys():
                stack.append(p)
            else:
                if not stack or validMap[stack.pop()] != p: 
                    return False
        return len(stack) == 0