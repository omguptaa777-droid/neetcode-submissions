class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not len(t):
            return ""
        countT = defaultdict(int)

        for ch in t:
            countT[ch] += 1
        
        window = defaultdict(int)
        have = 0
        need = len(countT)
        res = [-1,-1]
        resLen = float('inf')
        l = 0

        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1

            while have == need:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    res[0] = l
                    res[1] = r

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        return "" if resLen == float('inf') else s[res[0]:res[1]+1]
