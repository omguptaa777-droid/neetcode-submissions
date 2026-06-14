class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k = len(s1)
        i = 0
        j = 0

        counter1 = {}

        for ch in s1:
            counter1[ch] = 1 + counter1.get(ch,0)
        
        counter2 = {}

        while j < n:
            counter2[s2[j]] = 1 + counter2.get(s2[j],0)
            
            if j-i+1 > k:
                counter2[s2[i]] -= 1
                if counter2[s2[i]] == 0:
                    del counter2[s2[i]]
                i += 1

            if counter1 == counter2 and j-i+1 == k:
                    return True
            
            j += 1

        return False 


             