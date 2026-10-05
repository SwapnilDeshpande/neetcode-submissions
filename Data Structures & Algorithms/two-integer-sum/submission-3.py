class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        result = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numsMap:
                result.append(numsMap[complement])
                result.append(i)
                return result
            numsMap[nums[i]] = i