class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l = 1
        r = mountainArr.length() - 2
        peak = 0

        while l <= r:
            mid = (l+r)//2

            if mountainArr.get(mid-1) < mountainArr.get(mid) < mountainArr.get(mid+1):
                l = mid + 1
            elif mountainArr.get(mid-1) > mountainArr.get(mid) > mountainArr.get(mid+1):
                r = mid - 1
            else:
                peak = mid 
                break
        l = 0
        r = peak
        while l <= r:
            mid = (l+r)//2

            if mountainArr.get(mid) < target:
                l = mid + 1
            elif mountainArr.get(mid) > target:
                r = mid - 1
            else:
                return mid

        l = peak
        r = mountainArr.length() - 1

        while l <= r:
            mid = (l+r)//2

            if mountainArr.get(mid) < target:
                r = mid - 1
            elif mountainArr.get(mid) > target:
                l = mid + 1
            else:
                return mid
        
        return -1
