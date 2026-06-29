class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def solver(maxWeight):
            time = 0
            total = 0
            for x in weights:
                if total + x <= maxWeight:
                    total += x
                else:
                    time += 1
                    total = x
            time += 1
            return time


        i = max(weights)
        j = sum(weights)

        while i < j:
            m = (i+j)//2

            if solver(m) > days:
                i = m + 1
            else:
                j = m
        
        return i