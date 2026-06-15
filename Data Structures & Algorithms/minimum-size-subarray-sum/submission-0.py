class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0
        total = 0
        minLen = 100001

        while j < n:
            total += nums[j]

            if total >= target:
                minLen = min(minLen,j-i+1)
                while total >= target:
                    total -= nums[i]
                    i += 1
                minLen = min(minLen,j-i+2)
            j += 1

        return minLen if minLen != 100001 else 0