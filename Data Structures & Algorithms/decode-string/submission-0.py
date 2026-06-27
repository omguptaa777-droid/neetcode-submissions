class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                curr = ''
                while stack[-1] != '[':
                    curr = stack.pop() + curr
                stack.pop()
                num = 0
                i = 0
                while stack and stack[-1] in {'0','1','2','3','4','5','6','7','8','9'}:
                    num += (10**i * int(stack.pop()))
                    i += 1
                stack.append(curr * num)
            
        return "".join(stack)