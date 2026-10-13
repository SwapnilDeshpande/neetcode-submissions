class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        minLength = float('inf')
        sum = 0
        # For every element add it to the sum
        for R in range(len(nums)):
            sum += nums[R]
            # While the sum is greater than or equal to target
            # shrink window from left
            while sum >= target:
                minLength = min(minLength, R-L+1)
                sum -= nums[L]
                L += 1
        # Return the min length
        return minLength if minLength != float('inf') else 0