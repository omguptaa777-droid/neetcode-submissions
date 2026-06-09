class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        m = len(word1)
        n = len(word2)

        while i < m and i < n:
            res.append(word1[i]) 
            res.append(word2[i]) 
            i += 1
        
        res.append(word1[i:])
        res.append(word2[i:])

        return "".join(res)
 