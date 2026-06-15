class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l = 0
        r = n - 1
        res = []

        while r - l >= k:
            if abs(x-arr[l]) > abs(x-arr[r]):
                l += 1
            else:
                r -= 1
            
        return arr[l:r+1]
