class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0 
        substr = set()
        if len(s) == 0:
            return 0
        for R in range(len(s)):
            while s[R] in substr:
                substr.remove(s[L])
                L += 1
            substr.add(s[R])
            length = max(length, R-L+1)
        return length