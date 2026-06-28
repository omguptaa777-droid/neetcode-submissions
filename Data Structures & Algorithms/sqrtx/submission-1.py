class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        l = 0
        r = x // 2

        while l <= r:
            mid = (l+r)//2

            if mid*mid < x:
                l = mid + 1
            elif mid*mid > x:
                r = mid - 1
            else:
                return mid
        
        return l - 1