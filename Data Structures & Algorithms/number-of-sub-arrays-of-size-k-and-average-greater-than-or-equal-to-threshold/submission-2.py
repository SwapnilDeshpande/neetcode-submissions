class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currSum = 0
        left = 0
        count = 0
        for right in range(len(arr)):
            currSum += arr[right]
            if right - left + 1 > k:
                currSum -= arr[left]
                left += 1
            if right - left + 1 == k:
                avg = currSum/k
                if avg >= threshold:
                    count += 1
        return count