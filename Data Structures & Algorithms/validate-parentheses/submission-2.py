class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        map = {"[":"]",
            "(":")",
            "{":"}"
        }
        for b in s:
            if b in map:
                st.append(b)
            else:
                if not st or map[st.pop()] != b:
                    return False
        
        return False if st else True