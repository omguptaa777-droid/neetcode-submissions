class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        st = []

        for c in tokens:
            if c not in {"+","-","*","/"}:
                st.append(int(c))
                continue

            elif c == "+":
                op1 = st.pop()
                op2 = st.pop()
                res = op2 + op1

            elif c == "-":
                op1 = st.pop()
                op2 = st.pop()
                res = op2 - op1

            elif c == "*":
                op1 = st.pop()
                op2 = st.pop()
                res = op1 * op2

            else:
                op1 = st.pop()
                op2 = st.pop()
                res = int(op2 / op1)
                
            st.append(res)
        
        return st[0]
