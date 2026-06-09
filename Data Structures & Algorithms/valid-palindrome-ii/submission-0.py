class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n - 1
        k = 1

        while i < j:
            if s[i] != s[j]:
                i += 1
                k -= 1
            else:
                i += 1
                j -= 1
        if k >= 0:
            return True
        
        i = 0
        j = n - 1
        k = 1
        
        while i < j:
            if s[i] != s[j]:
                j -= 1
                k -= 1
            else:
                i += 1
                j -= 1
        if k >= 0:
            return True
        return False
