class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        i = 0
        m = len(word1)
        n = len(word2)

        while i < m and i < n:
            res += word1[i]
            res += word2[i]
            i += 1
        
        res += word1[i:]
        res += word2[i:]

        return res
 