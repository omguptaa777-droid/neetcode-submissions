class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        if not strs[0]:
            return ''
            
        s = strs[0]
        res = ''

        for i in range(len(s)):
            for j in range(len(strs)):
                if s[i] != strs[j][i]:
                    return res
            res += s[i]
        
        return res
