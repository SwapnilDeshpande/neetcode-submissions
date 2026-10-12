class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0 
        maxf = 0
        charSet = {}
        res = 0
        for R in range(len(s)):

            charSet[s[R]] = charSet.get(s[R], 0) + 1
            maxf = max(maxf, charSet.get(s[R]))
            if (R-L+1) - maxf > k:
                charSet[s[L]] -= 1
                L += 1

            res = max(res, R-L+1)
        return res
