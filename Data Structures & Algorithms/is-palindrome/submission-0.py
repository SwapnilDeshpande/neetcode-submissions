class Solution:
    def isPalindrome(self, s: str) -> bool:
        strWithNoAlphNum = []
        for char in s:
            if char.isalnum():
                strWithNoAlphNum.append(char.lower())

        stack = []
        lenToPush = int(len(strWithNoAlphNum)/2)
        for i in range(0, lenToPush):
            stack.append(strWithNoAlphNum[i])
        if len(strWithNoAlphNum) % 2 == 0:
            for i in range(lenToPush, len(strWithNoAlphNum)):
                c = stack.pop()
                if c != strWithNoAlphNum[i]:
                    return False
        else:
            for i in range(lenToPush+1, len(strWithNoAlphNum)):
                c = stack.pop()
                if c != strWithNoAlphNum[i]:
                    return False
        return True