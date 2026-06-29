class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def solver(k):
            time = 0
            for x in piles:
                time += math.ceil(x/k)
            return time

        i = 1
        j = max(piles)

        while i < j:
            k = (i+j)//2

            if solver(k) > h:
                i = k + 1
            elif solver(k) <= h:
                j = k 
        
        return i
