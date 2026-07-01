class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(m):
            currSum = 0
            subarrays = 1

            for n in nums:
                currSum += n
                if currSum > m:
                    subarrays += 1
                    if subarrays > k:
                        return False
                    currSum = n
            return True

        l,r = max(nums),sum(nums)
        res = r

        while l <= r:
            mid = (l+r)//2

            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res
