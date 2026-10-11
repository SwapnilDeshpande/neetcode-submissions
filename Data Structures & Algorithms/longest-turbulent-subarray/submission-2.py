class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L, R = 0, 1
        res = 1
        prevSign = ""
        while R < len(arr):
            if arr[R-1] < arr[R] and prevSign != "<":
                res = max(res, R-L+1)
                prevSign = "<"
                R += 1
            elif arr[R-1] > arr[R] and prevSign != ">":
                res = max(res, R-L+1)
                prevSign = ">"
                R += 1
            else:
                # If the 2 adjecent elements are equal, skip the elements that are equal (because they won't cause the
                # elements to be turbulent).
                # If the 2 adjecent elements are not equal, you can start the left pointer (i.e. L) to start from the
                # the previous element because it will still contribute to the array turbulence. 
                R = R if arr[R-1] == arr[R] else R-1
                L = R
                prevSign = ""
                R += 1
        return res