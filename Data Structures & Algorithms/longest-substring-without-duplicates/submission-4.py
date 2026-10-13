class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        # R = 0
        longestSubStrLen = 0
        seenChars = set()
        for R in range(len(s)):
            if s[R] not in seenChars:
                seenChars.add(s[R])
                longestSubStrLen = max(R-L+1, longestSubStrLen)
            else: 
                while s[R] in seenChars:
                    seenChars.remove(s[L])
                    L += 1
                seenChars.add(s[R])
        return longestSubStrLen