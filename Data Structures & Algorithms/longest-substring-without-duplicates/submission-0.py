class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 0
        chars = set()
        max_len = 0

        while j < n:
            if s[j] in chars:
                while s[j] in chars :
                    chars.remove(s[i])
                    i += 1 
            chars.add(s[j])
            j += 1
            max_len = max(max_len,len(chars))
        
        return max_len 