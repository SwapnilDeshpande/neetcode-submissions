class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = list()
        left = 0
        count = 0
        for right in range(len(arr)):
            window.append(arr[right])
            if right - left + 1 > k:
                del window[0]
                left += 1
            if right - left + 1 == k:
                sum = 0
                for num in window:
                    sum += num
                avg = sum/k
                if avg >= threshold:
                    count += 1
        return count