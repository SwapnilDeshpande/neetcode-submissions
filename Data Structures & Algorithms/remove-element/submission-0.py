class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        bPtr = 0
        ePtr = len(nums)-1
        while ePtr >= bPtr:
            if nums[bPtr] == val:
                nums[bPtr] = nums[ePtr]
                ePtr -= 1
            else:
                bPtr += 1
        return bPtr