class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCons = 0
        currCons = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currCons += 1
            else:
                currCons = 0
            if currCons > maxCons:
                maxCons = currCons
        return maxCons
        